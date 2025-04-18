from enum import Enum
from pathlib import Path
from typing import Optional, get_type_hints, Any, Dict

import xdg_base_dirs
from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
    JsonConfigSettingsSource,
    TomlConfigSettingsSource,
    YamlConfigSettingsSource,
)
import argparse
import logging

logger = logging.getLogger(__name__)


class LogLevel(str, Enum):
    """Standard logging levels."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


# Create a basic empty settings source for when no config file is found
class EmptySettingsSource(PydanticBaseSettingsSource):
    """An empty settings source that returns no settings."""

    def get_field_value(
        self, field_name: str, field_info: Any
    ) -> tuple[Any, str, bool]:
        return None, field_name, False

    def __call__(self) -> Dict[str, Any]:
        return {}


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
            Can be set using "-l" or "--log-level" command line arguments
        config_file: Path to configuration file.
            Can be set using "-c" or "--config" command line arguments
    """

    model_config = SettingsConfigDict(env_prefix="")
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
        json_schema_extra={
            "env": "LOG_LEVEL",
            "arg_short": "-l",
            "arg_long": "--log-level",
        },
    )
    config_file: Optional[Path] = Field(
        default=None,
        description="Path to configuration file",
        json_schema_extra={"arg_short": "-c", "arg_long": "--config"},
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Customize settings sources to support configuration files."""
        # First get values from CLI and environment to check if config_file was specified
        config_settings = cls._get_config_settings(settings_cls)

        # Return sources in priority order (highest to lowest)
        return (
            init_settings,  # 1. Values passed to the constructor
            env_settings,  # 2. Environment variables (higher priority than config file)
            config_settings,  # 3. Values from config file
            dotenv_settings,  # 4. Dotenv file
            file_secret_settings,  # 5. Secret files
        )

    @classmethod
    def _get_config_settings(
        cls, settings_cls: type[BaseSettings]
    ) -> PydanticBaseSettingsSource:
        """Get settings from configuration file."""
        # Parse command line arguments to get config_file if specified
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
            "-c", "--config", dest="config_file", help="Configuration file path"
        )
        args, _ = parser.parse_known_args()

        config_file = args.config_file if hasattr(args, "config_file") else None

        if config_file:
            # Use the specified config file
            config_path = Path(config_file)
            if config_path.exists():
                if config_path.suffix == ".toml":
                    return TomlConfigSettingsSource(
                        settings_cls, toml_file=str(config_path)
                    )
                elif config_path.suffix == ".json":
                    return JsonConfigSettingsSource(
                        settings_cls, json_file=str(config_path)
                    )
                elif config_path.suffix in [".yaml", ".yml"]:
                    return YamlConfigSettingsSource(
                        settings_cls, yaml_file=str(config_path)
                    )
        else:
            # Look for config files in XDG_CONFIG_HOME
            app_name = settings_cls.__name__.lower()
            xdg_config_home = Path(xdg_base_dirs.xdg_config_home())
            config_dir = xdg_config_home / app_name
            logger.debug(f"Looking for config files in {config_dir}")
            # Ensure the directory exists before trying to read from it
            try:
                config_dir.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                logger.warning(f"Could not create config directory {config_dir}: {e}")
                # Continue without XDG config if directory creation fails

            # Check for config files in order
            toml_path = config_dir / "config.toml"
            if toml_path.exists():
                logger.debug(f"Loading config from TOML file: {toml_path}")
                return TomlConfigSettingsSource(settings_cls, toml_file=str(toml_path))

            json_path = config_dir / "config.json"
            if json_path.exists():
                logger.debug(f"Loading config from JSON file: {json_path}")
                return JsonConfigSettingsSource(settings_cls, json_file=str(json_path))

            yaml_path = config_dir / "config.yaml"
            if yaml_path.exists():
                logger.debug(f"Loading config from YAML file: {yaml_path}")
                return YamlConfigSettingsSource(settings_cls, yaml_file=str(yaml_path))

            logger.debug("No config file found in XDG directory.")

        # Return empty settings source if no config file is found
        logger.debug("No config file specified or found.")
        return EmptySettingsSource(settings_cls)

    @classmethod
    def from_cli(cls) -> "StdConfig":
        """Construct StdConfig instance by parsing command-line arguments."""
        parser = argparse.ArgumentParser(description="Standard configuration utility")
        type_hints = get_type_hints(cls)

        for field_name, field_info in cls.model_fields.items():
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
                if field_name in type_hints and hasattr(
                    type_hints[field_name], "__members__"
                ):
                    kwargs["choices"] = [
                        level.value
                        for level in type_hints[field_name].__members__.values()
                    ]

                parser.add_argument(*options, **kwargs)

        args = parser.parse_args()
        config = cls()
        args_dict = vars(args)

        for field_name, field_info in cls.model_fields.items():
            if field_name in args_dict:
                value = args_dict[field_name]
                if value is not None and value != field_info.default:
                    setattr(config, field_name, value)

        return config

    def print_fields(self) -> None:
        """Print all configuration fields to stdout."""
        for field_name, field_info in type(self).model_fields.items():
            value = getattr(self, field_name)
            label = field_info.description or field_name.replace("_", " ").capitalize()
            print(f"{label}: {value}")
