# Linux Ubuntu DevBox Setup

![I stand with Israel](./images/IStandWithIsrael.png)

Ubuntu 22.04 comes with Python `3.10.12`.

## How to Install and Manage Other Versions of Python Interpreters

The default Python interpreter is located at `/usr/bin/python3`.

### Display All Installed Dependencies

To list all installed Python dependencies, use the following command:

```bash
apt list --installed | grep python
```

## Installing Multiple Versions of Python and Switching Between Them

[`pyenv`](https://github.com/pyenv/pyenv) is a utility for managing multiple Python versions, similar to [`nvm`](https://github.com/nvm-sh/nvm) for Node.js.

An alternative method is to use `apt`:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.5
```

## Install [pyenv](https://github.com/pyenv/pyenv)

### Install Dependencies

This script installs the necessary dependencies and clones the `pyenv` repository.

```bash
# Prerequisites
sudo apt install libedit-dev
sudo apt uninstall python3-pip
sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev
sudo apt-get install python-tk python3-tk tk-dev
```

### Install `pyenv`

```bash
curl https://pyenv.run | bash
```

### Update `~/.bashrc` File

Add the following lines to the end of your `~/.bashrc` file to initialize `pyenv`:

```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Build Location
export TMPDIR="$HOME/.pyenv-tmp"

# Load Virtualenv
# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:
eval "$(pyenv virtualenv-init -)"
```

### Install the Latest Version of Python

```bash
pyenv install --list | grep " 3\.[12]"

# Downloads and builds the specified version
pyenv install 3.12.3

# List installed versions
pyenv versions

# Set global Python version
pyenv global 3.12.3
```

![env](images/pyenv-python-version.png)

[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

### Install Aider or Poetry Virtual Environments

Once you have multiple Python versions running, you may need to set up global dependencies for your projects.

#### Aider

[aider](https://github.com/paul-gauthier/aider) is a tool for managing virtual environments.

```bash
# Create an environment
pyenv virtualenv 3.12.3 aider

# Display newly created environment
pyenv versions

# Activate the environment
pyenv activate aider

# Deactivate the environment
pyenv deactivate

# Install aider
pip install aider-chat

# Display the number of installed packages
pip freeze | wc -l
```

#### Poetry

[Poetry](https://python-poetry.org/) is another tool for dependency management and packaging in Python.

```bash
# Create an environment
pyenv virtualenv 3.12.3 poetry

# Display newly created environment
pyenv versions

# Activate the environment
pyenv activate poetry

# Deactivate the environment
pyenv deactivate

# Install Poetry
curl -sSL https://install.python-poetry.org | python -

# Configure Poetry to create virtual environments inside the project directory
poetry config virtualenvs.in-project true

# Create a new Poetry project
poetry new my-project

# Navigate to the project directory
cd my-project

# Add dependencies
poetry add requests

# Activate the virtual environment
poetry shell

# Deactivate the virtual environment
exit
```

## References

- [pyenvs-python-is-missing-bzip2-module](https://stackoverflow.com/questions/60775172/pyenvs-python-is-missing-bzip2-module)
- [How do I install a different Python version using apt-get?](https://askubuntu.com/questions/682869/how-do-i-install-a-different-python-version-using-apt-get)
- [Managing multiple Python versions on Ubuntu/Pop!_OS](https://medium.com/@kameshwarasekar/managing-multiple-python-versions-on-ubuntu-pop-os-eae4d0bf3171)
