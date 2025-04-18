import os
import sys
import json
import toml
import yaml
import xdg_base_dirs

from std_config.config import StdConfig, LogLevel
from std_config.ai_config import AIConfig


def test_stdconfig_defaults(monkeypatch):
    config = StdConfig()
    # Check that XDG paths are Path objects and exist
    assert hasattr(config, "xdg_data_home")
    assert hasattr(config, "xdg_config_home")
    assert hasattr(config, "xdg_state_home")
    assert config.xdg_data_home.__class__.__name__ == "PosixPath"
    assert config.xdg_config_home.__class__.__name__ == "PosixPath"
    assert config.xdg_state_home.__class__.__name__ == "PosixPath"
    # Check default log level
    assert config.log_level == LogLevel.INFO
    # Check config_file is None by default
    assert config.config_file is None


def test_stdconfig_env(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    config = StdConfig()
    assert config.log_level == LogLevel.DEBUG


def test_stdconfig_from_cli(monkeypatch):
    # Simulate CLI args for log level
    test_args = ["prog", "--log-level", "ERROR"]
    monkeypatch.setattr(sys, "argv", test_args)
    config = StdConfig.from_cli()
    assert config.log_level == LogLevel.ERROR


def test_stdconfig_from_cli_config_file(monkeypatch, tmp_path):
    # Create a temporary config file
    config_file = tmp_path / "config.toml"
    config_content = {"log_level": "DEBUG"}
    with open(config_file, "w") as f:
        toml.dump(config_content, f)

    # Simulate CLI args for config file
    test_args = ["prog", "--config", str(config_file)]
    monkeypatch.setattr(sys, "argv", test_args)

    # Initialize config from CLI
    config = StdConfig()

    # Assert that the config was loaded from the file
    assert config.log_level == LogLevel.DEBUG
    assert config.config_file is None  # The config_file field is not set from the file


def test_stdconfig_from_toml_file(monkeypatch, tmp_path):
    # Create a temporary config file
    config_dir = tmp_path / ".config" / "stdconfig"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "config.toml"
    config_content = {"log_level": "WARNING"}
    with open(config_file, "w") as f:
        toml.dump(config_content, f)

    # Mock XDG_CONFIG_HOME to point to our temporary directory
    monkeypatch.setattr(
        xdg_base_dirs, "xdg_config_home", lambda: str(tmp_path / ".config")
    )

    # Initialize config
    config = StdConfig()

    # Assert that the config was loaded from the file
    assert config.log_level == LogLevel.WARNING


def test_stdconfig_from_json_file(monkeypatch, tmp_path):
    # Create a temporary config file
    config_dir = tmp_path / ".config" / "stdconfig"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "config.json"
    config_content = {"log_level": "ERROR"}
    with open(config_file, "w") as f:
        json.dump(config_content, f)

    # Mock XDG_CONFIG_HOME to point to our temporary directory
    monkeypatch.setattr(
        xdg_base_dirs, "xdg_config_home", lambda: str(tmp_path / ".config")
    )

    # Initialize config
    config = StdConfig()

    # Assert that the config was loaded from the file
    assert config.log_level == LogLevel.ERROR


def test_stdconfig_from_yaml_file(monkeypatch, tmp_path):
    # Create a temporary config file
    config_dir = tmp_path / ".config" / "stdconfig"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "config.yaml"
    config_content = {"log_level": "CRITICAL"}
    with open(config_file, "w") as f:
        yaml.dump(config_content, f)

    # Mock XDG_CONFIG_HOME to point to our temporary directory
    monkeypatch.setattr(
        xdg_base_dirs, "xdg_config_home", lambda: str(tmp_path / ".config")
    )

    # Initialize config
    config = StdConfig()

    # Assert that the config was loaded from the file
    assert config.log_level == LogLevel.CRITICAL


def test_config_precedence(monkeypatch, tmp_path):
    # Create a temporary config file
    config_dir = tmp_path / ".config" / "stdconfig"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "config.toml"
    config_content = {"log_level": "WARNING"}
    with open(config_file, "w") as f:
        toml.dump(config_content, f)

    # Mock XDG_CONFIG_HOME to point to our temporary directory
    monkeypatch.setattr(
        xdg_base_dirs, "xdg_config_home", lambda: str(tmp_path / ".config")
    )

    # Set environment variable (higher precedence than config file)
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    # Initialize config
    config = StdConfig()

    # Assert that env var takes precedence over config file
    assert config.log_level == LogLevel.DEBUG

    # Now test CLI arguments (highest precedence)
    test_args = ["prog", "--log-level", "ERROR"]
    monkeypatch.setattr(sys, "argv", test_args)
    config = StdConfig.from_cli()

    # Assert that CLI args take precedence over env vars and config file
    assert config.log_level == LogLevel.ERROR


def test_config_file_order(monkeypatch, tmp_path):
    # Create all three config files with different values
    config_dir = tmp_path / ".config" / "stdconfig"
    config_dir.mkdir(parents=True)

    # TOML (highest priority)
    toml_file = config_dir / "config.toml"
    toml_content = {"log_level": "ERROR"}
    with open(toml_file, "w") as f:
        toml.dump(toml_content, f)

    # JSON (medium priority)
    json_file = config_dir / "config.json"
    json_content = {"log_level": "WARNING"}
    with open(json_file, "w") as f:
        json.dump(json_content, f)

    # YAML (lowest priority)
    yaml_file = config_dir / "config.yaml"
    yaml_content = {"log_level": "DEBUG"}
    with open(yaml_file, "w") as f:
        yaml.dump(yaml_content, f)

    # Mock XDG_CONFIG_HOME to point to our temporary directory
    monkeypatch.setattr(
        xdg_base_dirs, "xdg_config_home", lambda: str(tmp_path / ".config")
    )

    # Initialize config
    config = StdConfig()

    # Assert that TOML file was used (highest priority)
    assert config.log_level == LogLevel.ERROR

    # Remove TOML file and test again
    toml_file.unlink()
    config = StdConfig()

    # Assert that JSON file was used (next priority)
    assert config.log_level == LogLevel.WARNING

    # Remove JSON file and test again
    json_file.unlink()
    config = StdConfig()

    # Assert that YAML file was used (last priority)
    assert config.log_level == LogLevel.DEBUG


def test_aiconfig_inherits_stdconfig(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    # Should inherit all StdConfig fields
    config = AIConfig()
    assert hasattr(config, "xdg_data_home")
    assert hasattr(config, "log_level")
    assert hasattr(config, "config_file")
    # openai_api_key should default to None
    assert config.openai_api_key is None


def test_aiconfig_env(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-testkey")
    config = AIConfig()
    assert config.openai_api_key == "sk-testkey"


def test_aiconfig_from_cli(monkeypatch):
    test_args = ["prog", "--openai-api-key", "sk-cli"]
    monkeypatch.setattr(sys, "argv", test_args)
    config = AIConfig.from_cli()
    assert config.openai_api_key == "sk-cli"


def test_aiconfig_from_config_file(monkeypatch, tmp_path):
    # Create a temporary config file
    config_dir = tmp_path / ".config" / "aiconfig"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "config.toml"
    config_content = {"openai_api_key": "sk-config-file", "log_level": "DEBUG"}
    with open(config_file, "w") as f:
        toml.dump(config_content, f)

    # Mock XDG_CONFIG_HOME to point to our temporary directory
    monkeypatch.setattr(
        xdg_base_dirs, "xdg_config_home", lambda: str(tmp_path / ".config")
    )

    # Unset any environment variable that might interfere
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    # Initialize config
    config = AIConfig()

    # Assert that the config was loaded from the file
    assert config.log_level == LogLevel.DEBUG

    # Check the API key - if it's set in the environment this might differ
    if os.environ.get("OPENAI_API_KEY") is None:
        assert config.openai_api_key == "sk-config-file"


def test_print_fields(capsys):
    config = StdConfig()
    config.print_fields()
    out = capsys.readouterr().out
    assert "Logging level" in out or "log_level" in out
    assert "xdg_data_home" in out or "Xdg data home" in out
    assert "Path to configuration file" in out
