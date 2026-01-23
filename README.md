# TemplaTeX
TeX template generator for scientific papers, notes, posters, and presentations, written in Python. 
With a single command, you can quickly create a ready-to-use LaTeX project folder from pre-defined templates.

## Authors

Copyright (C) 2026, Matteo Saccardi

## Installation

The latest version of the package can be installed using `pip` directly from the github server.

```bash
pip install -U git+https://github.com/MatteoSaccardi/templatex.git@main
```

### Alternative Installation: Development Mode

To install the package in development mode (so updates from git pull are reflected immediately):

```git clone git@github.com:MatteoSaccardi/templatex.git
cd templatex
pip install -e .
```

## Usage

After installation, simply run:

`templatex`

You will be prompted to select the type of template:

`Paper [0], Notes [1], Poster [2], Presentation [3]`

If multiple templates are available for a type (e.g., Paper), you can choose one from a list. 
Then you can name the folder to create for your project, and TemplaTeX will copy all necessary files.

### macOS / Linux Notes

The templatex command should work out of the box.

If you installed Python locally (e.g., `--user`), make sure your local bin directory is in your PATH:

`export PATH="$HOME/Library/Python/3.9/bin:$PATH"  # adjust Python version`

You can add this line to ~/.bashrc, ~/.zshrc, or ~/.bash_profile to make it permanent.

## Example
`$ templatex
Hi, welcome to TemplaTeX!
Do you want to obtain the template for a Paper [0], Notes, [1], Poster [2] or a Presentation [3]? 
0
These are the following available templates:
['JHEP', 'Default', 'PoS', 'PRD']
Indicate which one you want to use (count from 0): 3
You chose the template for Paper of type PRD
Name the folder you want to create with the template: MyPaper
Successful creation of your template!
Thanks for using TemplaTeX!
`

Your folder MyPaper/ now contains the selected LaTeX template ready to edit.
Enjoy!
