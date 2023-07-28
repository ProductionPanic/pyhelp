#!/usr/bin/env python3
import sys
import os
import subprocess
import click
import re
import pkgutil
from cookiecutter.main import cookiecutter


@click.group()
def cli():
    pass


@cli.command('create-env')
@click.argument('env_name')
def create_env(env_name):
    """Create a new virtual environment"""
    subprocess.run(['python3', '-m', 'venv', env_name])


@cli.command('activate-env')
@click.argument('env_name')
def activate_env(env_name):
    """Activate a virtual environment"""
    if sys.platform == 'win32':
        bin_path = os.path.join(env_name, 'Scripts')
        bin_path = os.path.join(bin_path, 'activate.bat')
    else:
        bin_path = os.path.join(env_name, 'bin')
        bin_path = os.path.join(bin_path, 'activate')
    subprocess.run([bin_path])

@cli.command('autoinstall', help="Automatically install dependencies from a python file")
@click.argument('python_file', type=click.Path(exists=True), default='main.py')
def autoinstall(python_file):
    # read file
    with open(python_file, 'r') as f:
        lines = f.readlines()

    print('Found file')
    # find import statements
    imports = []
    for line in lines:
        if line.startswith('import') or line.startswith('from'):
            imports.append(line)
    print(f'Found {len(imports)} imports')
    # parse imports
    dependencies = []
    ss = re.compile(r'from\s+(\w+)\s+import\s+(\w+)')
    for imp in imports:
        m = ss.search(imp)
        if m:
            dependencies.append(m.group(1))
        else:
            dependencies.append(imp.split(' ')[1])
    # if a dependency includes a dot only take the first part
    dependencies = [dep.split('.')[0] for dep in dependencies]
    loaded = [x.name for x in list(pkgutil.iter_modules())]
    print(f'Found {len(dependencies)} dependencies')
    # install dependencies
    for dep in dependencies:
        print(f'Installing {dep}')
        # check if folder exists
        if os.path.exists(dep) or dep in loaded:
            print(f'{dep} already installed')
            continue        
        get_pgk_cmd = ['python3', '-m', 'pip', 'show', dep, '|', 'grep', 'Name', '|', 'awk', "'{print $2}'"]
        #get package name
        try:
            package_name = subprocess.run(get_pgk_cmd, shell=True, capture_output=True, timeout=5)
        except subprocess.TimeoutExpired:
            print('Timeout while finding package name')
            print('Using default package name')
            package_name = dep
            
        # if has stdout decode it
        if not type(package_name) == str:
            package_name = package_name.stdout.decode('utf-8').strip()
            
        if package_name and not 'WARNING' in package_name and package_name != '':
            print(f'Found package name {package_name}')
        else:
            print(dep + ' not found')
            continue
        print('running pip install')
        try:
            subprocess.run(['python3', '-m', 'pip', 'install', package_name])
            
            print(f'Installed {package_name}')
        except:
            print(f'Could not install {package_name}. try installing manually')
            continue
    


@cli.command('install-requirements')
@click.argument('requirements_file', default='requirements.txt')
def install_requirements(requirements_file):
    """Install requirements from a requirements.txt file"""
    subprocess.run(['pip3', 'install', '-r', requirements_file])

@cli.command('flask-template')
@click.argument('project_name')
def flask_template(project_name):
    """Create a Flask project template"""
    cookiecutter('https://github.com/cookiecutter-flask/cookiecutter-flask.git')


@cli.command('django-template')
@click.argument('project_name')
def django_template(project_name):
    """Create a Django project template"""
    cookiecutter('https://github.com/cookiecutter/cookiecutter-django.git')


@cli.command('import-libraries', help="Import library presets into a python file")
@click.argument('file_name')
@click.argument('category', required=False)
def import_libraries(file_name, category):
    if not category:        
        category = click.prompt('category', type=click.Choice(['data', 'web', 'gui', 'system', 'science', 'game', 'cli']))
    importmap={
        'data': 'pandas,re,os,sys,urllib,requests,sqlite3,json,csv',
        'web': 'flask,flask_CORS,json',
        'gui': 'tkinter,tkinter.messagebox,tkinter.filedialog',
        'system': 'subprocess,sys,os,shutil',
        'science': 'numpy,scipy,matplotlib',
        'game': 'pygame',
        'cli': 'click,rich,pyfiglet,termcolor,pyperclip',
    }
    # check if file exists
    if not os.path.exists(file_name):
        print(f'File {file_name} does not exist')
        # prompt to create file
        create_file = input('Do you want to create the file? [y/n]: ')
        if create_file.lower() == 'y':
            with open(file_name, 'w') as f:
                f.write('')
        else:
            sys.exit(1)

    # read file
    with open(file_name, 'r') as f:
        content = f.read()
    
    #split content into lines
    lines = content.split('\n')

    start_at = 0
    # check if file starts with a shebang if so start from the next line
    if lines[0].startswith('#!'):
        start_at = 1

    # find map for category
    libs = importmap[category].split(',')
    # add imports to file
    for lib in libs:
        if lib not in content:
            lines.insert(start_at, f'import {lib}')
            start_at += 1

    # write back to file
    with open(file_name, 'w') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    # if no arguments are passed print help
    if len(sys.argv) == 1:
        cli(['--help'])
    else:
        cli()
