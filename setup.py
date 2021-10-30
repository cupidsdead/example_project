import os
from setuptools import setup

# get key package details from example_project/__version__.py
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'example_project', '__version__.py')) as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

with open("./requirements.txt") as f:
    requirements = f.read().splitlines()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html

setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['example_project'],
    include_package_data=True,
    python_requires=">=3.9.*",
    install_requires=requirements,
    license=about['__license__'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['example_project=example_project.cli:main'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='package development template'
)
