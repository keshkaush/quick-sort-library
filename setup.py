from importlib.util import find_spec
from xml.etree.ElementInclude import include
from setuptools import setup, find_packages
import os

long_description = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

setup(
    name="quick-sorting-code",
    version="0.1.SNAPSHOT",
    description="quick sort libaray",
    long_description= long_description,
    author="keshav kaushik",
    author_email="keshav.kaushik@airbus.coms",
    package_dir={"":"src"},
    packages=find_packages(include=["quick_sort"]),
    license="MIT",
    classifiers=['License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'],
    requires=[""],
)