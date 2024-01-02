# Python dependencies and package management

![I Stand with Israel](../images/IStandWithIsrael.png)

## Resources

- [Python Enhancement Proposals](https://peps.python.org/)
- [`pip` user guide](https://pip.pypa.io/en/stable/user_guide/)
- ['setuptools quick start](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
- [`pipx`](https://pypa.github.io/pipx/)
- [`pyenv` utility to manage multiple versions of Python](https://github.com/pyenv/pyenv)
- [devpi server](https://github.com/devpi/devpi)

## Install with `pip` from https://pypi.org/

```bash
    
    # manually creates virtual environment
    python -m venv .venv

    # start environment
    source .venv/bin/activate
    # or
    . .venv/bin/activate

    # install latest version
    python -m pip install "package_name"
    
    # install a specific version    
    python -m pip install "package_name==1.2.2"
    
    # version comparison (<,>, >=, <=)
    python -m pip install "package_name < 1.2"
    
    # excluding a version
    python -m pip install "package_name!=1.0.0"

    # combining operators: comma means AND
    python -m pip install "Flask>=1.0.0,!=1.1.0, <=2.0.0"

    # compatible release
    # same major, minor versions equal or greater (ie pip install "requests >=2.24, ==2.*")
    python -m pip install "requests ~=2.24.0"

    # environment makers
    # os_name=='posix' mac os, linux or unix
    # os_name='nt' windows
    # sys_platform='darwin' mac os
    python -m pip install "asyncio; os_name='nt'"

    python -m show
    python -m pip list

    # will not install latest if version already installed
    python -m pip install "package_name"

    # use this command to upgrade to latest
    python -m pip install --upgrade "package_name"
    #or
    python -m pip install -U 

    # fastapi uses pyproject.toml for dependencies management
    # https://github.com/tiangolo/fastapi/blob/78f38c6bfda67b16d1f84ad6981ffb90a2936679/pyproject.toml#L56
    python -m pip install "fastapi[doc, dev]"

```

## Install from Github

https://pip.pypa.io/en/stable/topics/vcs-support/#supported-vcs

```bash
    python -m pip install "{name of the package} @ git+{url}"
```

## Install from local directory

```bash
    # pyproject.toml file is a must
    python -m pip install ~/projects/{project_name}
```

## Install in editable mode from local directory during development

```bash
    pip install -e ~/projects/{project_name}
    # or from the current directory
    python -m install -e .
```

## Global utilities

pip 
```bash
    python3 -V

    which python3
    
    python3 -m pip

    #install
    sudo apt install python3-pip

    # --user switch or if not sudo is used then packages are not globally installed

    # install pipx creates its own user python environment
    sudo apt install pipx
    # check the path
    pipx ensurepath


    # python3 -m pip install requests --index-url http://my-repo.example.com 
    # use configuration https://pip.pypa.io/en/stable/topics/configuration/
```

## Using `requirements.txt` for Applications

https://pip.pypa.io/en/stable/reference/requirements-file-format/

`requirements.txt` file pins the version of the dependencies.

```bash
    python -m venv .venv

    # start environment
    . .venv/bin/activate

    # install SQLAlchemy
    python -m pip install SQLAlchemy

    # show details of the installation 
    python -m pip show  SQLAlchemy

    # create dep file
    pip freeze > requirements.txt

    #restore deps from the file
    pip install -r requirements.txt

    # leave env
    deactivate
```

Use different `requirements.txt` files for `dev` or `prod` or `test`.


## Using `pyproject.toml` file for libraries

Versions of deps are not pinned.

https://github.com/tox-dev/tox
