# {{ cookiecutter.project_name }}

A sample project written in Python intended for use when learning the following tools:

* [setuptools](https://pypi.org/project/setuptools/) / [twine](https://pypi.org/project/twine/)
* [PyInstaller](https://pypi.org/project/PyInstaller/)
* [pyminifier](https://pypi.org/project/pyminifier/)
* [PEX](https://pypi.org/project/pex/)

## Usage

### Virtual Environment

First you need to create and activate a virtual environment, e.g. with [virtualenv](https://pypi.org/project/virtualenv/) or [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/).

```shell
$ mkvirtualenv {{ cookiecutter.project_name }}
```

### setuptools

Once virtual environment is activated and current working directory contains `setup.py` it is time to install the Python package:

```
({{ cookiecutter.project_name }}) $ pip install .
```

Optionally you may want to run the unit tests:

```
({{ cookiecutter.project_name }}) $ python setup.py test
```

To verify if the installation went correctly try to run the bundled script. It should be already available on the `$PATH` so even if you change directory (without deactivating virtual environment) it should work as expected.

```shell
({{ cookiecutter.project_name }}) $ {{ cookiecutter.project_name }}_script.py
hello world
```

Then you need to build source and binary distributions that will be uploaded to [PyPI](https://pypi.org/):

```shell
({{ cookiecutter.project_name }}) $ python setup.py sdist bdist_wheel
```

### twine

While setuptools allows for upload it is recommended to use `twine` instead since it takes advantage of SSL by default.

Also publishing a certain version directly to PyPI may not be desirable because it cannot be undone. Thus, it is advisable to test the upload against [Test PyPI](https://test.pypi.org/) first.

```shell
({{ cookiecutter.project_name }}) $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Only then:

```shell
({{ cookiecutter.project_name }}) $ twine upload dist/*
```

Note you will need to register separate accounts on both Test PyPI and PyPI, though.

### PyInstaller

To create a platform-specific native executable:

```shell
({{ cookiecutter.project_name }}) $ pyinstaller --onefile --additional-hooks-dir src/{{ cookiecutter.project_name }} bin/{{ cookiecutter.project_name }}_script.py
```

This will generate an executable file in dist/ subfolder.

### pyminifier

If your goal is to minify or obfuscate the code, then check out pyminifier.

* minify
```shell
({{ cookiecutter.project_name }}) $ pyminifier bin/{{ cookiecutter.project_name }}_script.py > bin/{{ cookiecutter.project_name }}_script_minified.py
```
* minify and compress
```shell
({{ cookiecutter.project_name }}) $ pyminifier --gzip bin/{{ cookiecutter.project_name }}_script.py > bin/{{ cookiecutter.project_name }}_script_compressed.py
```
* obfuscate
```shell
({{ cookiecutter.project_name }}) $ pyminifier --obfuscate bin/{{ cookiecutter.project_name }}_script.py > bin/{{ cookiecutter.project_name }}_script_obfuscated.py
```
* obfuscate with non-Latin substitution (and optional length specification)
```shell
({{ cookiecutter.project_name }}) $ pyminifier --nonlatin [--replacement-length=50] bin/{{ cookiecutter.project_name }}_script.py > bin/{{ cookiecutter.project_name }}_script_nonlatin.py
```

### PEX

PEX stands for **P**ython **EX**ecutable. It is a ZIP archive with `__main__.py` in it so that it can be executed as a regular script or a Python module.

Unfortunately running PEX files requires the right version of Python interpreter to be installed on the host machine. One can imagine PEX files as single-file portable virtual environments with dependencies and binary libraries (such as `lxml`) already installed. These files can be then easily deployed to remote hosts.

Commands:

```shell
({{ cookiecutter.project_name }}) $ python setup.py bdist_wheel
({{ cookiecutter.project_name }}) $ pex {{ cookiecutter.project_name }} -r requirements.txt -f dist -c {{ cookiecutter.project_name }}_script.py -o {{ cookiecutter.project_name }}.pex
```

There is a Dockerfile for convenience. To build a new Docker image:

```shell
$ docker build -t {{ cookiecutter.project_name }} -f Dockerfile .
```

Then run a temporary Docker container to extract PEX file from:

```shell
$ docker run --rm {{ cookiecutter.project_name }} cat /root/{{ cookiecutter.project_name }}.pex > {{ cookiecutter.project_name }}.pex
```
