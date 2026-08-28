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

# Convertendo TODAS as listas para arrays NumPy
np_nomes = np.array(nomes)
np_idades = np.array(idades)
np_alturas = np.array(alturas)
np_pesos = np.array(pesos)

# ---- SOLUÇÃO 1: Usando Máscara Booleana (Método mais rápido e limpo) ----
# Cria uma condição: onde o peso for menor que 70
filtro_peso = np_pesos < 70

# Aplica o filtro no array de idades e calcula a média diretamente
media_idade_peso_70 = np_idades[filtro_peso].mean()
print(f"Média de idade de quem pesa < 70kg: {media_idade_peso_70:.2f}")


# ---- SOLUÇÃO 2: Usando np.where (O que você tentou fazer) ----
# np.where retorna os índices onde a condição é verdadeira
indices_peso_70 = np.where(np_pesos < 70)

# Usa esses índices para puxar as idades e tirar a média
media_com_where = np_idades[indices_peso_70].mean()
print(f"Média de idade (usando np.where): {media_com_where:.2f}")
