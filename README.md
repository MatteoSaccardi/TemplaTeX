# TemplaTeX
TeX template generator for scientific papers, notes, posters and presentations, written in Python.

## Authors

Copyright (C) 2024, Matteo Saccardi

## Installation

The latest version of the package can be installed using `pip` directly from the github server.

```bash
pip install -U git+https://github.com/MatteoSaccardi/templatex.git@main
```

Alternatively after cloning the git repository, the package
can be installed in development mode, to keep it up to date
with every `git pull`

```bash
git clone git@github.com:MatteoSaccardi/templatex.git
cd templatex
pip install -e .
```

### Crucial step in the installation
One final step: we need to move manually the folder Templates into the local installation from pip.
You can download it from Github, or follow the terminal commands below, where we temporarily need 
to git clone the repository, move the desired folder and then delete the rest.
```bash
git clone https://github.com/MatteoSaccardi/templatex && cd templatex && mv Templates $(pip show -f templatex | grep Location | cut -d ' ' -f 2)/templatex && cd .. && rm -rf templatex
```

## Usage
After installing, you only need to type templatex in your terminal to activate the correct script
to generate the template. Then, just follow the instructions that appear in your terminal.
Enjoy!
