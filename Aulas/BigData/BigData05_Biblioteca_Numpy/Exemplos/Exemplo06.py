# Defina as dimensões da matriz tridimensional
dimensao1 = 3
dimensao2 = 4
dimensao3 = 5

# Crie uma matriz tridimensional preenchida com zeros
matriz_3d_zeros = [[[0 for _ in range(dimensao3)] for _ in range(dimensao2)] for _ in range(dimensao1)]

# Crie uma matriz tridimensional com valores aleatórios (usando list comprehension)
import random
matriz_3d_aleatoria = [[[random.random() for _ in range(dimensao3)] for _ in range(dimensao2)] for _ in range(dimensao1)]

# Exiba as matrizes
print("Matriz Tridimensional de Zeros:")
for i in range(dimensao1):
    for j in range(dimensao2):
        print(matriz_3d_zeros[i][j])
    print()

print("\nMatriz Tridimensional Aleatória:")
for i in range(dimensao1):
    for j in range(dimensao2):
        print(matriz_3d_aleatoria[i][j])
    print()