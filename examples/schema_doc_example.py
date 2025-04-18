#!/usr/bin/env python3
"""
Example of using the SchemaDocGenerator to document configuration classes.
"""
from pathlib import Path
from std_config import StdConfig, SchemaDocGenerator
from std_config.ai_config import AIConfig
from pydantic import Field


class AppConfig(StdConfig):
    """
    Custom application configuration extending StdConfig.
    
    This class demonstrates how to create a custom configuration
    that inherits from StdConfig and adds application-specific settings.
    """
    
    app_name: str = Field(
        default="my-app",
        description="Application name",
        json_schema_extra={
            "env": "APP_NAME",
            "arg_short": "-n",
            "arg_long": "--name"
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
    
    server_port: int = Field(
        default=8080,
        description="Server port number",
        json_schema_extra={
            "env": "PORT",
            "arg_long": "--port"
        }
    )


def main():
    """Generate and display schema documentation for configuration classes."""
    # Generate markdown documentation for StdConfig
    std_config_md = SchemaDocGenerator.to_markdown(StdConfig)
    print("# StdConfig Documentation\n")
    print(std_config_md)
    print("\n" + "-" * 80 + "\n")
    
    # Generate markdown documentation for AIConfig
    ai_config_md = SchemaDocGenerator.to_markdown(AIConfig)
    print("# AIConfig Documentation\n")
    print(ai_config_md)
    print("\n" + "-" * 80 + "\n")
    
    # Generate markdown documentation for custom AppConfig
    app_config_md = SchemaDocGenerator.to_markdown(AppConfig)
    print("# AppConfig Documentation\n")
    print(app_config_md)
    
    # Generate JSON schema
    output_dir = Path("./docs/schema")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\nSaving schema documentation to {output_dir.absolute()}")
    
    # Save documentation for all config classes
    SchemaDocGenerator.save_markdown(StdConfig, output_dir / "std_config_schema.md")
    SchemaDocGenerator.save_markdown(AIConfig, output_dir / "ai_config_schema.md") 
    SchemaDocGenerator.save_markdown(AppConfig, output_dir / "app_config_schema.md")
    
    # Save JSON schema
    SchemaDocGenerator.save_json(StdConfig, output_dir / "std_config_schema.json")
    SchemaDocGenerator.save_json(AIConfig, output_dir / "ai_config_schema.json")
    SchemaDocGenerator.save_json(AppConfig, output_dir / "app_config_schema.json")
    
    print("Schema documentation generated successfully!")


if __name__ == "__main__":
    main()