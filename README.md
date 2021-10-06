[![GitHub](https://img.shields.io/badge/GitHub-memfault/gdbundle--pycortexmdebug-8da0cb?style=for-the-badge&logo=github)](https://github.com/memfault/gdbundle-PyCortexMDebug)
[![PyPI
version](https://img.shields.io/pypi/v/gdbundle-pycortexmdebug.svg?style=for-the-badge)](https://pypi.org/project/gdbundle-pycortexmdebug/)
[![PyPI
pyversions](https://img.shields.io/pypi/pyversions/gdbundle-pycortexmdebug.svg?style=for-the-badge)](https://pypi.python.org/pypi/gdbundle-pycortexmdebug/)

# gdbundle-PyCortexMDebug

This is a [gdbundle](https://github.com/memfault/gdbundle) plugin for
[bnahill/PyCortexMDebug](https://github.com/bnahill/PyCortexMDebug)

The original `PyCortexMDebug` plugin is embedded as a git submodule, rather than
specifying as a typical dependency, because it is not as of yet deployed to
PyPi, and so this package cannot depend on it via `git+` dependency spec.

## Compatibility

- GDB

## Installation

After setting up [gdbundle](https://github.com/memfault/gdbundle), install the
package from PyPi.

```bash
$ pip install gdbundle-PyCortexMDebug
```

If you've decided to manually manage your packages using the
`gdbundle(include=[])` argument, add it to the list of plugins.

```bash
# .gdbinit

[...]
import gdbundle
plugins = ["PyCortexMDebug"]
gdbundle.init(include=plugins)
```

## Building

Be sure to `git submodule update --init` to get the `cmdebug` dependency.

```bash
$ poetry build
$ poetry publish
```
