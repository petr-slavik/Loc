import re
import os
from colorama import Fore
from colorama import init
init()

'''This is substitute of Segment Action plugin for Trados.
It will check all files in lang folders (except of en-US) and
change Status from Draft to Translated for all strings with
origin tm or ap + percent 100 '''

dir_path = str(os.path.dirname(os.path.realpath(__file__))) + "\\01_prep\\01_trados"
regex = r"conf=\"(Draft)\" origin=\"(tm|ap)\" (percent=\"100\")?"
subst = r'conf="Translated" origin="\2" \3'

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

print(Fore.LIGHTYELLOW_EX+"-----------------------------------------------------------------------------------")
print("/////////                Running Segment Action Script                  ///////////")
print("-----------------------------------------------------------------------------------")

for root, dirs_d, files_d in os.walk(dir_path):
    for dir_d in dirs_d:
        if dir_d != "en-US":
            for subdir, dirs, files in os.walk(root + os.sep + dir_d):
                for file in files:
                    filepath = root + os.sep + dir_d + "\\" + file
                    with open(filepath, encoding='UTF8', mode='r+') as soubor:
                        test_str = soubor.read()
                        result = re.sub(regex, subst, test_str, 0)
                        deleteContent(soubor)
                        soubor.write(result)
                        print("Processing: " + filepath)

print("-----------------------------------------------------------------------------------")
print("/////////                             DONE                              ///////////")
print("-----------------------------------------------------------------------------------\n\n\n")