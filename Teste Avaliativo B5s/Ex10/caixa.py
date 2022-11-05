# A função será utilizada em um sistema de caixa.
# Ela receberá um valor inteiro, representando o valor a ser sacado e um array contendo quais tipos de cédulas ela tem disponível.
# O array de cédulas disponiveis indica quais valores de cédulas existirão no caixa, a quantidade das mesmas é ilimitada. No caso do input [2,5,50], o caixa terá quantidades ilimitadas de notas de 2, 5 e 50 para devolver ao cliente.
# A função deverá retornar o mínimo de cédulas necessarias possivel para o saque em formato de um array, cuja chave seja o valor da cédula e o valor a quantidade daquela cédula que será sacada.

saque = int(input('qual o valor da retirada?  '))


cem = int(saque / 100)
saque = saque - (cem*100)

cinquenta = int(saque/50)
saque = saque - (cinquenta*50)

dez = int(saque/10)
saque = saque - (dez*10)

cinco = int(saque/5)
saque = saque - (cinco*5)

dois = saque/2

print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 10,00 = ', dez)
print('Notas R$ 5,00 = ', cinco)
print('Notas R$ 2,00 = ', dois)
