# std-config

> This is just a convenience library to handle a common pattern and introduces no new functionality.

To use this module:

1. Create a subclass of `StdConfig` (see `AIConfig` for an example)
    - Define fields using `pydantic-settings` format
    - Use `arg_short` and `arg_long` to specify command line arguments
2. Create a configuration file named `config.conl` in `$XDG_CONFIG_HOME` 
    - JSON and YAML are also supported
3. Import the library
    ```
    from std_config import StdConfig
    ```
4. Call the configuration loader
    ```
    config = StdConfig.from_cli()
    ```

    - The library handles command line arguments
    - Pydantic-settings automatically loads environment variables that match the field names

Large sections of this module were written by OpenAI and Claude.

## Key Features

- **Standardized Configuration Framework**: Uses Pydantic and Pydantic-Settings for robust validation and parsing
- **XDG Base Directory Support**: Automatically follows XDG specifications for config file locations 
- **Multiple Configuration Sources**: Elegantly merges values from defaults, files, environment variables, and CLI
- **Multiple File Format Support**: Load configuration from JSON, TOML, or YAML files
- **Extensible Base Class**: Easily extend `StdConfig` for custom configuration needs (see `AIConfig` example)
- **Type Safety**: Leverages Pydantic's type validation for safe configuration handling

## Configuration Precedence

Configuration values are loaded and merged with the following priority order (lowest to highest):

1.  **Default values**: Defined within the Pydantic model class itself.
2.  **Configuration file**: Values loaded from the first found configuration file (`config.toml`, `config.json`, or `config.yaml`) located in `$XDG_CONFIG_HOME/<app_name>/` or a specific file path provided via the `--config` argument.
3.  **Environment variables**: Values loaded from environment variables (e.g., `LOG_LEVEL`).
4.  **Command-line arguments**: Values explicitly passed via CLI arguments (e.g., `--log-level DEBUG`). These have the highest priority.

## Supported Formats

std-config automatically searches for configuration files within an application-specific subdirectory under `$XDG_CONFIG_HOME`. The subdirectory name (`<app_name>`) is derived from the lowercase name of your `StdConfig` subclass (e.g., `stdconfig` for `StdConfig`, `aiconfig` for `AIConfig`).

It looks for files in the following order within `$XDG_CONFIG_HOME/<app_name>/`:

1.  `config.toml`
2.  `config.json`
3.  `config.yaml`

The *first* file found in this sequence is loaded. If a specific configuration file is provided using the `-c` or `--config` command-line argument, that file is loaded instead, supporting `.toml`, `.json`, `.yaml`, or `.yml` extensions.

## Usage

First, create your own configuration class by subclassing `StdConfig` and defining your application-specific fields. See `src/std_config/ai_config.py` for an example (`AIConfig`).

Then, use your custom class to load the configuration:

```python
# Assuming you have defined AIConfig inheriting from StdConfig
from .ai_config import AIConfig # Adjust import based on your project structure

# Parse configuration sources (defaults, file, env vars, CLI args)
config = AIConfig.from_cli()

# Access your configuration fields
print(f"Log Level: {config.log_level}")
if config.openai_api_key:
    print("OpenAI API Key is set.")
else:
    print("OpenAI API Key is not set.")

# You can also print all fields easily
# config.print_fields()
```

## Built-in Configuration

The `StdConfig` base class provides:

- `xdg_data_home`: Path to XDG data directory
- `xdg_config_home`: Path to XDG config directory
- `xdg_state_home`: Path to XDG state directory
- `log_level`: Configurable logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
- `config_file`: Optional path to a specific configuration file

## Schema Documentation

std-config includes a `SchemaDocGenerator` class that can automatically generate documentation for your configuration schemas in Markdown or JSON formats.

```python
from std_config import StdConfig, SchemaDocGenerator
from pathlib import Path

# Generate Markdown documentation
markdown_doc = SchemaDocGenerator.to_markdown(StdConfig)
print(markdown_doc)

# Save to a file
SchemaDocGenerator.save_markdown(StdConfig, Path("./docs/std_config_schema.md"))

# Generate JSON schema
json_schema = SchemaDocGenerator.to_json(StdConfig)
print(json_schema)

# Save JSON schema to a file
SchemaDocGenerator.save_json(StdConfig, Path("./docs/std_config_schema.json"))
```

This makes it easy to keep documentation in sync with your configuration classes and generate up-to-date reference material for users.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

