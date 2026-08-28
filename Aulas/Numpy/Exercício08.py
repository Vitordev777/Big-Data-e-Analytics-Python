import numpy as np
# Criação de listas vazias para armazenar dados
nomes = []#Criando uma variável do tipo Lista vazia para receber os dados de nomes
idades = []
alturas = []
pesos = []

# Abrir e ler o arquivo CSV
with open(r'C:\Users\vitor\Downloads\dados1.csv', 'r', encoding = 'ISO-8859-1') as batata:#
    lines = batata.readlines()


    for line in lines[1:]:  # Ignorar o cabeçalho
        nome, idade, altura, peso = line.strip().split(',')
        nomes.append(nome)
        idades.append(int(idade))
        alturas.append(int(altura))
        pesos.append(float(peso))


nomes_nd = np.array(nomes)
idades_nd = np.array(idades)
alturas_nd = np.array(alturas)
pesos_nd = np.array(pesos)

#Qual é a diferença de idade entre a pessoa mais nova e a mais velha?
idade_maxima = np.max(idades_nd)
idade_minima = np.min(idades_nd)
print(idade_minima)
print(idade_maxima)
diferenca = idade_maxima-idade_minima
print(diferenca)


diferenca_2 = np.ptp(idades)
print(diferenca_2)