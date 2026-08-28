import numpy as np

nomes = []
idades = []
alturas = []
pesos = []

with open(r'C:\Users\vitor\Downloads\dados1.csv', 'r', encoding='ISO-8859-1') as batata:
    lines = batata.readlines()

    for line in lines[1:]:  # Ignorar o cabeçalho
        nome, idade, altura, peso = line.strip().split(',')
        nomes.append(nome)
        idades.append(int(idade))
        alturas.append(int(altura))
        pesos.append(float(peso))

nomes_nd = np.array(nomes)
alturas_nd = np.array(alturas)

#Quais são os nomes das pessoas com altura acima de 170 cm?

nomes_acima_170 = nomes_nd[alturas_nd > 170]
print("Pessoas com mais de 170cm:", nomes_acima_170)
