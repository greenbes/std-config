from .config import StdConfig


def main():
    config = StdConfig.from_cli()
    
    # Example usage
    print("Configuration loaded:")
    for field_name, field_info in StdConfig.model_fields.items():
        value = getattr(config, field_name)
        label = field_info.description or field_name.replace("_", " ").capitalize()
        print(f"  {label}: {value}")


if __name__ == "__main__":
    main()
