from setuptools import setup

import sys

version_name = sys.argv[1].replace("refs/tags/", "")
del sys.argv[1]

setup(
    name = 'countloc',
    version="0.67", 
    author = "Anish Lakkapragada", 
    author_email="anish.lakkapragada@gmail.com",
    description = "countloc is a fun application to count the loc in ur dir", 
    keywords=["Fun"], 
    packages = ['countloc'],
    entry_points = {
        'console_scripts': [
            'countloc = countloc.__main__:main'
        ]
    })