# Python Practices to Learn the Language

This repository contains a collection of Python practices designed to help you learn and master the Python programming language. Follow the instructions below to set up your environment and start working through the exercises.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:
- Python 3.x
- pip (Python package installer)
- Jupyter Notebook
- .NET SDK (for C# support)

## Recommended VS Code Extensions

To enhance your development experience, consider installing the following Visual Studio Code extensions:
- [Jupyter Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter): Provides Jupyter notebook support in VS Code.
- [VS Code Insiders and .NET Polyglot Notebooks](https://devblogs.microsoft.com/dotnet/net-interactive-preview-3-vs-code-insiders-and-polyglot-notebooks/): Enables .NET interactive notebooks in VS Code.

## Setup the Workbook

Follow these steps to set up your environment:

1. **Create a virtual environment**:
    ```bash
    python3 -m venv .venv
    ```

2. **Activate the virtual environment**:
    - On Linux/macOS:
        ```bash
        source .venv/bin/activate
        ```
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```

3. **Verify the virtual environment**:
    ```bash
    python -m site
    python -m pip list
    ```

4. **Install Jupyter Notebook support**:
    ```bash
    python -m pip install jupyter
    ```
    Or install from the requirements file:
    ```bash
    python -m pip install -r requirements.txt
    ```

5. **Check the Jupyter kernel**:
    ```bash
    jupyter kernelspec list
    ```

6. **Install .NET interactive for Jupyter (if needed)**:
    ```bash
    dotnet tool install -g dotnet-try
    export DOTNET_ROLL_FORWARD=LatestMajor
    export DOTNET_TRY_CLI_TELEMETRY_OPTOUT=1
    dotnet try jupyter install
    ```

7. **Save dependencies if changed**:
    ```bash
    python3 -m pip freeze > requirements.txt
    ```

8. **Select the newly created virtual environment for the `python-workbook.ipynb` notebook**.

## Install Multiple Python Versions

If you need to install multiple versions of Python, follow these steps:

1. **Add the deadsnakes PPA**:
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa --yes
    ```

2. **Update and upgrade your system**:
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

3. **Install Python 3.11**:
    ```bash
    sudo apt install python3.11 -y
    ```

4. **Verify the installation**:
    ```bash
    python3.11 --version
    python3.11 -m pip list
    ```

## References

- [Python for C# Developers by David Betteridge](https://youtu.be/LGMo1aJYYaE) and [code PythonTalks](https://github.com/DavidBetteridge/PythonTalks)
- [How to Install and Switch Python Versions on Ubuntu 22.04](https://www.eukhost.com/kb/how-to-install-and-switch-python-versions-on-ubuntu-22-04/)
