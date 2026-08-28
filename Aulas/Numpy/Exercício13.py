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

#Qual é a idade média das pessoas com peso abaixo de 70 kg?

pesos_abaixo_70 = np.where(pesos_nd < 70)
media_abaixo_70 = (idades_nd[pesos_abaixo_70]).mean()
media_abaixo_70

media_abaixo_70 = np.mean(idades_nd[pesos_abaixo_70])
print(media_abaixo_70)