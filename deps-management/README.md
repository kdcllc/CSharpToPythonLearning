# Python Dependencies and Package Management

![I Stand with Israel](./images/IStandWithIsrael.png)

## Introduction

As a C# developer, you might be familiar with NuGet for managing dependencies in your projects. Python has similar tools and practices for dependency management, but with some differences. This document will guide you through Python's dependency management tools and practices, comparing them to what you might already know from C# development.

## Packages vs. Modules

In Python, packages and modules are used to organize code. A package is a directory containing a special `__init__.py` file, while a module is a single Python file. This is somewhat similar to namespaces and assemblies in C#.

- **Packages**: Generally directories containing multiple modules.
- **Modules**: Single Python files.

Python uses `sys.path` to search for modules and packages. You can also use the `PYTHONPATH` environment variable to add additional directories to the search path.

### Creating a Package

1. Create a folder and add an `__init__.py` file.
2. Use the package in your code.

Example:
```python
python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2
```

## Executing Directories or Packages

You can execute a directory or package by adding it to `sys.path` and ensuring it contains a `__main__.py` file.

Example:
```python
python {directory_name}
```

Using the `-m` switch:
```python
python -m {directory_name}
```

## Build and Distribution

Python uses `setup.py` for building and distributing packages, similar to `.csproj` files in C#.

Example:
```bash
python setup.py sdist
pip install wheel
python setup.py bdist_wheel
```

## `pip` Dependencies and Package Management

`pip` is the package installer for Python, similar to NuGet in C#. It allows you to install and manage packages from the Python Package Index (PyPI).

### Resources

- [Python Enhancement Proposals](https://peps.python.org/)
- [`pip` user guide](https://pip.pypa.io/en/stable/user_guide/)
- [setuptools quick start](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
- [`pipx`](https://pypa.github.io/pipx/)
- [`pyenv` utility to manage multiple versions of Python](https://github.com/pyenv/pyenv)
- [devpi server](https://github.com/devpi/devpi)

### Install with `pip` from PyPI

```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment
source .venv/bin/activate
# or
. .venv/bin/activate

# Install the latest version of a package
python -m pip install "package_name"

# Install a specific version
python -m pip install "package_name==1.2.2"

# Version comparison
python -m pip install "package_name < 1.2"

# Exclude a version
python -m pip install "package_name!=1.0.0"

# Combine operators
python -m pip install "Flask>=1.0.0,!=1.1.0,<=2.0.0"

# Compatible release
python -m pip install "requests ~=2.24.0"

# Environment markers
python -m pip install "asyncio; os_name='nt'"

# Show installed packages
python -m pip list

# Upgrade to the latest version
python -m pip install --upgrade "package_name"
```

### Install from GitHub

```bash
python -m pip install "{name of the package} @ git+{url}"
```

### Install from Local Directory

```bash
# pyproject.toml file is required
python -m pip install ~/projects/{project_name}
```

### Install in Editable Mode

```bash
pip install -e ~/projects/{project_name}
# or from the current directory
python -m pip install -e .
```

### Global Utilities

```bash
python3 -V
which python3
python3 -m pip

# Install pip
sudo apt install python3-pip

# Install pipx
sudo apt install pipx
pipx ensurepath
```

### Using `requirements.txt`

`requirements.txt` is similar to `packages.config` in C#. It lists the dependencies for your project.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install SQLAlchemy
pip freeze > requirements.txt
pip install -r requirements.txt
deactivate
```

## Alternatives: `pipenv` and `poetry`

### `pipenv`

`pipenv` is focused on applications and uses `Pipfile` and `Pipfile.lock` for dependency management.

```bash
pipx install pipenv
pipenv install arrow
pipenv sync -d
pipenv graph
pipenv run python script.py
pipenv shell
pipenv check
```

### `poetry`

`poetry` is used for both libraries and applications. It uses `pyproject.toml` and `poetry.lock`.

```bash
pipx install poetry --sync
poetry new poetry_demo
poetry init
poetry add arrow requests
poetry install
poetry show --tree
poetry remove requests
poetry add pytest --group test
```

## More Options

- [pip-tools](https://github.com/jazzband/pip-tools)
- [pdm](https://github.com/pdm-project/pdm)
