# templatex/templatex.py

import sys
import os
import shutil
import requests
from zipfile import ZipFile

def download_and_extract_github_folder(path_to_folder,new_folder):
    # Construct the URL to download the repository as a zip file
    repo_url = 'https://github.com/MatteoSaccardi/templatex'
    folder_url = repo_url + '/' + path_to_folder
    # Make a request to get the zip file
    response = requests.get(folder_url, stream=True)
    # Ensure the request was successful (status code 200)
    if response.status_code == 200:
        # Create a temporary file to save the zip content
        zip_filename = 'temp.zip'
        with open(zip_filename, 'wb') as zip_file:
            for chunk in response.iter_content(chunk_size=128):
                zip_file.write(chunk)
        # Extract the contents of the zip file
        with ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(new_folder)
        # Remove the temporary zip file
        os.remove(zip_filename)
        print(f'Downloaded and extracted {folder_url}')
    else:
        print(f"Failed to download {folder_url}. Status code: {response.status_code}")
 
def main():
    print('Hi, welcome to TemplaTeX!')
    templates = { 'Paper'       : [ 'Default', 'JHEP', 'PoS', 'Cimento' ],
	          'Notes'       : [ 'Default' ],
	          'Poster'      : [ 'Default' ],
	          'Presentation': [ 'Default' ],
	        }
    print('Do you want to obtain the template for a Paper [0], Notes, [1], Poster [2] or a Presentation [3]? ')
    template_type = int(input())
    if template_type == 0:
        file_ = 'Paper'
    elif template_type == 1:
    	file_ = 'Notes'
    elif template_type == 2:
    	file_ = 'Poster'
    elif template_type == 3:
    	file_ = 'Presentation'
    else:
    	print('Not a valid number, exit from TemplaTeX.')
    	print('Thanks for using TemplaTeX!')
    	print('Matteo Saccardi')
    	print('')
    	return
    templates = templates[file_]
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
    #path_to_folder = here+'/Templates/'+file_+'/'+templates[0]
    #copy_folder_contents(path_to_folder, new_folder)
    path_to_folder = 'Templates/'+file_+'/'+templates[0]
    download_and_extract_github_folder(path_to_folder,new_folder)
    print('Successful creation of your template!')
    print('Thanks for using TemplaTeX!')
    print('Matteo Saccardi')
    print('')

if __name__ == "__main__":
    main()

