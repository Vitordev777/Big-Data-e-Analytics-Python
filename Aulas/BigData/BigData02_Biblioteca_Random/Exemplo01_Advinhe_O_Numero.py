from random import randint as rint
from google.colab import output
from time import sleep
numero = rint(1,10000)

chances = 10
chute = ''
for chance in range(chances):
  if chute == True:
    print('Sua escolha é maior que o número ')
  elif chute == False:
    print('Sua escolha é menor que o número ')

  # print(numero)
  print(f'Você tem {(chances+1)-(chance+1)} tentativas')
  escolha = int(input('Digite um número de 1 a 10000 \n '))

  if escolha == numero:
    print(f'Parabéns você acertou!!!!!! O número era {numero}')
    break
  elif escolha > numero:
    chute = True
  else:
    chute = False
  output.clear()
else:
  print('Suas tentativas acabaram. ;/ Você perdeu!!!!!')