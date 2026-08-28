import random
from google.colab import output
from time import sleep


print('''
         Configuração do jogo RPG Digite abaixo as configurações desejadas!
''')

vida_jogador = int(input("Qual a vida do jogador ?"))
vida_pc = int(input("Qual a vida do computador ?"))
min_dano = int(input("Qual o minimo de dano ?"))
max_dano = int(input("Qual o máximo de dano ?"))

print('\nCaregando...')

sleep(5)
output.clear()


while True:

  dano_jogador = ''
  dano_causado_jogador = ''
  dano_pc =''
  dano_causado_pc = ''

  menu = input(f'''
          Bem vindo ao RPG, escolha entre "Soco" e "Cabeçada" para atacar o inimigo,
          ou Sair para fugir.  ^.^
          Boa sorte!!!!
          HP jogador {vida_jogador}
          HP PC      {vida_pc}
  ''').upper()

  if menu == 'SAIR':
    print('Você fugiu ')
    break
  elif menu == 'SOCO':
    dano_jogador = random.randint(min_dano,max_dano)
    print(f'Você escolheu "SOCO" seu poder de ataque foi {dano_jogador}')
  elif menu == 'CABEÇADA':
    dano_jogador = max_dano * 0.65
    print(f'Você escolheu "CABEÇADA" seu poder de ataque foi {dano_jogador}')

  dano_pc = random.randint(min_dano,max_dano)
  print(f'O computador deu um soco o poder de ataque é {dano_pc}')

  if dano_jogador > dano_pc:
    print('Seu dano é maior, você ataca...')
    if menu == 'SOCO':
      dano_causado_pc = random.randint(min_dano,max_dano)
      vida_pc -= dano_causado_pc
      print(f'Seu soco deu {dano_causado_pc} de dano ao PC')

    elif menu == 'CABEÇADA':
      vida_pc -= max_dano * 0.45
      vida_jogador -= max_dano * 0.13
      print(f'Sua cabeçada deu {3} de dano ao PC')

  elif dano_jogador == dano_pc:
    print('Empate ')
    continue
  else:
    dano_causado_jogador = random.randint(min_dano,max_dano)
    vida_jogador -= dano_causado_jogador
    print(f'O soco do PC te causa {dano_causado_jogador} de dano')

  if vida_jogador <= 0:
    print('Você perdeu, seu HP foi a zero')
    break
  elif vida_pc <= 0:
    print('Você derrotou o PC, levando o hp dele a 0')
    break
  sleep(6)
  output.clear()