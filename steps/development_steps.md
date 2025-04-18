# Development Steps

This file lists the steps to be performed in order to complete the project. Only work on the next incomplete step.

- Completed steps are marked with "- [X] "
- Incomplete steps are marked with "- [ ] "

## The StdConfig class

- [X] CREATE a new class called `StdConfig` that is a subclass of `BaseSettings` (provided by `pydantic-settings`)
- [X] Add a field to `StdConfig` called `xdg_data_home`. It should default to the XDG value for `$XDG_DATA_HOME`.
- [X] Add a field to `StdConfig` called `xdg_config_home`. It should default to the XDG value for `$XDG_CONFIG_HOME`.
- [X] Add a field to `StdConfig` called `xdg_state_home`. It should default to the XDG value for `$XDG_STATE_HOME`.
- [X] Add a field to `StdConfig` called `log_level`. It should:
  - Use Python's `Enum` to only accept standard logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Default to INFO level
  - Be accessible via environment variable `LOG_LEVEL`
  - Be configurable from the command line using `-l` or `--log-level`
- [X] Read configuration values from a file. First check whether the `-c` or `--config` options were specified on the command line. If so, load the configuration from the provided file. If no configuration file was specified on the command line, look in the XDG_CONFIG_HOME directory for a configuration file. Check for files in this order:

    1. `config.toml`
    2. `config.json`
    3. `config.yaml`
    
    As soon as one of these files is found, do not load any other configuration files.

## Additional Features

- [X] Schema Documentation
  - Add a `SchemaDocGenerator` class that can generate documentation from configuration classes
  - Support Markdown and JSON output formats
  - Include field names, types, descriptions, defaults, and env/CLI options
  - Provide methods to save documentation to files
  - Add examples showing how to use the schema documentation feature

- [ ] Configuration Profiles
  - Add support for named configuration profiles (dev, test, prod)
  - Make it easy to switch between different environments
  - Support profile-specific config file locations
  
- [ ] Config Export Functionality
  - Add methods to export current configuration to files (TOML/JSON/YAML)
  - Enable saving modified configs and generating template config files
  
- [ ] Config Change Notification
  - Add support for observers/callbacks when configuration changes
  - Allow components to react to configuration changes without polling

