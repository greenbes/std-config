from .config import StdConfig


def main():
    config = StdConfig.from_cli()
    
    # Example usage
    print("Configuration loaded:")
    config.print_fields()


if __name__ == "__main__":
    main()
