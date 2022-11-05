# A função deverá receber uma string e substituir todas as vogais da mesma pelo sinal '?'

palavra = input('digite uma palavra ')


def substituir(palavra):
    vogais = 'AEIOUaeiou'
    for i in vogais:
        palavra = palavra.replace(i, '?')
    return palavra


print(substituir(palavra))
