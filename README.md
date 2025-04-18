# std-config

[![PyPI Version](https://img.shields.io/pypi/v/std-config.svg)](https://pypi.org/project/std-config)
[![Build Status](https://github.com/<username>/std-config/actions/workflows/ci.yml/badge.svg)](https://github.com/<username>/std-config/actions)
[![Coverage Status](https://coveralls.io/repos/github/<username>/std-config/badge.svg?branch=main)](https://coveralls.io/github/<username>/std-config?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> std-config is a Pydantic-powered configuration loader that merges defaults, XDG base directories, environment variables, and command-line arguments in a sensible order. 

This is just a convenience library to handle a common pattern and introduces no new functionality.

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

Configuration files are searched in these locations by default:
- `$XDG_CONFIG_HOME/<app_name>/config.toml`
- `$XDG_CONFIG_HOME/<app_name>/config.json`
- `$XDG_CONFIG_HOME/<app_name>/config.yaml`

Where `<app_name>` is the lowercase name of your configuration class (e.g., `stdconfig` for `StdConfig`).

## Usage

### Basic Usage

```python
from std_config import StdConfig

# Load configuration from all sources
config = StdConfig()

# Access configuration values
print(f"Log level: {config.log_level}")
print(f"Config directory: {config.xdg_config_home}")

# Print all configuration fields
config.print_fields()
```

### Command-Line Integration

```python
from std_config import StdConfig

# Parse CLI arguments automatically
config = StdConfig.from_cli()
```

### Custom Configuration

```python
from std_config import StdConfig
from pydantic import Field
from typing import Optional

class MyAppConfig(StdConfig):
    """Custom application configuration."""
    
    app_name: str = Field(
        default="my-app",
        description="Application name",
        json_schema_extra={
            "env": "APP_NAME",
            "arg_short": "-n", 
            "arg_long": "--name"
        }
    )
    
    api_key: Optional[str] = Field(
        default=None,
        description="API key for external service",
        json_schema_extra={
            "env": "API_KEY",
            "arg_long": "--api-key"
        }
    )
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

