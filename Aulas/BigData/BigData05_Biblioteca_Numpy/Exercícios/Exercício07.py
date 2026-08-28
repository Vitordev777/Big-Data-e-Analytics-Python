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

np.idades = np.array(idades)
np.alturas = np.array(alturas)
np.nomes = np.array(nomes)
np.pesos = np.array(pesos)


min_idade = np.min(idades)
max_idade = np.max(idades)
print(max_idade - min_idade)

diferença = np.ptp(idades)
print(diferença)