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

#Quem é a pessoa cuja altura está mais próxima da média (175 cm)?

diferenca = np.abs(alturas_nd - 175)
diferenca

menor_diferenca = np.min(diferenca)
menor_diferenca

indices_mais_proximos = np.count_nonzero(diferenca == menor_diferenca)
indices_mais_proximos

indices_mais_proximos = np.where(diferenca == menor_diferenca)
indices_mais_proximos

valores_mais_proximos = alturas_nd[indices_mais_proximos]
valores_mais_proximos

pessoas_175 = nomes_nd[indices_mais_proximos]
print(pessoas_175)