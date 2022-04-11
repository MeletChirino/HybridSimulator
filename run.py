# python modules
import sys
from os import mkdir, path
import os

if __name__ == "__main__":
    if sys.argv[1] == 'createtest':
        #create test
        parent_folder = os.getcwd()
        print(F'parent = {parent_folder}')
        new_folder_name = sys.argv[2]
        print(new_folder_name)
        new_folder = F'{parent_folder}/tests/{new_folder_name}'
        mkdir(new_folder)
        new_files = ['main.py', '__init__.py']
        for file in new_files:
            f = open(F'{new_folder}/{file}', 'a')
            f.write(' ')
            f.close()

        new_folder = F'{parent_folder}/tests/{new_folder_name}/img'
        mkdir(new_folder)

    elif sys.argv[1] == 'runtest':
        test_name = sys.argv[2]
        command = F"import tests.{test_name}; {test_name}.main()"
        exec(command)
