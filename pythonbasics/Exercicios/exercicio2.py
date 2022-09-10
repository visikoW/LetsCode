"""
Questão 2.
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
alguns exemplo abaixo:
💡 Entrada: 25.01 | Saída: (25,50]
Entrada: 25.00 | Saída: [0,25]
Entrada: 100.00 | Saída: (75,100]
Entrada: -25.02 | Saída: Fora de intervalo
📌 Lembrando que o [ ou ] representa que o valor está contido no intervalo, enquanto o ( ou
) representa que o valor associado não está contido no intervalo. Em outras palavras, (75, 100]
representa o intervalo que vai de maior que 75 (não incluindo o 75) até menor ou igual 100.
"""

valor = float(input('Digite um número: '))

intervalo_0 = '[0,25]'
intervalo_1 = '(25,50]'
intervalo_2 = '(50,75]'
intervalo_3 = '(75,100]'

if valor >= 0 and valor <= 25:
    print(intervalo_0)
elif valor > 25 and valor <= 50:
    print(intervalo_1)
elif valor > 50 and valor <= 75:
    print(intervalo_2)
elif valor > 75 and valor <= 100:
    print(intervalo_3)
else:
    print('Fora do intervalod')