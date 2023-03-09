import csv

def importer_csv():
    filePath = "test_python.csv"
    liste_dicos = []
    fichier_csv = open(filePath, 'r', encoding='UTF-8', newline= '')
    lecteur_csv = csv.DictReader(filePath, delimiter = ";")
    for element in lecteur_csv:
        liste_dicos.append(dict(element))
    fichier_csv.close()
    return liste_dicos




if __name__ == "__main__":
    importer_csv()