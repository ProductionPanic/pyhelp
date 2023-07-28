# Pyhelp

## Description

Pyhelp is a Python package that provides a set of functions to help you with your Python projects.

## Installation

```bash
git clone https://github.com/ProductionPanic/pyhelp.git
cd pyhelp
chmod +x install.sh
./install.sh
```

## Usage

```bash
Usage: pyhelp [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  activate-env          Activate a virtual environment
  autoinstall           Automatically install dependencies from a python...
  create-env            Create a new virtual environment
  django-template       Create a Django project template
  flask-template        Create a Flask project template
  import-libraries      Import library presets into a python file
  install-requirements  Install requirements from a requirements.txt file

```

## Commands

### activate-env

Activate a virtual environment

```bash
pyhelp activate-env [OPTIONS] ENV_NAME
```

- ENV_NAME: The name of the virtual environment to activate.

### autoinstall

Automatically install dependencies from a python file

```bash
pyhelp autoinstall [OPTIONS] [PYTHON_FILE]
```

- PYTHON_FILE: The python file to read from. If not specified, the current directory will be searched for a file named "main.py".

### create-env

Create a new virtual environment

```bash
pyhelp create-env [OPTIONS] ENV_NAME
```

- ENV_NAME: The name of the virtual environment to create.

### django-template

Create a Django project template

```bash
pyhelp django-template [OPTIONS] PROJECT_NAME
```

- PROJECT_NAME: The name of the Django project to create.

### flask-template

Create a Flask project template

```bash
pyhelp flask-template [OPTIONS] PROJECT_NAME
```

- PROJECT_NAME: The name of the Flask project to create.

### import-libraries

Import library presets into a python file

```bash
pyhelp import-libraries [OPTIONS] [PYTHON_FILE]
```

- PYTHON_FILE: The python file to read from. If not specified, the current directory will be searched for a file named "main.py".

### install-requirements

Install requirements from a requirements.txt file

```bash
pyhelp install-requirements [OPTIONS] [REQUIREMENTS_FILE]
```

- REQUIREMENTS_FILE: The requirements.txt file to read from. If not specified, the current directory will be searched for a file named "requirements.txt".

## Contributing

Pull requests are always welcome.

## License

MIT License
