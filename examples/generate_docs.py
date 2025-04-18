#!/usr/bin/env python3
"""
Example script showing how to generate documentation from configuration schema.
"""
from pathlib import Path
from std_config import StdConfig, SchemaDocGenerator
from std_config.ai_config import AIConfig


def main():
    """Generate documentation for StdConfig and AIConfig classes."""
    # Ensure the output directory exists
    output_dir = Path("./docs/schema")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate Markdown documentation
    print("Generating StdConfig documentation...")
    SchemaDocGenerator.save_markdown(
        StdConfig, output_dir / "std_config_schema.md"
    )
    
    print("Generating AIConfig documentation...")
    SchemaDocGenerator.save_markdown(
        AIConfig, output_dir / "ai_config_schema.md"
    )
    
    # Generate JSON schema documentation
    SchemaDocGenerator.save_json(
        StdConfig, output_dir / "std_config_schema.json"
    )
    SchemaDocGenerator.save_json(
        AIConfig, output_dir / "ai_config_schema.json"
    )
    
    print(f"Documentation generated in {output_dir.absolute()}")
    
    # Print example markdown to console
    print("\nExample Markdown for StdConfig:")
    print(SchemaDocGenerator.to_markdown(StdConfig))


if __name__ == "__main__":
    main()