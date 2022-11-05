# Descubra o número do cartão de crédito abaixo sabendo que o mesmo é um multiplo de 123457 e o digito de luhn é válido.
# * O Número do cartão deve ter o seguinte padrão: 543210******1234
numMin = '000000'
numMax = '999999'
inicio = '543210'
fim = '1234'
inteiro = ''


def luhn(n):
    sum = 0
    alt = 0
    i = len(n) - 1
    num = 0
    while i >= 0:
        num = int(n[i])
        if alt:
            num = num * 2
            if num > 9:
                num = (num % 10) + 1
        sum = sum + num
        alt = not alt
        i -= 1
    return sum % 10 == 0


for i in range(int(numMin), int(numMax)):
    num = i
    inteiro = inicio + str(num) + fim
    if int(inteiro) % 123457 == 0:
        if luhn(inteiro):
            print(inteiro)
