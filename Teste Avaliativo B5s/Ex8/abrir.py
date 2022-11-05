arquivo = open('Ex8\data.dat', 'r')

cond1 = 0
for arquivo in arquivo.readlines():

    dado = arquivo.split()
    for i, dado in enumerate(dado):
        zeros = dado.count('0')
        uns = dado.count('1')
        if zeros % 3 == 0 or uns % 2 == 0:
            cond1 += 1

print(cond1)
