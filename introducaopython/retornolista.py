# Faça um código onde receba uma lista de elementos e retorno uma lista de elementos sendo eles
# os primeiros pares e os ultimos impares

def par_impar(lista):
    retorno = []
    for x in lista:
        if x%2 == 0:
            retorno.append(x)
        else:
            retorno.insert(0, x)
    return retorno

lista = [5, 4, 7, 1, 7, 3, 1, 8, 6, 7, 4]

resultado = par_impar(lista)

print(resultado)