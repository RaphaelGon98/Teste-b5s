# A função deverá receber um array com pelo menos 3 itens e retornar a média simples de todos os itens do array.
# Caso o array recebido possua menos que 3 itens, deverá ser retornado o boleano false.

lista = []

quantidade = int(input('digite a quantidade de elementos'))
for i in range(0, quantidade):
    numero = int(input('digite um numero '))
    lista.append(numero)


def mediaSimples(lista):
    soma = 0
    resposta = False
    if len(lista) == 3:
        for i in lista:
            soma = soma + i
        media = soma / 3
        print(f'a media é : {media}')
    else:
        print(resposta)


mediaSimples(lista)
