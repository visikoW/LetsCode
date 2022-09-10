"""
Questão 6.
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
"""

def criar_lista(quantidade):
    i = 0
    lista = []
    while i < quantidade:
        numero = float(input('Digie um número: '))
        lista.append(numero)
        i += 1
    return sum(lista)

nova_lista = criar_lista(int(input('Digite a quantidade de elementos: ')))

print(nova_lista)