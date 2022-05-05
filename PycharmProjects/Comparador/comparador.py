import csv
# archivo para leer tags de un archivo csv y buscarlo en otro
ejemplo = [] # cadena donde guardamos los tags
# debemos tener en cuenta que el archivo que se va a abrir en
# la siguiente linea tiene un formato determinado donde se
# la 3ra columna pertenece al tag que queremos identificar
with open('datos_antena.csv') as file:
    reader = csv.reader(file, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        ejemplo.append(row[2])

# en este archivo aprovechamso el metodo 'read' que lee el archivo .csv
# como una cadena completa, comparamos la salida con -1 debido a que
# si no encontramos la cadena que queremos en el archivo el metodo
# find nos devuelve dicho valor.
for tag in ejemplo:
    if open('Prueba.csv', 'r').read().find(tag) !=-1:
        print(tag)
        print('Encontrado')
