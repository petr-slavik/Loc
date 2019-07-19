import codecs, re

#line length = 92
#length limit for trados = 88 chars

source_file = "00_source\\SIMGHELP.APE"
target_file = "00_source\\SIMGHELP_target_for_trans.APE"
new_target_file = "00_source\\SIMGHELP_target_new.APE"
pattern1 = r"\s+E$"
pattern2 = r"^Z\s+"
pattern = r"(^Z\s+)(.*?)(\s+E$)"

def nacti_source():
    with codecs.open(source_file, "r", encoding="utf8") as source:
        return source.readlines()


def nacti_target():
    with codecs.open(target_file, "r", encoding="utf8", errors="ignore") as target:
        return target.readlines()

source = [x.strip() for x in nacti_source()]


def skupiny(line):
    if line.startswith("Z"):
        prefix = re.search(pattern, line).group(1)
        text = re.search(pattern, line).group(2)
        suffix = re.search(pattern, line).group(3)
    return prefix, text, suffix



#Vytvori target soubr pro preklad, ocisteny od nepotrebnych znaku
def vytvor_target():
    with open(target_file, "x",  encoding="utf8", errors="ignore") as target:
        for x, line in enumerate(source, 1):
            if line.startswith("Z"):
                target.write((skupiny(line)[1]) + "\n")
            else:
                target.write("\n")
                #target.write(line + "\n")



def rekonstruuj_target():
    target = nacti_target()
    #print(target)
    with open(new_target_file, "w",  encoding="utf8", errors="ignore") as new_target:
        for x, line in enumerate(target, 0):
            if line.startswith("\r\n"):
                #print(x, source[x])
                new_target.write(source[x] + "\n")
            else:
                prefix = re.search(pattern, source[x]).group(1)
                konec = source[x][-1]
                new_line = prefix + line.strip()
                #Pokud je delka noveho stringu kratsi nez delka sourcu tak prida nakonec mezeru
                while (len(new_line) + 1) < len(source[x]):
                    new_line += " "
                print(new_line + konec)
                new_target.write(new_line + konec + "\n")




vytvor_target()
#rekonstruuj_target()