import argparse
import sys
from typing import get_type_hints

from .config import StdConfig


def main():
    parser = argparse.ArgumentParser(description="Standard configuration utility")
    
    # Dynamically add arguments based on StdConfig fields
    type_hints = get_type_hints(StdConfig)
    
    for field_name, field_info in StdConfig.model_fields.items():
        help_text = field_info.description
        default = field_info.default
        
        # Only create command line options for fields with arg_short or arg_long
        # Custom field attributes are stored in json_schema_extra dict
        extras = field_info.json_schema_extra or {}
        arg_short = extras.get("arg_short")
        arg_long = extras.get("arg_long")
        
        if arg_short or arg_long:
            # Determine argument options
            options = []
            if arg_short:
                options.append(arg_short)
            if arg_long:
                options.append(arg_long)
            
            # Determine if we need choices for enum types
            kwargs = {"help": help_text, "default": default}
            if field_name in type_hints and hasattr(type_hints[field_name], "__members__"):
                kwargs["choices"] = [level.value for level in type_hints[field_name].__members__.values()]
            
            parser.add_argument(*options, **kwargs)
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Get environment variables and override with command line arguments
    config = StdConfig()
    
    # Update with command line arguments if specified
    args_dict = vars(args)
    for field_name, field_info in StdConfig.model_fields.items():
        # Map command line arg to field name (use arg_long without -- or arg_short without -)
        extras = field_info.json_schema_extra or {}
        arg_long = extras.get("arg_long")
        arg_short = extras.get("arg_short")
        
        arg_name = None
        if arg_long and arg_long.startswith("--"):
            arg_name = arg_long[2:]
        elif arg_short and arg_short.startswith("-"):
            arg_name = arg_short[1:]
        
        if arg_name and arg_name in args_dict:
            field_value = args_dict[arg_name]
            # Only override if the argument was explicitly specified
            if field_value is not None and field_value != default:
                setattr(config, field_name, field_value)
    
    # Example usage
    print("Configuration loaded:")
    for field_name, field_info in StdConfig.model_fields.items():
        value = getattr(config, field_name)
        label = field_info.description or field_name.replace("_", " ").capitalize()
        print(f"  {label}: {value}")


if __name__ == "__main__":
    main()
