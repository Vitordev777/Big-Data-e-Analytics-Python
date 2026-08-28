def criar_matriz(linhas, colunas):
  matriz = []
  for i in range(linhas):
      linha = [0] * colunas  # Preenche a linha com zeros, você pode alterar conforme necessário
      matriz.append(linha)
  return matriz

criar_matriz(5, 5)