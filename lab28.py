import matplotlib.pyplot as plt
import time
def sum_dos(numeros):
    i = 0
    while i < len(numeros):
        k = i + 1
        while k < len(numeros):
            suma = numeros[i] + numeros[k]
            if suma == 0:
                print(numeros[i], "y", numeros[k], "suman 0")
            
            k += 1
        i += 1
    return 0
tamaño = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
numeros = []


sum_dos(numeros)
plt.bar(range(len(numeros)), numeros)
plt.show()