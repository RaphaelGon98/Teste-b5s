#A função irá receber um array de inteiros e retornar o primeiro elemento não repetido.

lista = ['4', '1', '5', '8', '5', '3', '4', '3', '2']
listaNaoRepetidas = []


def removeRepetidos():
    for i in lista:
        if lista.count(i) == 1:
            listaNaoRepetidas.append(i)


removeRepetidos()
print(listaNaoRepetidas[0])
