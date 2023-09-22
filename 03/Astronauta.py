# [3 - Repetição] Astronauta confuso

#funções úteis:

def coleta():
    entrada = input().slice(' ')
    totalCelulas = entrada[0]**2
    movimentos = entrada[1]
    return (totalCelulas, movimentos)

def caminhar(espacos, passos):
    msg = ''
    if(espacos < passos):
        pass
    elif(espacos == passos):
        pos = espacos/2 - 1
        msg = f'O astronauta está na posição: {pos, pos} \n'
    else: 
        msg = ' \n'
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
    msg1 = x
    msg2 = checarMissao(totEspacos, movimentos)
    print(msg1,msg2)

Oathbringer()