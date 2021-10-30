# Python Example Project Structure

Example of statuses that can be in readme:

[![Go Report Card](https://goreportcard.com/badge/github.com/prometheus/prometheus)](https://goreportcard.com/report/github.com/prometheus/prometheus)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/486/badge)](https://bestpractices.coreinfrastructure.org/projects/486)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/prometheus/prometheus)
[![Fuzzing Status](https://oss-fuzz-build-logs.storage.googleapis.com/badges/prometheus.svg)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:prometheus)

Visit [my docs](https://google.com) for the full documentation,
examples and guides.

With this project you get:

- a minimal `setup.py` file
- testing with PyTest
- documentation (HTML and PDF) generated using Sphinx
- a CLI entry point

## Project Structure

```bash
example_project/
 |-- docs/
 |-- |-- build/
 |-- |-- source/
 |-- example_project/
 |-- |-- __init__.py
 |-- |-- __version__.py
 |-- |-- example_module.py
 |-- tests/
 |-- |-- test_data/
 |-- |   |-- example_class_data.json
 |-- |   __init__.py
 |-- |   conftest.py
 |-- |   test_example_class.py
 |-- .env
 |-- .gitignore
 |-- Pipfile
 |-- Pipfile.lock
 |-- README.md
 |-- setup.py
```

### Example Project

- `example_module.py`
- `cli.py`

The `example_module.py` module contains sample code. `tests` folder contains tests using PyTest.

The `cli.py` module is referenced in the `setup.py` file via the `entry_points` definitions:

```python
entry_points={
    'console_scripts': ['py-package-template=example_project.cli:main'],
}
```


### Project Dependencies

Using [pipenv](https://docs.pipenv.org). Use --dev flag for pkgs only needed for dev or test.
This gives a deterministic build. Note pipenv is a reference implementation recommened by Python.
I fully expect pip to eventually implement it internally.

#### Installing Pipenv

Assuming you have python installed (duh). On Mac (I exclusively code on mac now)
I use brew to manage stuff as mac comes with python 2.x but the world has moved on and you
MUST use 3.x, latest version at time of writing is 3.10.

Anyway Install pipenv

```bash
pip3 install pipenv
```

# Initialise Your Pipenv shell!

```bash
pipenv shell
```
do this from the source folder where Pipfile is present i.e. root folder.

this will also create your virtual env if its not there, i suggest reading up
a bit on pipenv (just a quick brush) so you know the fundamentals as its quite
different to virtualenv

#### Installing this Projects' Dependencies

Make sure that you're in the project's root directory 

```bash
pipenv install --dev
```

#### Running Python and IPython from the Project's Virtual Environment

I find using IPython in command line really useful when I am not in PyCharm IDE.
I have included ipython as part of the --dev install above so you should be able to get into it
by just doing 

```bash
❯ ipython
Python 3.10.0 (default, Oct 13 2021, 06:45:00) [Clang 13.0.0 (clang-1300.0.29.3)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.28.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```

#### Automatic Loading of Environment Variables

Pipenv will automatically pickup any environment variables 
declared in the `.env` file, located in root directory. 
For example, adding,

```bash
DILLY=VANILLY
```

Will enable access to this variable from python
```python
os.environ['DILLY']
```

### Running Unit Tests

All test have been written using the [PyTest](https://docs.pytest.org/en/latest/) package. 
Tests are kept in the `tests` folder and can be run from the command line

```bash
cd tests
pytest
```
The `conftest.py` module is used by PyTest - I've used it to add fixtures
which is really cool feature of pytest, I recommend.

### Linting Code

I used [flake8](http://flake8.pycqa.org/en/latest/) for linting code.

```bash
pipenv run flake8 example_project
```

And [black](https://black.readthedocs.io/en/stable/) for formatting.
```bash
 pipenv run black example_project
```

And you can use [pre-commit](https://pre-commit.com/) to hook it all up (incl docs)
so you never have to actually do anything manually by hand. 

### Static Type Checking

I think this is very useful. Think of all the times we said ah it might break some import
or something but we wont know until we run, sure we can do extensive tests (we should) but
this is like being able to do a compile of python and find problems. 

it will barf about pandas/numpy etc which doesnt have stubs, so ignore it for now.
am using  [MyPy package](http://mypy-lang.org). You can configure what it does with
mypy.ini options should be in their docs.

Also note [Data Science Types](https://pypi.org/project/data-science-types/) is trying to
fix above problem - but I have not tried it.

To run mypy do >

```bash
pipenv run python -m mypy example_project/*.py
```

MyPy options for this project can be defined in the `mypy.ini` file that MyPy will look for by default. For more information on the full set of options, see the [mypy documentation](https://mypy.readthedocs.io/en/stable/config_file.html).

Examples of type annotation and type checking for library development can be found in the `py_pkg.curves.py` module. This should also be cross-referenced with the improvement to readability (and usability) that this has on package documentation.

### some terminal output from running above stuff

```bash

❯ pipenv run python -m mypy example_project/*.py
Loading .env environment variables...
example_project/example_module.py:12: error: Skipping analyzing "pandas": found module but no type hints or library stubs
example_project/example_module.py:12: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports


❯ pipenv run flake8 example_project
Loading .env environment variables...
example_project/__version__.py:11:13: W292 no newline at end of file
example_project/cli.py:14:10: E211 whitespace before '('
example_project/cli.py:14:20: W292 no newline at end of file

❯ pipenv run black example_project
Loading .env environment variables...
reformatted example_project/__version__.py
reformatted example_project/cli.py
reformatted example_project/example_module.py
```

### Documentation

The documentation in the `docs` folder has been built using [Sphinx](http://www.sphinx-doc.org). 
Its a powerful framework that can be used to generate docs on the fly into various formats.

I generated the initial source using:

```bash
sphinx-quickstart docs
```
And then you'd hope to see auto generated docs based on docstring but sadly
it isnt so auto-magical... I had to add them in manually per module in 
``docs/source/index.rst`` where you see I reference 2 files
`modules.rst` and `modules_test.rst`

And then I did:

```bash
cd docs
make html
```

I like that sphinx ships with make, and we can definitely look to using make as our
over-arching tool, plays in nicely with c++.

But alternatively you could also generate the docs by doing:

```bash
pipenv run sphinx-build -b html docs/source docs/build/html
```

Also you obviously should source pipenv shell, and you dont have to actually
run pipenv run, but I just show the foolproof way here.

The resulting HTML documentation can be accessed by opening `docs/build/html/index.html` in a web browser.

If you are curious you'll see I've had to do quite bit of customisation for the config file
so that it could generate the docs > `docs/source/config.py`


I also explored creating PDF docs, I think these are really important if wanting to
send to end users, and that can be done using an addon called LatEx, but I havent set it
up as yet - but I have explored how to do it.


### Building Deployable Distributions

Finally to package this into a wheel! do the following:


```bash
pipenv run python setup.py bdist_wheel
```

This will create `build`, `example_package.egg-info` and `dist` directories. 
whl should be in `dist`. 

Annoyingly, you cant use pipfile for setup.py requirements,
so I had to take a shortcut of generate the requirements.txt by
doing

```bash
pipenv run pip freeze > requirements.txt
```
and i wrote a func in setup.py to read the file and use the it to
generate install_require, so that the generated wheel installs all the 
dependencies. 

But I make persist requirements.txt in git intentionally, so you
generate it everytime you want to create a distributable, i suppose
it could be made part of a make command.