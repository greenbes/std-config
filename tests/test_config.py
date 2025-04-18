import os
import sys
import types
import importlib
import pytest

from src.std_config.config import StdConfig, LogLevel
from src.std_config.ai_config import AIConfig

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

def test_aiconfig_inherits_stdconfig(monkeypatch):
    # Should inherit all StdConfig fields
    config = AIConfig()
    assert hasattr(config, "xdg_data_home")
    assert hasattr(config, "log_level")
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

def test_print_fields(capsys):
    config = StdConfig()
    config.print_fields()
    out = capsys.readouterr().out
    assert "Logging level" in out or "log_level" in out
    assert "xdg_data_home" in out or "Xdg data home" in out
