# Development Steps

This file lists the steps to be performed in order to complete the project. Only work on the next incomplete step.

- Completed steps are marked with "- [X] "
- Incomplete steps are marked with "- [ ] "

## The StdConfig class

- [X] CREATE a new class called `StdConfig` that is a subclass of `BaseSettings` (provided by `pydantic-settings`)
- [X] Add a field to `StdConfig` called `xdg_data_home`. It should default to the XDG value for `$XDG_DATA_HOME`.
- [X] Add a field to `StdConfig` called `xdg_config_home`. It should default to the XDG value for `$XDG_CONFIG_HOME`.
- [X] Add a field to `StdConfig` called `xdg_state_home`. It should default to the XDG value for `$XDG_STATE_HOME`.

## Additional StdConfig Features

- [X] Add a field to `StdConfig` called `log_level`. It should:
  - Use Python's `Enum` to only accept standard logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Default to INFO level
  - Be accessible via environment variable `LOG_LEVEL`
  - Be configurable from the command line using `-l` or `--log-level`



