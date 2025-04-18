from pathlib import Path

import xdg_base_dirs
from pydantic import Field
from pydantic_settings import BaseSettings


class StdConfig(BaseSettings):
    """
    Standard configuration using pydantic-settings BaseSettings.

    Attributes:
        xdg_data_home: Base directory for user-specific data according to XDG specification.
            Uses xdg-base-dirs library to determine the default path.
    """
    xdg_data_home: Path = Field(
        default_factory=lambda: Path(xdg_base_dirs.xdg_data_home())
    )