print('Jogo da concurso de beleza, cada jogador deve informar um numero,\n a media dos numeros informados será multiplicada\npelo valor fixo de 0,8, ganha o jogador que informar o numero mais proximo do produto.')

qtde_de_jogadores = int(input('Informe quantos jogadores vão participar (minimo 3/maximo 5): '))

while qtde_de_jogadores != 3 and qtde_de_jogadores != 4 and qtde_de_jogadores != 5:
    print('A quantidade de jogadores informada não é valida para o jogo, informe um numero de 3 a 5 jogadores')
    qtde_de_jogadores = int(input('Informe quantos jogadores vão participar (minimo 3/maximo 5): '))

if qtde_de_jogadores == 3:
    num1 = float(input('Informe o numero do primeiro jogador '))
    num2 = float(input('Informe o numero do segundo jogador '))
    num3 = float(input('Informe o numero do terceiro jogador '))
    media = (num1 + num2 + num3) / 3
    produto = media * 0.8
    
    print(f'O produto da media dos numeros x 0,8 é: {produto}')
    
    repp1 = num1 - produto
    if repp1 < 0:
        rep1 = repp1 * -1
    else:
        rep1 = repp1
    repp2 = num2 - produto
    if repp2 < 0:
        rep2 = repp2 * -1
    else:
        rep2 = repp2
    repp3 = num3 - produto
    if repp3 < 0:
        rep3 = repp3 * -1
    else:
        rep3 = repp3
    
    minimo = min(rep1 , rep2 , rep3)
    
    if minimo == rep1:
        print('O primeiro jogador venceu essa rodada!')
    elif minimo == rep2:
        print('O segundo jogador venceu essa rodada!')
    elif minimo == rep3:
        print('O terceiro jogador venceu essa rodada!')
    else:
        print('Nenhum jogador venceu essa rodada!')
   


elif qtde_de_jogadores == 4:
    num1 = float(input('Informe o numero do primeiro jogador '))
    num2 = float(input('Informe o numero do segundo jogador '))
    num3 = float(input('Informe o numero do terceiro jogador '))
    num4 = float(input('Informe o numero do quarto jogador '))
    media = (num1 + num2 + num3 + num4) / 4
    produto = media * 0.8
    
    print(f'O produto da media dos numeros x 0,8 é: {produto}')
    
    repp1 = num1 - produto
    if repp1 < 0:
        rep1 = repp1 * -1
    else:
        rep1 = repp1
    repp2 = num2 - produto
    if repp2 < 0:
        rep2 = repp2 * -1
    else:
        rep2 = repp2
    repp3 = num3 - produto
    if repp3 < 0:
        rep3 = repp3 * -1
    else:
        rep3 = repp3
    repp4 = num4 - produto
    if repp4 < 0:
        rep4 = repp4 * -1
    else:
        rep4 = repp4
   
    
    minimo = min(rep1 , rep2 , rep3 , rep4)
    
    if minimo == rep1:
        print('O primeiro jogador venceu essa rodada!')
    elif minimo == rep2:
        print('O segundo jogador venceu essa rodada!')
    elif minimo == rep3:
        print('O terceiro jogador venceu essa rodada!')
    elif minimo == rep4:
        print('O quarto jogador venceu essa rodada!')
    else:
        print('Nenhum jogador venceu essa rodada!')
   
   
        
        
elif qtde_de_jogadores == 5:
    num1 = float(input('Informe o numero do primeiro jogador '))
    num2 = float(input('Informe o numero do segundo jogador '))
    num3 = float(input('Informe o numero do terceiro jogador '))
    num4 = float(input('Informe o numero do quarto jogador '))
    num5 = float(input('Informe o numero do quinto jogador '))
    media = (num1 + num2 + num3 + num4 + num5) / 5
    produto = media * 0.8
    
    print(f'O produto da media dos numeros x 0,8 é: {produto}')
    
    repp1 = num1 - produto
    if repp1 < 0:
        rep1 = repp1 * -1
    else:
        rep1 = repp1
    repp2 = num2 - produto
    if repp2 < 0:
        rep2 = repp2 * -1
    else:
        rep2 = repp2
    repp3 = num3 - produto
    if repp3 < 0:
        rep3 = repp3 * -1
    else:
        rep3 = repp3
    repp4 = num4 - produto
    if repp4 < 0:
        rep4 = repp4 * -1
    else:
        rep4 = repp4
    repp5 = num5 - produto
    if repp5 < 0:
        rep5 = repp5 * -1
    else:
        rep5 = repp5
    
    minimo = min(rep1 , rep2 , rep3 , rep4 , rep5)
    
    if minimo == rep1:
        print('O primeiro jogador venceu essa rodada!')
    elif minimo == rep2:
        print('O segundo jogador venceu essa rodada!')
    elif minimo == rep3:
        print('O terceiro jogador venceu essa rodada!')
    elif minimo == rep4:
        print('O quarto jogador venceu essa rodada!')
    elif minimo == rep5:
        print('O quinto jogador venceu essa rodada!')
    else:
        print('Nenhum jogador venceu essa rodada!')
