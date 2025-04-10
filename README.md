# std-config

> Python library that implements my preferred configuration patterns

This is just a thin shim on top of [xdg-base-dirs](https://github.com/srstevenson/xdg-base-dirs) and [cfg](https://docs.red-dove.com/cfg/python.html).

1. Identify the XDG directories
2. Parse command line arguments into a dictionary
3. Load environment values into a dictionary
4. If a configuration file was specified on the command line, load it. If not, look in 
   the standard locations.
5. Create a ChainMap of the dictionaries
5. Validate values using Pydantic

## Command Line Utility

This package also provides a command line utility that loads a configuration and prints it to
stdout as a JSON structure.

To run the command line utility
```bash
stdconfig --config CONFIG_FILE.cfg
```


