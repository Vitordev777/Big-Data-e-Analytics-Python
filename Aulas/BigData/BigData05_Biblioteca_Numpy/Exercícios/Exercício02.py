import numpy as np


# Criação de listas vazias para armazenar dados
nomes = []#Criando uma variável do tipo Lista vazia para receber os dados de nomes
idades = []
alturas = []
pesos = []

# Abrir e ler o arquivo CSV
with open(r'C:\Users\vitor\Downloads\dados1.csv', 'r', encoding = 'ISO-8859-1') as batata:
    lines = batata.readlines()


    for line in lines[1:]:  # Ignorar o cabeçalho
        nome, idade, altura, peso = line.strip().split(',')
        nomes.append(nome)
        idades.append(int(idade))
        alturas.append(int(altura))
        pesos.append(float(peso))


altura_maxima = np.max(alturas)
altura_maxima

alturas.index(altura_maxima)

print(nomes[9])

np_altura = np.array(alturas)
pessoas_190 = np.argwhere(alturas == altura_maxima)
pessoas_191 = np.count_nonzero(alturas == altura_maxima)

print(altura_maxima)
print(pessoas_190)
print(np.array(nomes)[pessoas_190])
print(pessoas_191)