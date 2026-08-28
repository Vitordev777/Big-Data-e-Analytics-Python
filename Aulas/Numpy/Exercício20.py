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

#Quantas pessoas têm idade entre 25 e 30 anos e altura abaixo de 170 cm?

pessoas_25_30 = np.count_nonzero(np.logical_and(idades_nd >= 25,idades_nd <=30, alturas_nd < 170))
print(pessoas_25_30)