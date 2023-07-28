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

### autoinstall

Automatically install dependencies from a python file

```bash
pyhelp autoinstall [OPTIONS] [PYTHON_FILE]
```

### create-env

Create a new virtual environment

```bash
pyhelp create-env [OPTIONS] ENV_NAME
```

### django-template

Create a Django project template

```bash
pyhelp django-template [OPTIONS] PROJECT_NAME
```

### flask-template

Create a Flask project template

```bash
pyhelp flask-template [OPTIONS] PROJECT_NAME
```

### import-libraries

Import library presets into a python file

```bash
pyhelp import-libraries [OPTIONS] [PYTHON_FILE]
```

### install-requirements

Install requirements from a requirements.txt file

```bash
pyhelp install-requirements [OPTIONS] [REQUIREMENTS_FILE]
```

## Contributing

Pull requests are always welcome.

## License

MIT License
