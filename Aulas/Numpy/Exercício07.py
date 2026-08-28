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

#Qual é o Índice de Massa Corporal (IMC) médio das pessoas?
imc_nd = np.array([pesos_nd[i] /
                   ((alturas_nd[i]/100)**2) for i in range(len(nomes_nd))])
imc_nd

imc_nd = np.array([pesos_nd / ((alturas_nd/100)**2)])
imc_nd

# def calcula_imc(peso,altura):
#   imc_1 = np.array([peso / ((altura/100)**2)])
#   return imc_1

# imc_aluno = calcula_imc(80,170)
# imc_aluno

imc = []

for i in range(len(nomes_nd)):

    resultado = pesos_nd[i] /((alturas_nd[i]/100)**2)
    imc.append(resultado)

print(imc)