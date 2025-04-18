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

Values are applied in the following order (lowest to highest priority):

1. Default values defined in the Pydantic model  
2. Values from configuration files in XDG directories
3. Environment variables  
4. Command-line arguments

## Supported Formats

std-config supports configuration files in multiple formats:

- TOML (highest priority)
- JSON (medium priority)
- YAML (lowest priority)

## Usage

```python
from std_config import StdConfig

# Parse configuration file and command line arguments 
config = StdConfig.from_cli()

# Print all configuration fields
config.print_fields()
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

