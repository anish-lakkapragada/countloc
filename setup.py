import sys
from setuptools import setup

version_name = sys.argv[1].replace("refs/tags/", "")
del sys.argv[1]

with open("README.md", "r") as fh:
    read_me_description = fh.read()

setup(
    name = 'countloc',
    version=version_name,
    author = "Anish Lakkapragada", 
    author_email="anish.lakkapragada@gmail.com",
    description = "countloc is a simple CLI to count the number of lines of code in your directory that you wrote.", 
    keywords=["LOC", "SLOC", "CLI"], 
    packages = ['countloc'],
    license="MIT",
    long_description = read_me_description, 
    long_description_content_type="text/markdown",
    entry_points = {
        'console_scripts': [
            'countloc = countloc.__main__:main'
        ]
    })