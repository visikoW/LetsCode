"""
Questão 5.
Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
sim ou não:
1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
você vai informar como a polícia o considera.
"""

def teste_sus(resposta_pergunta):
    if resposta_pergunta == 'y':
        return 1
    return 0

def pontuacao():
    soma = 0
    print('Digite sendo "y" ou "n" para as respostas')

    soma += teste_sus(input('Mora perto da vítima? '))
    soma += teste_sus(input('Já trabalhou com a vítima? '))
    soma += teste_sus(input('Telefonou para a vítima? '))
    soma += teste_sus(input('Esteve no local do crime? '))
    soma += teste_sus(input('Devia para a vítima? '))

    return soma

interrogado = pontuacao()

if interrogado < 2:
    print('Liberado')
elif interrogado < 3:
    print('Suspeito')
elif interrogado >= 3 and interrogado <= 4:
    print('Cumplice')
elif interrogado <= 5:
    print('Assassino')