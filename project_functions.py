from json import dump as jdump
from json import load
from json import loads
from json import dumps
from yaml import dump as ydump
from yaml import safe_load
from csv import DictReader as csv_load
from csv import DictWriter as csv_write
from xmltodict import parse
from dicttoxml import dicttoxml as dtx

def python_structure(file):
    reader = ''
    with open(file, 'r') as thefile:
        if file.endswith('.json'):
            reader = load(thefile)
        elif file.endswith('.yaml') or file.endswith('.yml'):
            reader = safe_load(thefile)
        elif file.endswith('.csv'):
            # this = {}
            this = []
            k = 0
            reader = csv_load(thefile)
            # for element in reader:
            #     this.setdefault("value" + str(k), element)
            #     k +=1
            # reader = this
            for element in reader:
                this.append(element)
            reader = this
        elif file.endswith('.xml'):
            reader = loads(dumps(parse(thefile.read())))
        return reader


def converter(pdata, extent):
    with open('new_file.' + extent, 'w') as target:
        if extent == 'json':
            jdump(dumps(pdata), target)
        elif extent == 'yaml' or extent == 'yml':
            ydump(pdata, target)
        elif extent == 'csv':
            pdata = [pdata]
            fieldnames = pdata[0].keys()
            # n = int(input("Entrer la taille de l'entete: "))
            # fieldnames = [input() for i in range(n)]
            output = csv_write(target, fieldnames)
            output.writeheader()
            for elem in pdata:
                output.writerow(elem)
        elif extent == 'xml':
            xml = dtx(pdata)
            target.write(str(xml, 'utf-8'))
