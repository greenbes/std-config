from typing import Type, Any, List, Union, Optional, get_origin, get_args, get_type_hints
import inspect
from pathlib import Path
import json
from pydantic_settings import BaseSettings


class SchemaField:
    """Represents a field in a configuration schema for documentation purposes."""

    def __init__(
        self,
        name: str,
        type_name: str,
        description: str,
        default: Any,
        required: bool,
        choices: Optional[List[str]] = None,
        env_var: Optional[str] = None,
        cli_args: Optional[List[str]] = None,
    ):
        self.name = name
        self.type_name = type_name
        self.description = description
        self.default = default
        self.required = required
        self.choices = choices
        self.env_var = env_var
        self.cli_args = cli_args or []


class SchemaDocGenerator:
    """
    Generates documentation for configuration schema.
    
    This class provides methods to generate documentation for Pydantic-based
    configuration classes in various formats like Markdown, JSON, etc.
    """

    @staticmethod
    def _get_type_display_name(type_hint: Any) -> str:
        """Get a human-readable name for a type hint."""
        if type_hint is None:
            return "None"
        
        origin = get_origin(type_hint)
        args = get_args(type_hint)

        if origin is Union:
            # Handle Optional[X] which is Union[X, NoneType]
            if len(args) == 2 and type(None) in args:
                non_none_arg = args[0] if args[1] is type(None) else args[1]
                return f"Optional[{cls._get_type_display_name(non_none_arg)}]"
            # General Union
            union_args = ", ".join(cls._get_type_display_name(arg) for arg in args)
            return f"Union[{union_args}]"
        elif origin in (list, List):
            if not args: return "List"
            return f"List[{cls._get_type_display_name(args[0])}]"
        elif origin in (dict, Dict):
            if not args or len(args) != 2: return "Dict"
            key_type = cls._get_type_display_name(args[0])
            value_type = cls._get_type_display_name(args[1])
            return f"Dict[{key_type}, {value_type}]"
        elif hasattr(type_hint, "__name__"):
            return type_hint.__name__
        elif origin is not None:
            # Handle other generics like Tuple, Set etc.
            origin_name = getattr(origin, "__name__", str(origin))
            arg_names = ", ".join(cls._get_type_display_name(arg) for arg in args)
            return f"{origin_name}[{arg_names}]"
        else:
            # Fallback for simple types or unknown complex types
            return str(type_hint).replace("typing.", "")
    
    @staticmethod
    def _get_field_info(
        model_class: Type[BaseSettings], field_name: str, field_info: Any
    ) -> SchemaField:
        """Extract information about a field for documentation."""
        # Get type information
        type_hints = get_type_hints(model_class)
        field_type = type_hints.get(field_name, Any)
        type_name = SchemaDocGenerator._get_type_display_name(field_type)
        
        # Check if it's an enum
        choices = None
        if hasattr(field_type, "__members__"):
            choices = [value.value for value in field_type.__members__.values()]
        
        # Get description and default
        description = field_info.description or field_name.replace("_", " ").capitalize()
        default = field_info.default
        if inspect.isfunction(default) and default.__name__ == "<lambda>":
            default = "Dynamic default value"
        
        # Get environment variable and CLI args
        extras = field_info.json_schema_extra or {}
        env_var = extras.get("env")
        cli_args = []
        if extras.get("arg_short"):
            cli_args.append(extras["arg_short"])
        if extras.get("arg_long"):
            cli_args.append(extras["arg_long"])
        
        # Required field
        required = field_info.is_required()
        
        return SchemaField(
            name=field_name,
            type_name=type_name,
            description=description,
            default=default,
            required=required,
            choices=choices,
            env_var=env_var,
            cli_args=cli_args,
        )
    
    @classmethod
    def get_schema_fields(cls, model_class: Type[BaseSettings]) -> List[SchemaField]:
        """Get schema documentation fields from a Pydantic model class."""
        fields = []
        
        for field_name, field_info in model_class.model_fields.items():
            field = cls._get_field_info(model_class, field_name, field_info)
            fields.append(field)
            
        return fields
    
    @classmethod
    def to_markdown(cls, model_class: Type[BaseSettings]) -> str:
        """Generate Markdown documentation for a Pydantic model class."""
        fields = cls.get_schema_fields(model_class)
        
        # Get class docstring
        class_description = model_class.__doc__ or ""
        class_description = inspect.cleandoc(class_description)
        
        # Format as markdown
        lines = [
            f"# {model_class.__name__} Configuration",
            "",
            class_description,
            "",
            "## Configuration Fields",
            "",
            "| Field | Type | Description | Default | Required | Env Variable | CLI Arguments |",
            "| ----- | ---- | ----------- | ------- | -------- | ------------ | ------------ |",
        ]
        
        for field in fields:
            default_value = str(field.default) if field.default is not None else "None"
            required = "Yes" if field.required else "No"
            env_var = f"`{field.env_var}`" if field.env_var else "-"
            cli_args = ", ".join(f"`{arg}`" for arg in field.cli_args) if field.cli_args else "-"
            
            description = field.description
            # Add enum choices to description if applicable
            if field.choices:
                choices_str = ", ".join(f"`{choice}`" for choice in field.choices)
                description += f"<br/>Choices: {choices_str}"

            lines.append(
                f"| `{field.name}` | {field.type_name} | {description} | `{default_value}` | {required} | {env_var} | {cli_args} |"
            )

        return "\n".join(lines)
    
    @classmethod
    def to_json(cls, model_class: Type[BaseSettings]) -> str:
        """Generate JSON schema documentation for a Pydantic model class."""
        fields = cls.get_schema_fields(model_class)
        
        schema = {
            "name": model_class.__name__,
            "description": inspect.cleandoc(model_class.__doc__ or ""),
            "fields": [
                {
                    "name": field.name,
                    "type": field.type_name,
                    "description": field.description,
                    "default": field.default if not callable(field.default) else str(field.default),
                    "required": field.required,
                    "choices": field.choices,
                    "env_var": field.env_var,
                    "cli_args": field.cli_args,
                }
                for field in fields
            ],
        }
        
        return json.dumps(schema, indent=2, default=str)
    
    @classmethod
    def save_markdown(cls, model_class: Type[BaseSettings], output_path: Path) -> None:
        """Save Markdown documentation to a file."""
        markdown = cls.to_markdown(model_class)
        with open(output_path, "w") as f:
            f.write(markdown)
    
    @classmethod
    def save_json(cls, model_class: Type[BaseSettings], output_path: Path) -> None:
        """Save JSON schema documentation to a file."""
        json_schema = cls.to_json(model_class)
        with open(output_path, "w") as f:
            f.write(json_schema)
