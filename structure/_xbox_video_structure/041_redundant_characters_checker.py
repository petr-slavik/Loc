import re
import os
from colorama import Fore
from colorama import init
init()

'''This will check if there are any redundant
characters between <target> and <mrk> tags.
If they are present script will remove them.'''

dir_path = str(os.path.dirname(os.path.realpath(__file__))) + "\\03_fromtrans\\_QA"
regex = r"target>(\w+)<mrk"
subst = r"target><mrk"

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

for root, dirs_d, files_d in os.walk(dir_path):
    for dir_d in dirs_d:
        if (dir_d == "ja-JP") or (dir_d == "ko-KR") or (dir_d == "zh-CN"):
            for subdir, dirs, files in os.walk(root + os.sep + dir_d):
                for file in files:
                    filepath = root + os.sep + dir_d + "\\" + file
                    with open(filepath, encoding='UTF8', mode='r+') as soubor:
                        test_str = soubor.read()
                        if re.search(regex, test_str):
                            redundant = re.search(regex, test_str).group(1)
                            print(file + Fore.LIGHTCYAN_EX+f" contains redundant characters '{redundant}' between <Target> and <Mrk>")
                            result = re.sub(regex, subst, test_str, 0)
                            deleteContent(soubor)
                            soubor.write(result)
                            print(Fore.LIGHTWHITE_EX+"Redundant characeters removed")
                            