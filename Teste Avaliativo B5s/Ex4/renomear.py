#A função deverá receber uma string e retornar a mesma invertida.

palavra = str(input('digite uma palavra '))


def inverter(palavra):
    return palavra[::-1]


print(inverter(palavra))
