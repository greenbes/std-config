import json
import tempfile
from pathlib import Path
from typing import Optional

from pydantic import Field

from std_config import SchemaDocGenerator, StdConfig
from std_config.ai_config import AIConfig


def test_schema_doc_generator_fields():
    """Test that the schema documentation generator extracts fields correctly."""
    fields = SchemaDocGenerator.get_schema_fields(StdConfig)
    field_names = [field.name for field in fields]
    
    # Check that all expected fields are extracted
    assert "xdg_data_home" in field_names
    assert "xdg_config_home" in field_names
    assert "xdg_state_home" in field_names
    assert "log_level" in field_names
    assert "config_file" in field_names
    
    # Check field details
    log_level_field = next(field for field in fields if field.name == "log_level")
    assert log_level_field.description == "Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
    assert log_level_field.env_var == "LOG_LEVEL"
    assert "-l" in log_level_field.cli_args
    assert "--log-level" in log_level_field.cli_args
    assert log_level_field.choices is not None
    assert "DEBUG" in log_level_field.choices
    
    # Check inherited fields in AIConfig
    ai_fields = SchemaDocGenerator.get_schema_fields(AIConfig)
    ai_field_names = [field.name for field in ai_fields]
    
    assert "openai_api_key" in ai_field_names
    assert "log_level" in ai_field_names  # Inherited from StdConfig


def test_markdown_generation():
    """Test that Markdown documentation is generated correctly."""
    markdown = SchemaDocGenerator.to_markdown(StdConfig)
    
    # Check that the markdown contains expected sections
    assert "# StdConfig Configuration" in markdown
    assert "## Configuration Fields" in markdown
    assert "| Field | Type | Description |" in markdown
    
    # Check that fields are documented
    assert "| `log_level` |" in markdown
    assert "| `xdg_data_home` |" in markdown


def test_json_generation():
    """Test that JSON schema documentation is generated correctly."""
    json_schema = SchemaDocGenerator.to_json(StdConfig)
    schema_dict = json.loads(json_schema)
    
    assert schema_dict["name"] == "StdConfig"
    assert "description" in schema_dict
    assert "fields" in schema_dict
    
    # Check that fields are documented
    field_names = [field["name"] for field in schema_dict["fields"]]
    assert "log_level" in field_names
    assert "xdg_data_home" in field_names


def test_save_markdown():
    """Test saving markdown documentation to a file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "test_schema.md"
        SchemaDocGenerator.save_markdown(StdConfig, output_path)
        
        # Verify that file exists and contains content
        assert output_path.exists()
        content = output_path.read_text()
        assert "# StdConfig Configuration" in content


def test_save_json():
    """Test saving JSON schema documentation to a file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "test_schema.json"
        SchemaDocGenerator.save_json(StdConfig, output_path)
        
        # Verify that file exists and contains valid JSON
        assert output_path.exists()
        content = output_path.read_text()
        schema_dict = json.loads(content)
        assert schema_dict["name"] == "StdConfig"


def test_custom_config_documentation():
    """Test documenting a custom configuration class."""
    
    class CustomConfig(StdConfig):
        """Custom configuration for testing documentation."""
        
        api_key: Optional[str] = Field(
            default=None,
            description="API key for external service",
            json_schema_extra={
                "env": "API_KEY",
                "arg_long": "--api-key"
            }
        )
        debug_mode: bool = Field(
            default=False,
            description="Enable debug mode",
            json_schema_extra={
                "env": "DEBUG_MODE",
                "arg_short": "-d",
                "arg_long": "--debug"
            }
        )
    
    fields = SchemaDocGenerator.get_schema_fields(CustomConfig)
    field_names = [field.name for field in fields]
    
    # Check inherited and new fields
    assert "log_level" in field_names  # From StdConfig
    assert "api_key" in field_names    # New field
    assert "debug_mode" in field_names # New field
    
    # Check that markdown generation works
    markdown = SchemaDocGenerator.to_markdown(CustomConfig)
    assert "# CustomConfig Configuration" in markdown
    assert "Custom configuration for testing documentation" in markdown
    assert "| `api_key` |" in markdown
    assert "| `debug_mode` |" in markdown