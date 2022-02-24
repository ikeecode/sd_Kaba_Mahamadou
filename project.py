from os import listdir
from os import getcwd
from os import chdir
from os.path import isfile
from os.path import abspath

current_folder = getcwd()
foldername = input("Vous etes dans le dossier "+ current_folder + "\nEntrer le chemin du dossier ou on doit chercher les fichiers: ")
try:
    chdir(foldername)
except FileNotFoundError:
    print("Ce dossier n'existe pas !")

extents = ['json', 'xml', 'yaml', 'yml', 'csv']
myfiles = []
for file in listdir('.'):
    extension = file.split('.')[-1]
    if extension in ['json', 'xml', 'yaml', 'yml', 'csv']:
        if isfile(abspath(file)):
            myfiles.append(file)

print()
print("Choisir un fichier: ")
for i in range(len(myfiles)):
    print(i + 1, '-', myfiles[i])

choice = int(input("Entrer votre choix ici: "))

choice_name = myfiles[choice - 1].split('.')[0]
choice_extent = myfiles[choice - 1].split('.')[-1]
print("vous avez choisi", myfiles[choice - 1])


if choice_extent in ['yaml', 'yml']:
    extents.remove('yaml')
    extents.remove('yml')
else:
    extents.remove(choice_extent)

print("Choisissez un format de sortie: ")
for format in extents:
    print(format, " ", end="")
print()

output_extent =''
while output_extent not in extents:
    print("Choisir le bon format de fichier: ")
    output_extent = input()


# print(myfiles)
# print(extents)
