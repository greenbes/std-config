# std-config

> Python library that implements my preferred configuration patterns

This is just a thin shim on top of [xdg-base-dirs](https://github.com/srstevenson/xdg-base-dirs), [cfg](https://docs.red-dove.com/cfg/python.html) and [pydantic](https://docs.pydantic.dev/latest/).

1. Evaluate the provided class and identify command line arguments
2. Add command line arguments to `argparse`
3. Use `argparse` to parse command line arguments
1. Identify the XDG directories
2. Parse command line arguments into a dictionary
3. Load environment values into a dictionary
4. If a configuration file was specified on the command line, load it. If not, look in 
   the standard locations.
5. Create a ChainMap of the dictionaries
6. Validate types using Pydantic


## Order of Precedence

Order of precedence for setting a configuration value

Follow this logic in order to determine which value to use:
```
    IF a command line argument is provided THEN
        set value to command line argument
    ELSE IF environment variable is provided THEN
        set value to environment variable
    ELSE IF configuration file is available THEN
        set value from configuration file
    ELSE set value to default
```

## Command Line Utility

This package also provides a command line utility that loads a configuration and prints it to
stdout as a JSON structure.

To run the command line utility
```bash
stdconfig --config CONFIG_FILE.cfg
```


