from enum import Enum
import logging
from pathlib import Path

import xdg_base_dirs
from pydantic import Field
from pydantic_settings import BaseSettings


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
        arg_long="--log-level"
    )
