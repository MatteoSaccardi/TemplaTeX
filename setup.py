from setuptools import setup, find_packages

VERSION = (1, 0, 0)

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
    description="TeX template generator for scientific papers, notes, posters and presentations, written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatteoSaccardi/templatex",
    packages=['templatex'], #find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv2",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'templatex = templatex.templatex:main',
        ],
    },
    keywords=["LaTeX", "templates", "scientific papers", "notes", "posters", "presentations"],
    include_package_data=True,
    package_data={'templatex': ['Templates/*']},  # Include the Templates folder
)
