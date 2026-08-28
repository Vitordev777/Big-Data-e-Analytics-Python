import numpy as np

nomes = []
idades = []
alturas = []
pesos = []

# Abrir e ler o arquivo CSV
with open(r'C:\Users\vitor\Downloads\dados1.csv', 'r', encoding='ISO-8859-1') as batata:
    lines = batata.readlines()

    for line in lines[1:]:  # Ignorar o cabeçalho
        linha_limpa = line.strip()
        if not linha_limpa:
            continue
        nome, idade, altura, peso = linha_limpa.split(',')
        nomes.append(nome)
        idades.append(int(idade))
        alturas.append(int(altura))
        pesos.append(float(peso))

# 1. Transforma a lista de idades em um array do NumPy
np_idades = np.array(idades)

# 2. Faz a conta e conta os elementos que não têm resto 0
idades_impar = np.count_nonzero((np_idades % 2) != 0)

print(f"Quantidade de idades ímpares: {idades_impar}")
