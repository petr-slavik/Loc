import re
import os
import sys
import msvcrt
import xml.etree.ElementTree as etree
from colorama import Fore
from colorama import init
init()

#----------------------------- DECLARATION --------------------------
'''
Script will remove files that do not belong to certain language based on given conversion table 

1. Do backup of you Trados structure

Notes:
	- regular expressions are used to identify language code
	- case is ignored
	- can be defined if "foldernames" or "filenames" are used for language identification

Known issues:
	Long path issue - script will ends with this error:
	"FileNotFoundError: [WinError 3] The system cannot find the path specified: ..."
	Solution: Use shorter path

convertTable = [
[TRADOS_LANGUAGE_CODE,[list of regular expressions for trados code identification based on "subfolder"/"file"]]
...
]
'''

#path to trados structure
trados_path = os.getcwd()+os.sep+"01_prep\\01_trados"+os.sep

#store detection type "folder" or "file"
detectionType = "file"
#detection table
convertTable = [
["cs-CZ",["(.*?)cs-CZ(.*?)","cs-cz_"]],
["da-DK",["(.*?)da-DK(.*?)","da-dk"]],
["de-DE",["(.*?)de-DE(.*?)","de-de"]],
["el-GR",["(.*?)el-GR(.*?)","el-gr"]],
["en-GB",["(.*?)en-GB(.*?)","en-gb"]],
["es-ES",["(.*?)es-ES(.*?)","es-es"]],
["es-MX",["(.*?)es-MX(.*?)","es-mx"]],
["fi-FI",["(.*?)fi-FI(.*?)","fi-fi"]],
["fr-CA",["(.*?)fr-CA(.*?)","fr-ca"]],
["fr-FR",["(.*?)fr-FR(.*?)","fr-fr"]],
["hu-HU",["(.*?)hu-HU(.*?)","hu-hu"]],
["it-IT",["(.*?)it-IT(.*?)","it-it"]],
["ja-JP",["(.*?)ja-JP(.*?)","ja-jp"]],
["ko-KR",["(.*?)ko-KR(.*?)","ko-kr"]],
["nb-NO",["(.*?)nb-NO(.*?)","nb-no"]],
["nl-NL",["(.*?)nl-NL(.*?)","nl-nl"]],
["pl-PL",["(.*?)pl-PL(.*?)","pl-pl"]],
["pt-BR",["(.*?)pt-BR(.*?)","pt-br"]],
["pt-PT",["(.*?)pt-PT(.*?)","pt-pt"]],
["ru-RU",["(.*?)ru-RU(.*?)","ru-ru"]],
["sk-SK",["(.*?)sk-SK(.*?)","sk-sk"]],
["sv-SE",["(.*?)sv-SE(.*?)","sv-se"]],
["tr-TR",["(.*?)tr-TR(.*?)","tr-tr"]],
["zh-CN",["(.*?)zh-CN(.*?)","zh-hans"]],
["zh-HK",["(.*?)zh-HK(.*?)","zh-hanh"]],
["zh-TW",["(.*?)zh-TW(.*?)","zh-hant"]]
]
#-----------------------------  FUNCTIONS  --------------------------
def getLanguageCode(string):
	returnValue="n/a"
	for code in convertTable:
		for c in code[1]:
			ignorecase = re.compile(c, re.IGNORECASE)
			if ignorecase.match(string)!=None:
				return code[0]
	return returnValue

def wait():
    msvcrt.getch()

#----------------------------- START POINT --------------------------
#clear screen
#os.system('cls')

print(Fore.LIGHTGREEN_EX+"\n\n\n\n-----------------------------------------------------------------------------------")
print("/////////    Deleting extra files from Trados project in progress...    ///////////")
print("-----------------------------------------------------------------------------------")

#store project file path
for file in os.listdir(trados_path):
#	print(file)
	if file.endswith(".sdlproj"):
		tradosProjectFile = trados_path+file
		break
#set parser and read the file / get root
parser = etree.XMLParser()
tree = etree.parse(tradosProjectFile)
#save original file as backup
tree.write(tradosProjectFile+".backup")
#get source language
sourceLanguageCode = tree.find(".//LanguageDirections/LanguageDirection").get("SourceLanguageCode")
print("Source language: " + sourceLanguageCode)
#load project files tree
groups = tree.findall(".//ProjectFile")
for group in groups:
	#if detection is based on "folder" get language code from path

	if detectionType=="folder":
		correctLanguageCode = getLanguageCode(group.get("Path"))
		if correctLanguageCode=="n/a":
			print("Folder: \"" + group.get("Path") + "\" can't detect trados language code!")
			continue
		else:
			print("Folder: \"" + group.get("Path") + "\" detected as \"" + correctLanguageCode + "\" - content removed for all other languages except "+sourceLanguageCode)
	#if detection is based on "filename" get language code from filename
	if detectionType=="file":
		correctLanguageCode = getLanguageCode(group.get("Name"))
		if correctLanguageCode=="n/a":
			print("File: \"" + group.get("Name") + "\" can't detect trados language code!")
			continue
		else:
			print("File: \"" + group.get("Name") + "\" detected as \"" + correctLanguageCode + "\"")
	filesHolder = group.find("LanguageFiles")
	files = filesHolder.findall("LanguageFile")
	for file in reversed(files):
		#get file language code
		currentFileLanguageCode = file.get("LanguageCode")
		#do not delete source language
		if currentFileLanguageCode!=sourceLanguageCode:
			#do not delete correct language
			if currentFileLanguageCode!=correctLanguageCode:
				#delete xml node here
				filesHolder.remove(file)
				#delete file from trados structure here
				os.remove(os.path.dirname(tradosProjectFile)+os.sep+currentFileLanguageCode+os.sep+group.get("Path")+group.get("Name")+".sdlxliff")

#save adusted file
tree.write(tradosProjectFile)

#end
print("-----------------------------------------------------------------------------------")
print("/////////           Extra files from trados project deleted             ///////////")
print("-----------------------------------------------------------------------------------\n\n\n\n")