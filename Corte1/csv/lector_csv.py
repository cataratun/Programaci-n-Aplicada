import csv

with open ('personas.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print("Ap. materno: {0}, Ap. paterno: {1}, Nombre: {2}, Edad: {3}".format(row[0], row[1], row[2], row[3]))
