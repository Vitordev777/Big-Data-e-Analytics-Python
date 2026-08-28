nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

qtd_nome = len(nome)
ano_n = 2023 - idade
imc = peso / (altura*altura)

print(f"Seu  nome é {nome} e tem {qtd_nome} caracteres, você tem {idade} anos e nasceu em {ano_n}. Você mede {altura} cm, pessa {peso}Kg e seu imc é: {imc:.2f}")