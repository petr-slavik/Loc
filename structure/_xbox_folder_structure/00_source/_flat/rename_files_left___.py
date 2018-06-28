#!/usr/bin/env python3
import os
from colorama import Fore
from colorama import init
init()

directories = [d for d in os.listdir('.') if os.path.isdir(d)]

print(Fore.LIGHTMAGENTA_EX+"\n\n\n-----------------------------------------------------------------------------------")
print("/////////        Running Rename filles acording to LCID Script          ///////////")
print("-----------------------------------------------------------------------------------")

for directory in directories:
    for file in os.listdir(directory):
        file = os.path.join(directory, file)
        if os.path.isfile(file):
            extension = directory + '\\' 
            new_ext = directory + '\\' + directory + '_'
            new_file = file.replace(extension, new_ext)
            os.rename(file, new_file)