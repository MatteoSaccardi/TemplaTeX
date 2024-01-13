from setuptools import setup

VERSION = (0, 1, 0)

def version():
    v = ".".join(str(v) for v in VERSION)
    return v

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="templatex",
    version=version(),
    author="Matteo Saccardi",
    author_email="m.saccardi@campus.unimib.it",
    description="Template generator for TeX scientific papers with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatteoSaccardi/templatex",
    packages=['templatex'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv2",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'templatex = templatex.templatex:main',
        ],
    },
)
