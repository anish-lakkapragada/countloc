from setuptools import setup

setup(
    name="countloc",
    version="0.1",
    packages=['countloc'],
    entry_points={
        'console_scripts': [
            'countloc = countloc.__main__:main'
        ]
    }
)