import re, string, os


dir_path = str(os.path.dirname(os.path.realpath(__file__))) + "\\01_prep\\01_trados"

file_list = [file for file in os.listdir(dir_path) if file.endswith(".sdlproj")]
file = dir_path + "\\" + file_list[0]

new_file = "_new_" + file_list[0]
pattern = re.compile(r'(serverAddress=)(.*?)"')
entity = {
    "/": "%2f",
    r"\+": "%2b",
    "=": "%3d",
    ":": "%3a",
    "@": "%40"
}

def zmen_entitu(adresa):
    for key in entity:
        new_server_address = re.sub(key, entity[key], adresa)
        adresa = new_server_address
    return new_server_address

with open(file, "r") as soubor:
    novy_soubor = open(dir_path + "\\" + new_file, "w")
    i = 1
    for numero, line in enumerate(soubor, start=1):
        #print(line.strip(), re.match("serverAddress", line))
        server_address = pattern.search(line)
        if server_address:
            print(f"{i}): ", zmen_entitu(server_address.group(2)))
            i+=1 
            edited_line = line.replace(server_address.group(2), zmen_entitu(server_address.group(2)))
            novy_soubor.write(edited_line)
        else:
            novy_soubor.write(line)
    novy_soubor.close()

os.rename(file, file + ".bac")
os.rename(dir_path + "\\" + new_file, dir_path + "\\" + file_list[0])