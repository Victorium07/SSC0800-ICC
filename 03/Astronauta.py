# [3 - Repetição] Astronauta confuso

#funções úteis:

#coletando dados
def coleta():
    entrada = list(map(int,input().split(' ')))
    totalCelulas = entrada[0]**2
    movimentos = entrada[1]
    return (totalCelulas, movimentos, entrada[0])

#Devolve a mensagem com a posição do astronauta no sistema (coordenadas, se dentro da nave; mensagem padrão, se não)
def caminhar(espacos, passos, lado):
    msg = ''
    if(espacos < passos):
        pass
    elif(espacos == passos):
        pos = int(lado/2)
        msg = f'O astronauta está na posição: {pos, pos} \n'
    else: 
        pos_lin, pos_col = caminhoInverso(espacos, passos, lado)
        msg = f'O astronauta está na posição: {pos_lin, pos_col} \n'
    return msg

#Devolve a posição do astronauta caso esteja dentro da nave
def caminhoInverso(espacos, passos, lado):
    posInicial = int(lado/2)
    espacosRestantes = espacos - passos
    horizontal, vertical = calculoPassos(espacosRestantes)
    lin = posInicial + horizontal
    col = posInicial + vertical
    pos = (lin, col)
    return pos

#Devolve quantos passos em cada direção o astronauta deu em cada direção
def calculoPassos(espacosRestantes):
    fator = int(espacosRestantes/4)
    resto = espacosRestantes % 4

    esquerda = 0
    baixo = 0
    direita = 0
    cima = 0

    horizontal = direita - esquerda
    vertical = baixo - cima
    return (horizontal, vertical)

#Devolve mensagem sobre status da missão do astronauta
def checarMissao(espacos, passos):
    msg = ''
    if(espacos == passos):
        msg = 'Preste atencao, astronauta, chegou a sua vez!'
    elif(espacos < passos):
        msg = f'O astronauta ja saiu em missao ha {passos-espacos} chamadas.'
    else: msg = f'Ainda faltam {espacos-passos} chamadas para a sua vez!'
    return msg

#Chama a função completa
def Oathbringer():
    totEspacos, movimentos, lado = coleta()
    msg1 = caminhar(totEspacos, movimentos, lado)
    msg2 = checarMissao(totEspacos, movimentos)
    print(msg1,msg2)

Oathbringer()
