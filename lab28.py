import math
def sum_dos(lista):
    i = 0
    while i < len(lista):
        k = i + 1
        while k < len(lista):
            suma = lista[i] + lista[k]
            if suma == 0:
                print(lista[i], "y", lista[k], "suman 0")
            k += 1
        i += 1
    return 0
sum_dos([-1, 1, 3, -1, -2, -3, 4, 5, 6, -4, -5, -6])