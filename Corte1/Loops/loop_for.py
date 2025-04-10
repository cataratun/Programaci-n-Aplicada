import time

cadena = 'python'

for letra in cadena:
    if letra == 't':
        continue
    print(letra)
    time.sleep(1)