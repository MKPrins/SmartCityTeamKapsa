# Getting Started
Below a short guide on getting everything up and running so you can start developing.

## Contents
 1. [Setup Virtual Environment for Python](#1-setup-virtual-environment-for-python)
 2. [Setup Pipenv](#2-setup-pipenv)

## 1. Setup Virtual Environment for Python
To be able to install packages through pip in the latest python versions you need to create a virtual python enviroment, 'venv' for short.
To create a virtual enviroment you just need a single command.

```bash
python -m venv ~/.local --system-site-packages
```

This will create a venv that's stored in `~/.local`.

_Initially i had created the venv inside the project folder. However this was causing some issues._

To enter the venv you simply call the following command. Once activated you will most likely notice a `(.local)` in your terminal inline with your commands.

```bash
source ~/.local/bin/activate
```

For more info visit the [official python docs](https://docs.python.org/3/library/venv.html).

## 2. Setup Pipenv
Now that the venv has been setup and assuming you have activated it, you can now install Pipenv. Pipenv is used to manage dependencies within a project as to not have conflicting dependencies with other projects. The depencies are managed inside the `Pipfile` and `Pipfile.lock`. These exist in the root folder of this project.

To install Pipenv;
```bash
pip install --user pipenv
```

With pipenv installed, you can now install all of the projects dependencies.
```bash
pipenv install
```

For more info visit the [official pipenv docs](https://pipenv.pypa.io/en/latest/).