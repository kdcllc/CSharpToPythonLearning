# Python Practices to learn Language

- [Jupyter Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [VS Code Insiders and .NET Polyglot Notebooks](https://devblogs.microsoft.com/dotnet/net-interactive-preview-3-vs-code-insiders-and-polyglot-notebooks/)

## Setup the workbook

1. Run the following commands in the `practices` folder:

```bash
    
    # 1. create virtual environment on linux box
    python3 -m venv .venv

    # 2. activates the current virtual environment
    . .venv/bin/activate

    # 3. check the locations
    python -m show
    python -m pip list

    # 4. install jupyter notebook support
    python -m pip install jupyter
    # or
    python -m pip install -r requirements.txt

    # 5. check kernel
    jupyter kernelspec list

    # 6. C# assumes that dotnet is installed on the machine
    # this is should be run once.
    dotnet tool install -g dotnet-try
    export DOTNET_ROLL_FORWARD=LatestMajor
    export DOTNET_TRY_CLI_TELEMETRY_OPTOUT=1
    dotnet try jupyter install

    # save deps if changed
    python3 -m pip freeze > requirements.txt
```

2. Select newly created virtual environment for the `python-workbook.ipynb` notebook.