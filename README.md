# std-config

[![PyPI Version](https://img.shields.io/pypi/v/std-config.svg)](https://pypi.org/project/std-config)
[![Build Status](https://github.com/<username>/std-config/actions/workflows/ci.yml/badge.svg)](https://github.com/<username>/std-config/actions)
[![Coverage Status](https://coveralls.io/repos/github/<username>/std-config/badge.svg?branch=main)](https://coveralls.io/github/<username>/std-config?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

std-config is a Pydantic-powered configuration loader that merges defaults, XDG base directories, environment variables, and command-line arguments in a sensible order.

## Table of Contents
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Configuration Precedence](#configuration-precedence)
- [Supported Formats](#supported-formats)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Installation

Install from PyPI:

```bash
pip install std-config
```

Or from source:

```bash
git clone https://github.com/<username>/std-config.git
cd std-config
pip install .
```

## Quickstart

### Programmatic Usage

```python
from pydantic import BaseModel, Field
from std_config import load_config

class MyConfig(BaseModel):
    foo: str = Field("default_value", env="FOO", arg_long="--foo")
    bar: int = Field(42, env="BAR", arg_short="-b")

cfg = load_config(MyConfig)
print(cfg.foo, cfg.bar)
```

## Configuration Precedence

Values are applied in the following order (lowest to highest priority):

1. Default values defined in the Pydantic model  
2. XDG base directories (from `$XDG_CONFIG_HOME`, `$HOME/.config`, etc.)  
3. Configuration file values (applied by `pydantic-settings`)  
4. Environment variables  
5. Command-line arguments

## Supported Formats

std-config uses Pydantic Settings under the hood and supports any format supported by Pydantic Settings (e.g., JSON, TOML, YAML).

Configuration files are searched in these locations by default:
- `$XDG_CONFIG_HOME/<app_name>/config.(json|toml|yaml)`
- `$HOME/.config/<app_name>/config.(json|toml|yaml)`

## API Reference

- `load_config(config_model: Type[BaseModel], **kwargs) -> BaseModel`  
  Load configuration into an instance of your Pydantic model.

- Field arguments:  
  - `env`: Environment variable name  
  - `arg_long`: Long CLI argument (e.g., `--foo`)  
  - `arg_short`: Short CLI argument (e.g., `-f`)

See the code or docs for more advanced usage.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started, code style, and submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


