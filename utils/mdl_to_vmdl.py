# cmd command: python mdl_to_vmdl.py "C:\Program Files (x86)\Steam\steamapps\common\SteamVR\tools\steamvr_environments\content\steamtours_addons\l4d2_converted\models"
# MUST run in the models folder

import re, sys, os, io, re

from tqdm import tqdm
from colorama import init
from termcolor import colored, cprint

init()

# name of file that stores all paths we need
FILE_MULTIPLE_CONVERT_NAME = 'paths.txt'

INPUT_FILE_EXT = '.mdl'
OUTPUT_FILE_EXT = '.vmdl'

VMDL_BASE = '''<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->
{
    m_sMDLFilename = "<mdl>"
}
'''

def text_parser(filepath, separator="="):
    return_dict = {}
    with open(filepath, "r") as f:
        for line in f:
            if not line.startswith("//") or line in ['\n', '\r\n'] or line.strip() == '':
                line = line.replace('\t', '').replace('\n', '')
                line = line.split(separator)
                return_dict[line[0]] = line[1]
    return return_dict

def walk_dir(dirname):
    files = []

    for root, dirs, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.lower().endswith(INPUT_FILE_EXT):
                files.append(os.path.join(root,filename))
            
    return files

def putl(f, line, indent = 0):
    f.write(('\t' * indent) + line + '\r\n')

def strip_quotes(s):
    return s.strip('"').strip("'")

def fix_path(s):
    return strip_quotes(s).replace('\\', '/').replace('//', '/').strip('/')

def relative_path(s, base):
    base = base.replace(abspath, '')
    base = base.replace(os.path.basename(base), '')

    return fix_path(os.path.basename(abspath) + base + '/' + fix_path(s))

def get_mesh_name(file):
    return os.path.splitext(os.path.basename(fix_path(file)))[0]

def convert_multiple_get_valid_paths():
    buff_paths = []
    paths_filtered = []
    path_index = ''

    with io.open(FILE_MULTIPLE_CONVERT_NAME, encoding='utf-8') as file_src:
        # open file and read all in buffer
        buff_paths = [row.rstrip() for row in file_src]
        
    for i in buff_paths:
        # check valid paths
        path_index = re.findall(r'^[a-zA-Z]:[\\\S|*\S]?.*$', i) 
        
        if (bool(path_index) != False):
            for j in path_index:
                # right paths we write in filtered list
                if (os.path.exists(j)):
                    paths_filtered.append(j)
    
    return(paths_filtered)


def convert_multiple_generate_vmdl(paths_array):
    _paths = paths_array

    for i in _paths:
        files = []
        
        PATH_TO_CONTENT_ROOT = i
        
        abspath = os.path.abspath(PATH_TO_CONTENT_ROOT)
        print('\nConverting "' + abspath + '"')
        
        for j in tqdm(range(len(_paths))):
    
            if os.path.isdir(abspath):
                files.extend(walk_dir(abspath))

                for filename in files:
                    # replacing format name
                    out_name = filename.replace(INPUT_FILE_EXT, OUTPUT_FILE_EXT)

                    #print('\tImporting', colored(os.path.basename(filename), 'yellow'))

                    out = sys.stdout

                    sourcePath = "models" + filename.split("models", 1)[1] # HACK?
                    mdl_path = fix_path(sourcePath)
    
                    with open(out_name, 'w') as out:
                        putl(out, VMDL_BASE.replace('<mdl>', mdl_path).replace((' ' * 4), '\t'))

        print(colored('\tConverting completed!', 'green'))
    
    pass

def convert_multiple_main():
    paths = []

    # if file exists
    if (os.path.isfile(FILE_MULTIPLE_CONVERT_NAME)):
        paths = convert_multiple_get_valid_paths()

        if (bool(paths) != False):
            #print all valid paths
            print("\nValid paths:")
            for i in paths:
                print(colored('+ ' + i, 'green'))
            print('--------------------------------------------------------------------------------------------------------')
            
            convert_multiple_generate_vmdl(paths)
        
        else:
            invalidMsg = colored('Valid paths not found! Check your paths with example: ', 'red') + colored('C:\\Steam\\steamapps\\Half-Life Alyx\\content\\tf\\models\\props_spytech\\', 'green')
            print(invalidMsg)

    else:
        textInvalid = colored(FILE_MULTIPLE_CONVERT_NAME + ' not found! Add ' + FILE_MULTIPLE_CONVERT_NAME + ' file and fill it with some of the paths you need.', 'red')
        print(textInvalid)
        
    pass

def convert_once_main():
    finalCommand = ''

    while (not finalCommand == 'n'):
        PATH_TO_CONTENT_ROOT = input("\nWhat folder would you like to convert? Valid path format example: C:\\Steam\\steamapps\\Half-Life Alyx\\content\\tf\\models\\props_spytech\\ \nPath: ").lower()
    
        if (not os.path.exists(PATH_TO_CONTENT_ROOT)):
            textInvalid = colored('Path "' + PATH_TO_CONTENT_ROOT + '" is invalid! Check path with valid format example:', 'red') + colored(' C:\\Steam\\steamapps\\Half-Life Alyx\\content\\tf\\models\\props_spytech\\ \n', 'green')
            print(textInvalid)
        else:
            # recursively search all dirs and files
            abspath = os.path.abspath(PATH_TO_CONTENT_ROOT)
            print('\nConverting "' + abspath + '"')
    
            if os.path.isdir(abspath):
                files.extend(walk_dir(abspath))

            for i in tqdm(range(len(files))):

                for filename in files:
                    out_name = filename.replace(INPUT_FILE_EXT, OUTPUT_FILE_EXT)

                    #print('\tImporting', colored(os.path.basename(filename), 'yellow'))

                    out = sys.stdout

                    sourcePath = "models" + filename.split("models", 1)[1] # HACK?
                    mdl_path = fix_path(sourcePath)
    
                    with open(out_name, 'w') as out:
                        putl(out, VMDL_BASE.replace('<mdl>', mdl_path).replace((' ' * 4), '\t'))
        
            print(colored('\tConverting completed!', 'green'))
        
        finalCommand = input('\nDo you want to continue? "n" - back. \ny/n: ')
  
    pass

print('\nSource 2 VMDL Generator! By Rectus via Github.')
print("Initially forked by Alpine, based on caseytube's fork, this version by 5FB5.")
print("Version: 1.1.2")
print('--------------------------------------------------------------------------------------------------------')
print('Reminder to put your models in the same directory structure as Source 1, starting with models!\n')

abspath = ''
files = []

# Warning message if we haven't file
if (not os.path.isfile(FILE_MULTIPLE_CONVERT_NAME)):
    warningMsg = FILE_MULTIPLE_CONVERT_NAME + ' file for multiple converting ' + colored('not founded!\n', 'yellow')
    print(warningMsg)
else:
    validMsg = FILE_MULTIPLE_CONVERT_NAME + ' file for multiple converting ' + colored('detected!\n', 'green')
    print(validMsg)

# Main function
while (True):
    startupMsg = input('\nDo you want to convert multiple files automatically ("a") or specific one manually ("m") or quit ("q")? \na/m/q: ')

    if (startupMsg == 'a'):
        convert_multiple_main()
    
    elif (startupMsg == 'm'):
        convert_once_main()
    
    elif (startupMsg == 'q'):
        print('Quitting program...')
        sys.exit(0)
