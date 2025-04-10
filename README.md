# std-config

> Python library that implements my preferred configuration patterns

This is just a thin shim on top of [xdg-base-dirs](https://github.com/srstevenson/xdg-base-dirs) and [cfg](https://docs.red-dove.com/cfg/python.html).

1. Identify the XDG directories
2. Parse argument values into a config dictionary
3. Load environment values into a config dictionary
4. If a configuration file was specified on the command line, load it. If not, look in 
   the standard locations.

## Command Line Utility

This package also provides a command line utility that loads a configuration and prints it to
stdout as a JSON structure.

To run the command line utility
```bash
stdconfig --config CONFIG_FILE.cfg
```


