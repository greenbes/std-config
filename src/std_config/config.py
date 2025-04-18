from enum import Enum
import logging
from pathlib import Path

import xdg_base_dirs
from pydantic import Field
from pydantic_settings import BaseSettings
import os


class LogLevel(str, Enum):
    """Standard logging levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class StdConfig(BaseSettings):
    """
    Standard configuration using pydantic-settings BaseSettings.

    Attributes:
        xdg_data_home: Base directory for user-specific data according to XDG specification.
            Uses xdg-base-dirs library to determine the default path.
        xdg_config_home: Base directory for user-specific configuration according to XDG specification.
            Uses xdg-base-dirs library to determine the default path.
        xdg_state_home: Base directory for user-specific state data according to XDG specification.
            Uses xdg-base-dirs library to determine the default path.
        log_level: Logging level to use.
            Defaults to INFO level.
            Can be set via LOG_LEVEL environment variable.
            Can be set using "-l" or "--long" command line arguments
    """
    xdg_data_home: Path = Field(
        default_factory=lambda: Path(xdg_base_dirs.xdg_data_home())
    )
    xdg_config_home: Path = Field(
        default_factory=lambda: Path(xdg_base_dirs.xdg_config_home())
    )
    xdg_state_home: Path = Field(
        default_factory=lambda: Path(xdg_base_dirs.xdg_state_home())
    )
    log_level: LogLevel = Field(
        default=LogLevel.INFO,
        description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
        validation_alias="LOG_LEVEL",
        arg_short="-l",
        arg_long="--log-level",
        environment_variable="LOG_LEVEL"
    )

    def from_cli(self) -> "StdConfig":
        """Construct StdConfig instance by parsing command-line arguments."""
        import argparse
        from typing import get_type_hints

        parser = argparse.ArgumentParser(description="Standard configuration utility")
        type_hints = get_type_hints(self.__class__)

        for field_name, field_info in self.model_fields.items():
            help_text = field_info.description
            default = field_info.default
            extras = field_info.json_schema_extra or {}
            arg_short = extras.get("arg_short")
            arg_long = extras.get("arg_long")

            if arg_short or arg_long:
                options = []
                if arg_short:
                    options.append(arg_short)
                if arg_long:
                    options.append(arg_long)

                kwargs = {"help": help_text, "default": default, "dest": field_name}
                if field_name in type_hints and hasattr(type_hints[field_name], "__members__"):
                    kwargs["choices"] = [level.value for level in type_hints[field_name].__members__.values()]

                parser.add_argument(*options, **kwargs)

        args = parser.parse_args()
        config = self
        args_dict = vars(args)

        for field_name, field_info in self.model_fields.items():
            if field_name in args_dict:
                value = args_dict[field_name]
                if value is not None and value != field_info.default:
                    setattr(config, field_name, value)

        return self

    def from_environment(self) -> "StdConfig":
        """
        Load configuration from environment variables for fields with an environment_variable extra.
        """
        import os
        from pydantic import TypeAdapter, ValidationError

        for field_name, field_info in self.model_fields.items():
            extras = field_info.json_schema_extra or {}
            env_var = extras.get("environment_variable")
            if env_var:
                raw = os.getenv(env_var)
                if raw:
                    adapter = TypeAdapter(field_info.annotation)
                    try:
                        value = adapter.validate_python(raw)
                    except ValidationError:
                        value = raw
                    setattr(self, field_name, value)
        return self

    def print_fields(self) -> None:
        """Print all configuration fields to stdout."""
        for field_name, field_info in self.model_fields.items():
            value = getattr(self, field_name)
            label = field_info.description or field_name.replace("_", " ").capitalize()
            print(f"{label}: {value}")
