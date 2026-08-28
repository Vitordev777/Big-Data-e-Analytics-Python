from google.colab import output

lista_de_compras = []
while True:
  menu = int(input(f'''
  ===================== Lista de compras =====================

              1 - Adicionar itens
              2 - Apagar itens
              3 - Listar itens
              4 - Sair

  '''))
  if menu == 1:
    while True:
      itens_adicionar = input("Digite o item:\n").upper()
      if itens_adicionar != "SAIR":
        lista_de_compras.append(itens_adicionar)
      else:
        break
      output.clear()
  elif menu == 2:
    for item in lista_de_compras:
      print(f"{lista_de_compras.index(item) + 1} - {item.title()} ")
    lista_de_compras.pop(int(input("Qual item você quer excluir?\n"))-1)
  elif menu == 3:
    for item in lista_de_compras:
      print(f"{lista_de_compras.index(item) + 1} - {item.title()} ")
  elif menu == 4:
    break