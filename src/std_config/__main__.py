from .ai_config import AIConfig


def main():
    config = AIConfig.from_cli()

    # Example usage
    print("Configuration loaded:")
    config.print_fields()


if __name__ == "__main__":
    main()
