#Recebe um array de inteiros maiores que zero e retorna a quantidade de números pares existentes no array

import random
lista = []

quantidade = int(input('digite a quantidade de elementos '))
for i in range(0, quantidade):
    numero = random.randrange(100)
    lista.append(numero)


def parOuImpar(lista):
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares += 1
    print(f'tem {pares} numeros pares')


print(lista)

parOuImpar(lista)
