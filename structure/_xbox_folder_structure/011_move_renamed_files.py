import os
import shutil
from colorama import Fore
from colorama import init
init()

'''This will move renamed files to _flat folder and remove extra empty directoies '''

dir_path = str(os.path.dirname(os.path.realpath(__file__))) + "\\00_source\\_flat"

print(Fore.LIGHTCYAN_EX+"\n\n\n-----------------------------------------------------------------------------------")
print("/////////                 Running Move & Rename Script                  ///////////")
print("-----------------------------------------------------------------------------------")

# will move renamed files to _flat
for root, dirs_d, files_d in os.walk(dir_path):
    for dir_d in dirs_d:
        if dir_d != "en-US":
            for subdir, dirs, files in os.walk(root + os.sep + dir_d):
                for file in files:
                    filepath = root + os.sep + dir_d + "\\" + file
                    shutil.move(filepath, dir_path)
                    print("Processing: "+file)

# will remove empty directories
index = 0
for root, dirs, files in os.walk(dir_path):
    for dir in dirs:
        newDir = os.path.join(root, dir)
        index += 1
        #print(str(index) + " ---> " + newDir)

        try:
            os.removedirs(newDir) #It removes all non-empty folders
        except:
            pass #Exception is if a folder is not empty. Folder will stay untouched.
            #print("Directory not empty and will not be removed")
            #print(" ")

os.remove(dir_path + "\\" + "rename_files_left___.py")