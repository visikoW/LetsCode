"""
Questão 7.
Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
euclidiana entre os pontos, utilizando a equação abaixo:
𝑑 = raiz((𝑥2 − 𝑥1)² + (𝑦2 − 𝑦1)²)
"""

def d(x1: float, y1: float, x2: float, y2: float) -> float:
    """Retorna a raiz quadrada de (x2 - x1)² + (y2 - y1)²"""
    calcular = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    return calcular

print(d(2, 5, 6, 9))