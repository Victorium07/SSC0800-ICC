# [3 - Repetição] Astronauta confuso

#funções úteis:


def coleta():
    entrada = input().slice(' ')
    totalCelulas = entrada[0]**2
    movimentos = entrada[1]
    return (totalCelulas, movimentos)

def caminhar(totEspacos):
    pass


def checarMissao(espacos, passos):
    msg = ''
    if(espacos == passos):
        msg = '\nPreste atencao, astronauta, chegou a sua vez!'
    elif(espacos < passos):
        msg = f'O astronauta ja saiu em missao ha {passos-espacos} chamadas.'
    else: msg = f'\nAinda faltam {espacos-passos} chamadas para a sua vez!'
    return msg

def Oathbringer():
    totEspacos, movimentos = coleta()
    msg1 = x
    msg2 = checarMissao(totEspacos, movimentos)