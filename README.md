# gdbundle-PyCortexMDebug

This is a [gdbundle](https://github.com/memfault/gdbundle) plugin for [bnahill/PyCortexMDebug](https://github.com/bnahill/PyCortexMDebug)

## Compatibility

- GDB

## Installation

After setting up [gdbundle](https://github.com/memfault/gdbundle), install the package from PyPi. 

```
$ pip install gdbundle-PyCortexMDebug
```

If you've decided to manually manage your packages using the `gdbundle(include=[])` argument,
add it to the list of plugins.

```
# .gdbinit

[...]
import gdbundle
plugins = ["PyCortexMDebug"]
gdbundle.init(include=plugins)
```

## Building

```
$ poetry build
$ poetry publish
```
