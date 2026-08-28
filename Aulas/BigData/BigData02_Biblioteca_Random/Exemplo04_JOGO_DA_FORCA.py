palavra_secreta = input('Digite a palavra secreta ').upper()


chutes = ''

tentativas = 10
for tentativa in range(tentativas):
  output.clear()
  print(f'Você tem {(tentativas+1)-(tentativa+1)} tentativas')
  palavra_jogo =''
  for letra in palavra_secreta:

    if letra in chutes:
      palavra_jogo = palavra_jogo + letra
    elif letra == '-':
      palavra_jogo = palavra_jogo + letra
    elif letra == "'":
      palavra_jogo = palavra_jogo + letra
    else:
      palavra_jogo = palavra_jogo + "_ "
  print(palavra_jogo)


  chute = input('Digite uma letra ou chute uma palavra,\nSabendo que se errar a palavra você perde o jogo!!!!\n').upper()
  if chute in chutes:
    sleep(4)
    print('Você ja digitou esta letra!!')
    print('Carregando... ')
    sleep(4)
    tentativas += 1
    continue
  if chute == 'PALAVRA':
    chute = input('Digite a palavra que você imagina ser:').upper()
    if chute == palavra_secreta:
      print('Parabéns você acertou!!!')
      break
    else:
      print('Você perdeu')
      break
  elif len(chute) >1:

    print('Chute inválido ')
    print('Carregando... ')
    sleep(4)
    tentativas += 1
    continue


  chutes += chute