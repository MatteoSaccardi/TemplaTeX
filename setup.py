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
    author_email="matteo.saccardi97@gmail.com",
    description="TeX template generator for scientific papers, notes, posters and presentations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MatteoSaccardi/templatex",
    packages=find_packages(),
    include_package_data=True,   # 🔥 IMPORTANT
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'templatex = templatex.templatex:main',
        ],
    },
    keywords=["LaTeX", "templates", "scientific papers", "notes", "posters", "presentations"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv2",
        "Operating System :: OS Independent",
    ],
)
