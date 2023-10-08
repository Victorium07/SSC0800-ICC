# [3 - Repetição] Astronauta confuso

import math

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
        if(lado%2 == 0):
            msg = f'O astronauta está na posição: {pos+1, pos} \n'
        else:
            msg = f'O astronauta está na posição: {pos, pos} \n'
    else: 
        pos_lin, pos_col = inverterCaminho(espacos, passos, lado)
        msg = f'O astronauta está na posição: {pos_lin, pos_col} \n'
    return msg

#Devolve a posição do astronauta caso esteja dentro da nave
def inverterCaminho(espacos, passos, lado):
    posInicial = int(lado/2)
    espacosRestantes = espacos - passos
    horizontal, vertical = calcularPassos(espacosRestantes, lado)
    if(lado%2 == 0):
        lin = posInicial + 1 + vertical
    else:
        lin = posInicial + vertical
    col = posInicial + horizontal
    pos = (lin, col)
    return pos

#Devolve quantos passos em cada direção o astronauta deu em cada direção
def calcularPassos(espacosRestantes, lado):
    limInferior = int(math.sqrt(espacosRestantes))
    limInferiorQuadrado = int(limInferior**2)
    casasFinais = espacosRestantes - limInferiorQuadrado

    adjVerticalCompleta = (int(limInferior/2) + 1)
    verticalIncompleta = sum([1 for i in range(1, limInferior+1) if i <= casasFinais])
    adjHorizontalIncompleta = casasFinais - verticalIncompleta

    if(lado%2 == 0):
        if(limInferior%2 == 0):
            esquerda = horizontalCompleta(2, limInferior)
            cima = esquerda - adjVerticalCompleta
            baixo = esquerda - limInferior + verticalIncompleta
            direita = cima + adjHorizontalIncompleta

        else:
            direita = horizontalCompleta(1, limInferior)
            baixo = direita - adjVerticalCompleta
            cima = direita - limInferior + verticalIncompleta
            esquerda = baixo + adjHorizontalIncompleta
    
    else:
        if(limInferior%2 == 0):
            direita = horizontalCompleta(2, limInferior)
            baixo = direita - adjVerticalCompleta
            cima = direita - limInferior + verticalIncompleta
            esquerda = baixo + adjHorizontalIncompleta

        else:
            esquerda = horizontalCompleta(1, limInferior)
            cima = esquerda - adjVerticalCompleta
            baixo = esquerda - limInferior + verticalIncompleta
            direita = cima + adjHorizontalIncompleta
    
    h = direita - esquerda
    v = baixo - cima
    return (h, v)

def horizontalCompleta(comeco, final):
    return sum([i for i in range(comeco, final+2, 2)])
    

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
