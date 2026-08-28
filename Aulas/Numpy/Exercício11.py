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

# Quantas pessoas têm IMC acima de 25 (indicando sobrepeso)?

imc_nd = np.array([pesos_nd[i] /
                   ((alturas_nd[i]/100)**2) for i in range(len(nomes_nd))])
imc_nd
imc_nd = np.array([pesos_nd / ((alturas_nd/100)**2)])

imc_25 = np.count_nonzero(imc_nd >=25)
imc_25