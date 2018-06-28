import zipfile
import os
from colorama import Fore
from colorama import init
init()

'''This will unzip all zip files in 00_source folder and extract then to 00_source\_flat folder'''

dirpath = os.getcwd()
zipfiles = [file for file in os.listdir('00_source') if file.endswith(".zip")]

print(Fore.LIGHTBLUE_EX+"\n\n\n-----------------------------------------------------------------------------------")
print("/////////                  Running UnZipping Script                     ///////////")
print("-----------------------------------------------------------------------------------")

print("\nUNZIPPED:")

for zfile in zipfiles:
    archive = dirpath +"\\00_source\\"+ zfile
    with zipfile.ZipFile(archive,"r") as zip_ref:
        zip_ref.extractall(dirpath+"\\00_source\\_flat")
        print(archive)