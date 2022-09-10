"""
Questão 4.
Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.
"""

primeiro_numero = int(input('Digite o primeiro número inteiro: '))
segundo_numero = int(input('Digite o segundo número inteiro: '))
terceiro_numero = float(input('Digite o terceiro número flutuante: '))

# a) o produto entre o dobro do primeiro e a metade do segundo.
calculo_a = (primeiro_numero * 2) * (segundo_numero / 2)
print(calculo_a)

# b) a soma entre o triplo do primeiro e o terceiro.
calculo_b = (primeiro_numero * 3) + terceiro_numero
print(calculo_b)

# c) o terceiro elevado ao cubo.
calculo_c = terceiro_numero ** 3
print(calculo_c)