from random import randint as rint
from google.colab import output
from time import sleep

soma_2 = 0
soma_3 = 0
soma_4 = 0
soma_5 = 0
soma_6 = 0
soma_7 = 0
soma_8 = 0
soma_9 = 0
soma_10 = 0
soma_11 = 0
soma_12 = 0

vezes = int(input('Digite o número de vezes que você quer jogar os dados:'))

for vez in range(vezes):

  dado_1 = rint(1,6)
  dado_2 = rint(1,6)

  if (dado_1 + dado_2) == 2:
    soma_2 += 1
  if (dado_1 + dado_2) == 3:
    soma_3 += 1
  if (dado_1 + dado_2) == 4:
    soma_4 += 1
  if (dado_1 + dado_2) == 5:
    soma_5 += 1
  if (dado_1 + dado_2) == 6:
    soma_6 += 1
  if (dado_1 + dado_2) == 7:
    soma_7 += 1
  if (dado_1 + dado_2) == 8:
    soma_8 += 1
  if (dado_1 + dado_2) == 9:
    soma_9 += 1
  if (dado_1 + dado_2) == 10:
    soma_10 += 1
  if (dado_1 + dado_2) == 11:
    soma_11 += 1
  if (dado_1 + dado_2) == 12:
    soma_12 += 1
else:
  print('2',soma_2)
  print('3',soma_3)
  print('4',soma_4)
  print('5',soma_5)
  print('6',soma_6)
  print('7',soma_7)
  print('8',soma_8)
  print('9',soma_9)
  print('10',soma_10)
  print('11',soma_11)
  print('12',soma_12)

print()
list_all = []

for soma in range(2,13):
  List = [(x,y) for x in range(1,7) for y in range(1,7) if x + y == soma]
  list_all.append(List)

for i in list_all:
  print(i)