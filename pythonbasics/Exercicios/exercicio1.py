"""
Questão 1.
Faça um programa que peça ao usuário um número e imprima todos os números de um até o
número que o usuário informar.
💡 Exemplo:
Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4 5
"""

def decrescente(number):
    numero = 0

    for x in range(number):
        if numero != number:
            numero += 1
            print(numero, end = ' ')

# Resultado
numero = int(input('Por favor, digite um número: '))
resultado = decrescente(numero)
