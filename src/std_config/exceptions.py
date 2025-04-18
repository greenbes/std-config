class StdConfigError(Exception):
    """Base class for exceptions in the std-config library."""
    pass


class ConfigDirectoryError(StdConfigError):
    """Raised when there's an error creating the configuration directory."""
    def __init__(self, directory_path, original_exception):
        self.directory_path = directory_path
        self.original_exception = original_exception
        message = f"Failed to create configuration directory '{directory_path}': {original_exception}"
        super().__init__(message)


class ConfigFileError(StdConfigError):
    """Base class for configuration file related errors."""
    def __init__(self, file_path, message):
        self.file_path = file_path
        self.message = message
        super().__init__(f"Error related to config file '{file_path}': {message}")


class ConfigFileNotFoundError(ConfigFileError):
    """Raised when a specified configuration file is not found."""
    def __init__(self, file_path):
        super().__init__(file_path, "File not found.")


class ConfigFileParseError(ConfigFileError):
    """Raised when a configuration file cannot be parsed."""
    def __init__(self, file_path, original_exception):
        self.original_exception = original_exception
        super().__init__(file_path, f"Failed to parse file: {original_exception}")
