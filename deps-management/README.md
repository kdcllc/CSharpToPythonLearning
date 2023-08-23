# Python dependencies and package management

- [`pip` dependencies and package management](./pip-dependecies.md)
- [`pip` alternatives](./pip-alternatives.md)


## Packages vs. Modules

Use `__path__` is a list

- Packages are generally directories `Package -> module.py`
- Modules are generally files `module.py`

* `sys.path` searches thru list of directories in order of the `import` statements 1st math provides module, if not `ImportError` is raised.

*`PYTHONPATH` allows to add other directories for `import` search.

### Creating a package

1. Create a folder and create a `__init__.py` file.

```python
    python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2
```

2. `__all__` module level attribute that controls how `import *` behavior if not specified, import all public names.

## Executing directories or packages

- add {directory_name} to `sys.path`
- add {directory_name}__main__.py is not in a package

Then you can run it as follows

```python
    python {directory_name}
```

- `-m` instructs python to treat it as a module
- {directory_name} is treated as  a module
- {directory_name}__main__.py  is a submodule of the directory package

```python
    python -m {directory_name}
```

## Build and Distribution

- `python setup.py sdist` - build in functionality and allows for source distribution
- install wheel first `pip install wheel` then `python setup.py bdist_wheel`

```python
    python3 -m pip install --upgrade pip
```
