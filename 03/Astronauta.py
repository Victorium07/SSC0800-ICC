# [3 - Repetição] Astronauta confuso

#funções úteis:

def coleta():
    entrada = list(map(int,input().split(' ')))
    totalCelulas = entrada[0]**2
    movimentos = entrada[1]
    return (totalCelulas, movimentos, entrada[0])

def caminhoInverso(espacos, passos, lado):
    posInicial = int(lado/2)
    esquerda = 0
    direita = 0
    baixo = 0
    cima = 0
    contador = 1
    for i in range(espacos - passos):
        direcao = i%4
        if(direcao == 0):
            esquerda += contador
        elif(direcao == 1):
            baixo += contador
            contador +=1
        elif(direcao == 2):
            direita += contador
        else: 
            cima += contador
            contador +=1

    lin = posInicial - esquerda + direita 
    col = posInicial + baixo - cima
    pos = (lin, col)
    return pos

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


def checarMissao(espacos, passos):
    msg = ''
    if(espacos == passos):
        msg = 'Preste atencao, astronauta, chegou a sua vez!'
    elif(espacos < passos):
        msg = f'O astronauta ja saiu em missao ha {passos-espacos} chamadas.'
    else: msg = f'Ainda faltam {espacos-passos} chamadas para a sua vez!'
    return msg

def Oathbringer():
    totEspacos, movimentos, lado = coleta()
    msg1 = caminhar(totEspacos, movimentos, lado)
    msg2 = checarMissao(totEspacos, movimentos)
    print(msg1,msg2)

Oathbringer()
