# [3 - Repetição] Astronauta confuso

#funções úteis:

def coleta():
    entrada = input().slice(' ')
    totalCelulas = entrada[0]**2
    movimentos = entrada[1]
    return (totalCelulas, movimentos)

def caminhoInverso(espacos, passos):
    posInicial = espacos/2 - 1
    esquerda = 0
    direita = 0
    baixo = 0
    cima = 0
    for i in range(espacos):
        direcao = i%4
        if(direcao == 0):
            esquerda += x
        elif(direcao == 1):
            baixo += x
        elif(direcao == 2):
            direita += x+1
        else: cima += x+1
    lin = posInicial + esquerda - direita 
    col = posInicial + baixo - cima
    pos = (lin, col)
    return pos





def caminhar(espacos, passos):
    msg = ''
    if(espacos < passos):
        pass
    elif(espacos == passos):
        pos = espacos/2 - 1
        msg = f'O astronauta está na posição: {pos, pos} \n'
    else: 
        pos_lin, pos_col = caminhoInverso(espacos, passos)
        msg = f'O astronauta está na posição: {pos_lin, pos_col} \n'
    return msg


def checarMissao(espacos, passos):
    msg = ''
    if(espacos == passos):
        msg = 'Preste atencao, astronauta, chegou a sua vez!'
    elif(espacos < passos):
        msg = f'O astronauta ja saiu em missao ha {passos-espacos} chamadas.'
    else: msg = f'Ainda faltam {espacos-passos} chamadas para a sua vez!'
    return msg

def Oathbringer():
    totEspacos, movimentos = coleta()
    msg1 = caminhar(totEspacos, movimentos)
    msg2 = checarMissao(totEspacos, movimentos)
    print(msg1,msg2)

Oathbringer()
