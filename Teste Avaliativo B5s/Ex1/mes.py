# A função recebe um inteiro entre 1 e 12 e retorna o mês correspondente por extenso. Caso o mês informado não esteja entre 1 e 12, deverá ser retornado "Mes Inexistente"


mes = int(input('digite o numero do mês desejado: '))


def mesCorrespondente(mes):
    nomemes = ''
    if mes == 1:
        nomemes = 'janeiro'
    elif mes == 2:
        nomesmes = 'fevereiro'
    elif mes == 3:
        nomemes = 'março'
    elif mes == 4:
        nomemes = 'abril'
    elif mes == 5:
        nomemes = 'maio'
    elif mes == 6:
        nomemes = 'junho'
    elif mes == 7:
        nomemes = 'julho'
    elif mes == 8:
        nomemes = 'agosto'
    elif mes == 9:
        nomemes = 'setembro'
    elif mes == 10:
        nomemes = 'outubro'
    elif mes == 11:
        nomemes = 'novembro'
    elif mes == 12:
        nomemes = 'dezembro'
    else:
        nomemes = 'mês desconhecido'
    return nomemes


mes = mesCorrespondente(mes)

print(f'mês: {mes}')
