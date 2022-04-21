# from distutils.core import setup
from setuptools import find_packages, setup
import pathlib

setup(
    # Application name:
    name="tfjsa",
    
    # Version number (initial):
    version="0.0.1",
    
    # Application author details:
    author="Zhang",
    author_email="oo@zju.edu.cn",
    
    # Packages
    packages=["tfjsa"],

    package_dir={'templates': 'tfjsa/templates', 'static': 'tfjsa/static'},

    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="http://pypi.python.org/pypi/tfjsa/",
    
    #
    license="LICENSE",
    description="tfjs(Tensorflow js)-based Flask web apps.",
    
    # long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    
    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)

# To Build and Publish (for developer only), 
# Run: python setup.py sdist bdist_wheel; twine upload dist/*