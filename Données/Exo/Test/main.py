#phrase = "Une être humain est une machine sophistiquée."
#print(phrase.split())
#
#registre = [1,{'nom':'HILIUM', 'prenom': 'Mohan', 'adresse':'224 avenue des fleurs 75001 Paaris', 'age': 67, 'taille':178, 'poids':81}]
#print(registre[1]['nom'])
#import csv
#filein = ''
#with open(filein, encoding='UFT-8') as file:
#    data = list(csv.reader(file))

table = [ ['lovelace', 'ada', 1815, 1852],
['von neumann','john', 1903, 1957],
['turing', 'alan', 1912, 1954],
['mccarthy', 'john', 1927, 2011],
['floyd', 'robert', 1936, 2001] ]
def age(personnage):
    return personnage[3] - personnage[2]
table.sort(key=age, reverse=True)
print(table)

#t = [ {'id':1, 'age':23, 'sejour':'PEKIN'},
# {'id':2, 'age':27, 'sejour':'ISTANBUL'},
# {'id':3, 'age':53, 'sejour':'LONDRES'},
# {'id':4, 'age':41, 'sejour':'ISTANBUL'},
# {'id':5, 'age':62, 'sejour':'RIO'},
# {'id':6, 'age':28, 'sejour':'ALGER'}]
#
#r = [ c for c in t if c['age']>30 and c['sejour']=='ISTANBUL' ]
#
#print(r)