# std-config

> This module accepts a Pydantic CLASS definition that represents desired application configuration values and returns a filled object INSTANCE based on command line options, environment variables, and a configuration file. Pydantic provides data validation.

This is just a thin shim on top of [xdg-base-dirs](https://github.com/srstevenson/xdg-base-dirs) and [pydantic](https://docs.pydantic.dev/latest/).

## Order of Precedence

Follow this logic when filling the object INSTANCE:

```
    IDENTIFY xdg values from environment
    CREATE an INSTANCE of the provided CLASS
    ITERATE OVER fields in provided class and identify command line arguments
    ADD command line arguments to argparse
    CHECK command line arguments for a configuration file but do not apply other values
    IF configuration file is available THEN
        read configuration file
        set INSTANCE values using values from configuration file
    IF a command line argument is provided THEN
        set value to command line argument
    ELSE IF environment variable is provided THEN
        set value to environment variable
```

## Detailed Steps to Implement the Order of Precedence

1. Identify the XDG base directories to use as default prefixes
2. Create an INSTANCE of the provided CLASS
    - Default values handled by Pydantic definitions
3. Iterate over the attributes in the provided class and identify command line arguments
    - Each `Field` definition can have an optional `arg_short` parameter or an optional `arg_long` parameter 
4. Add command line arguments to `argparse` definition 
5. Use `argparse` to parse command line arguments
6. If a configuration file was specified on the command line, load it. If not, look for a configuration file in the locations specified by the INSTANCE.
    - Override defaults
7. Identify ENVIRONMENT VARIABLES and set INSTANCE attributes 
8. Parse COMMAND LINE ARGUMENTS and set the related INSTANCE attributes

## Notes

- Values not specified in the CLASS attributes are ignored

## Command Line Utility

This package also provides a command line utility that loads a configuration and prints it to
stdout as a JSON structure.

To run the command line utility
```bash
stdconfig --config CONFIG_FILE.cfg
```


