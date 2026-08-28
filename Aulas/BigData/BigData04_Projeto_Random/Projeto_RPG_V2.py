from google.colab import output
from time import sleep
from random import randint


niveis_dificuldade = ['Easy','Normal','hard']
nivel_dificuldade = niveis_dificuldade[0]
hp_user = 100
atk_user = [1,3]

def menu():
  global nivel_dificuldade
  while True:
    menu = input('''

  ==================== Bem Vindo ao RPG ====================

  1 - Iniciar
  2 - Configurar
  3 - Sair


    ''')
    if menu == '1':
      output.clear()
      print("Caregando...")
      sleep(4)
      output.clear()
      break
    if menu == '2':
      output.clear()
      sleep(2)
      config = input(f'''

      ======================== Configuração ========================

      1 - Alterar Nivel de Dificuldade
      2 - Sair

      ''')
      output.clear()
      print('Carregando...')
      sleep(4)
      if config == '1':
        escolha_config = input(f'''

        Nivel de dificuldade - {nivel_dificuldade}
        Qual nivel de dificuldade deseja?
        1 - {niveis_dificuldade[0]}
        2 - {niveis_dificuldade[1]}
        3 - {niveis_dificuldade[2]}
        ''')
        if escolha_config == '1':
          nivel_dificuldade = niveis_dificuldade[0]
        if escolha_config == '2':
          nivel_dificuldade = niveis_dificuldade[1]
        if escolha_config == '3':
          nivel_dificuldade = niveis_dificuldade[2]
          output.clear()
          print('configurando...')
          continue
    if menu == '3':
      print('Até logo!')
      output.clear()
      break


def cadastro():
  global nome_usuario
  nome_usuario = input('''

  Qual o nome do aventureiro?

  ''')
  iniciar = input(f'''

  {nome_usuario} está pronto para começar?
  1 - Sim
  2 - Não

  ''').upper
  if iniciar == '1':
    output.clear()
    print('Iniciando...')
    sleep(4)
  elif iniciar == '2':
    menu()



def level_one():

  global hp_user
  global atk_user
  global hp_pc
  global atk_pc

  if nivel_dificuldade == 'Easy':
    hp_pc = 5
    atk_pc = [1,3]
  if nivel_dificuldade == 'Normal':
    hp_pc = 10
    atk_pc = [1,5]
  if nivel_dificuldade == 'Hard':
    hp_pc = 15
    atk_pc = [1,10]

  while True:
    rodada = 1
    menu = input(f'''

  ==================== Level 1 ====================
  Rodada : {rodada}
  User: {nome_usuario}
  Seu HP : {hp_user:.2f}
  HP Monstro: {hp_pc}


  Escolha entre Atacar ou Curar:
  ''').upper()
    if menu == 'ATACAR':
      dano_user = randint(atk_user[0],atk_user[1])
      dano_pc = randint(atk_pc[0],atk_pc[1])
      hp_pc -= dano_user
      hp_user -= dano_pc
      print(f'Dano causado na rodada {rodada}: {dano_user}')
      print(f'Dano recebido na rodada {rodada}: {dano_pc}')
    if menu == 'CURAR':
      if hp_user <= 100:
        cura_user = (randint(atk_user[0],atk_user[1])) * 0.6
        dano_pc = randint(atk_pc[0],atk_pc[1])
        hp_user += cura_user
        hp_user -= dano_pc
        print(f'Cura recebida na rodada {rodada}: {cura_user}')
        print(f'Dano recebido na rodada {rodada}: {dano_pc}')

    if hp_pc <= 0:
      sleep(4)
      output.clear()
      print('Você Derrotou o monstro!')
      break
    sleep(3)
    output.clear()
    rodada += 1



menu()
cadastro()
level_one()