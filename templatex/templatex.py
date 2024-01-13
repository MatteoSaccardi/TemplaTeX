# templatex/templatex.py

import sys
import os
import shutil

def get_all_directory_names(directory):
    directory_names = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    return directory_names

def copy_folder_contents(source_folder, destination_folder):
    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    # Copy contents of source folder to destination folder
    for item in os.listdir(source_folder):
        source_item = os.path.join(source_folder, item)
        destination_item = os.path.join(destination_folder, item)
        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item, symlinks=True)
        else:
            shutil.copy2(source_item, destination_item)
 
def main():
    print('Hi, welcome to TemplaTeX!')
    print('Do you want to obtain the template for a Paper [0], Notes, [1], Poster [2] or a Presentation [3]? ')
    template_type = int(input())
    if template_type == 0:
        file = 'Paper'
    elif template_type == 1:
    	file = 'Notes'
    elif template_type == 2:
    	file = 'Poster'
    elif template_type == 3:
    	file = 'Presentation'
    else:
    	print('Not a valid number, exit from TemplaTeX.')
    	print('Thanks for using TemplaTeX!')
    	print('Matteo Saccardi')
    	print('')
    	return
    here = os.getcwd()
    templates = get_all_directory_names(here+'/Templates/'+file)
    if len(templates) > 1:
    	print('These are the following available templates:')
    	print(templates)
    	print('Indicate which one you want to use (count from 0): ')
    	which_template = int(input())
    	templates = [ templates[which_template] ]
    print(f'You chose the template for {file} of type {templates[0]}')
    new_folder = None
    while new_folder is None:
    	print(f'Name the folder you want to create with the template')
    	new_folder = input()
    	if os.path.exists(new_folder):
    		print('Folder already exists, choose another name')
    		new_folder = None
    copy_folder_contents(here+'/Templates/'+file+'/'+templates[0], new_folder)
    print('Successful creation of your template!')
    print('Thanks for using TemplaTeX!')
    print('Matteo Saccardi')
    print('')

if __name__ == "__main__":
    main()

