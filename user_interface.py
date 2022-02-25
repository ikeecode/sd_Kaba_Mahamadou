from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from pathlib import Path
from os.path import abspath
from os.path import basename
from os import chdir
from project_functions import python_structure
from project_functions import converter


root = Tk()
root.title('Convertisseur Xml-Json-Csv-Yaml')
root.geometry('700x490+900+160')
root.resizable(True, True)

pdata =''

def output_extent(pdata, choice_name, self):
    print(self)
    output_folder = askdirectory()
    chdir(abspath(output_folder))
    converter(pdata, choice_name, self)

# construction des choix de sortie du fichier
def construct_button(pdata, choice_name, extent):
    # row = 10, column = 1
    button_1 = Button(root, text = extent[0], command = lambda: output_extent(pdata, choice_name, extent[0]))
    button_2 = Button(root, text = extent[1], command = lambda: output_extent(pdata, choice_name, extent[1]))
    button_3 = Button(root, text = extent[2], command = lambda: output_extent(pdata, choice_name, extent[2]))

    button_1.grid(row=4, column=2)
    button_2.grid(row=4, column=3)
    button_3.grid(row=4, column=4)


def recup_file():
    file = askopenfilename(title='Ouvrir file',
                       filetypes=[("files",".xml .json .yml .yaml .csv")],
                       initialdir=str(Path.home()) + '/Bureau/')

    extents = ['json', 'xml', 'csv', 'yaml', 'yml']
    chemin_file = abspath(file)
    file = basename(file).split('.')
    choice_name = file[0]
    choice_extent = file[-1]
    if choice_extent in ['yaml', 'yml']:
        extents.remove('yaml')
        extents.remove('yml')
    else:
        extents.remove(choice_extent)
    pdata = python_structure(chemin_file)
    construct_button(pdata, choice_name, extents)
    # print(extents)
    # print(pdata)






filing = Label(root, text='Svp ajouter un fichier', font=('Arial 20 bold'), bg='grey', fg='white')
filing_btn = Button(root, text='Charger fichier', command=recup_file)

output_line = Label(root, text='', anchor='w', justify='left')

filing.grid(row=1, column=1)
filing_btn.grid(row=2, column=1)

root.mainloop()
