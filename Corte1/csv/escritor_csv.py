import csv

amigos = []
while True:
    entrada = input("Ingrese los datos del amigo (Apellido1, Apellido2, Nombre, Edad) separados por comas, o 'salir' para terminar: ")
    if entrada.lower() == 'salir':
        break
    try:
        apellido1, apellido2, nombre, edad = entrada.split(',')
        amigos.append([apellido1.strip(), apellido2.strip(), nombre.strip(), int(edad.strip())])
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar los datos en el formato correcto.")

"""amigos = [
    ['Gonzalez', 'Lopez', 'Juan', 25],
    ['Martinez', 'Hernandez', 'Maria', 30],
    ['Perez', 'Gomez', 'Carlos', 22],
    ['Sanchez', 'Diaz', 'Ana', 28],
    ['Torres', 'Morales', 'Luis', 35]
]
"""

with open ('amigos.csv', 'w', newline = '') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerows(amigos)