# Alternatives `pipenv` and `poetry`

![I Stand with Israel](../images/IStandWithIsrael.png)

- Using one tool instead of two for env and deps management
- Deterministic builds
- Security (hashes)

## `pipenv`

- Focused on applications
- All versions are pinned
- `Pipefile`` for top-level deps
- `Pipfile.lock` locks versions with hashes

```bash
     
    python3 -m --user install pipenv
    # or
    pipx install pipenv
    
    # creates virtual environment in /home/{user_name}/.local/share
    pipenv install arrow
```

```bash
    # clone project
    
    # sync deps use -d switch to install dev deps
    pipenv sync -d

    
    # show deps tree
    pipenv graph

    # run
    pipenv run python script.py

    # env
    pipenv shell

    # exit

    # check security issues
    pipenv check
```

## `poetry`

https://python-poetry.org/

- Used for Libraries and Applications
- Custom deps resolver
- Building and distributing packages
- `pyproject.toml` for top-level deps
- `poetry.lock` locks versions with hashes


```bash
    # install poetry to the user bin --sync will update packages
    pipx install poetry --sync

    # create a sample project
    poetry new poetry_demo

    # init myproject.toml file
    poetry init

    # add deps
    poetry add arrow requests

    # git a project and install deps
    poetry install

    # check deps
    poetry show --tree

    # remove dep, removes deps for the package as well
    poetry remove requests
    
    # project is installed in edit mode
    poetry run pip list

    # create install groups 
    poetry add pytest --group test

```

## More options ...

- https://github.com/jazzband/pip-tools
- https://github.com/pdm-project/pdm