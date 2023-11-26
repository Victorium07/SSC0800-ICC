# [5 - Funções] Simulação de Partículas - PESO 2x

#biblitecas úteis:
import copy

#funções úteis:
## funções de processamento de entrada:
def entrada_frames() -> int:
    n_frames = int(input())
    return n_frames

def entrada_blocos() -> list:
    novo_bloco = input().split()
    frame = novo_bloco[0]
    novo_bloco[0] = frame[:-1]
    for i in range(0,3):
        novo_bloco[i] = int(novo_bloco[i])
    return novo_bloco

def check_novo_bloco(_total_frames):
        try:
            novo_bloco = entrada_blocos()
            return novo_bloco

        except EOFError:
            return _total_frames+1


## funções de atualização de quadro:
def gerador_quadro_inicial(_tuple:tuple) -> list:
    quadro = [' ' * _tuple[1] for _ in range(_tuple[0])]
    return quadro

def adicionar_elemento(quadro_antigo: list, _lista_entradas: list) -> list:
    quadro_novo = copy.deepcopy(quadro_antigo)
    coordenadas_entrada = _lista_entradas[0:2]
    limites = pegar_limites(quadro_novo)
    if(checar_limites(coordenadas_entrada, limites)):
        quadro_novo[_lista_entradas[0]][_lista_entradas[1]] = _lista_entradas[2]
        return quadro_novo
    else: return False

def pegar_limites(_quadro: list) -> tuple:
    lim_linhas = len(_quadro[0])
    lim_colunas = len(_quadro[1])
    limites = (lim_linhas, lim_colunas)
    return limites

def checar_limites(_coords: list, _limites: tuple) -> bool:
    if(_coords[0]+1 > _limites[0]-1): return False
    elif(_coords[1]+1 >_limites[1]-1): return False
    else: return True

def checar_limite_linear(_coord: int, _limite: int) -> bool:
    if(_coord > _limite): return False
    else: return True

def atualizar_quadro_atual(_quadro: list) -> list:
    _linhas = len(_quadro[0])
    _colunas = len(_quadro[1])
    for _linha in range(_linhas):
        for _coluna in range(colunas):
            elem = _quadro[_coluna][_linha]
            coords = [_linha, _coluna]
            mover_elemento(_quadro, elem, coords)
    return 0

def imprimir_quadro_atual(_quadro: list, _frame: int) -> bool:
    _colunas = len(_quadro[1])
    _linhas = len(_quadro[0])
    print(f'frame: {_frame}')
    for _coluna in range(_colunas):
        for _linha in range(_linhas):
            print(_quadro[_coluna][_linha], end='')
        print()
    return 0

## funções de física:
# finalizar função
def mover_elemento(_quadro: list, elemento: str, _coords: list) -> list:
    linha = _coords[0]
    coluna = _coords[1]
    limites = pegar_limites(_quadro)
    lim_linha = limites[0]
    lim_coluna = limites[1]
    if(check_ar(_quadro[coluna][linha])):
        return 0
    elif(check_areia(_quadro[coluna][linha])):
        #check se tem espaço para baixo, caso negativo: areia não se move.
        if(checar_limite_linear(linha+1, lim_linha)):
            return 0
        # mover areia
        mover_areia()
    else: 
        #check se tem espaço para baixo, caso negativo: aǵua se move apenas para os lados.
        if(checar_limite_linear(linha+1, lim_linha)):
            continue
        if(checar_limite_linear(coluna-1, lim_coluna)):
            continue
        if(checar_limite_linear(coluna+1, lim_coluna)):
            return 0
        

def mover_areia(_quadro: list, _linha: int, _coluna: int) -> list:
    if(check_areia(_quadro[_coluna][_linha+1]) == False):
        _quadro[_coluna][_linha], _quadro[_coluna][_linha+1] == _quadro[_coluna][_linha+1], _quadro[_coluna][_linha]
        return 0
    elif(check_areia(_quadro[coluna-1][linha+1]) == False):
        _quadro[_coluna][_linha], _quadro[_coluna-1][_linha+1] == _quadro[_coluna-1][_linha+1], _quadro[_coluna][_linha]
        return 0
    elif(check_areia(_quadro[coluna+1][linha+1]) == False):
        _quadro[_coluna][_linha], _quadro[_coluna+1][_linha+1] == _quadro[_coluna+1][_linha+1], _quadro[_coluna][_linha]
        return 0
    else: return 0

def check_ar(elemento: str) -> bool:
    if(elemento == ''): return True
    else: return False

def check_areia(elemento: str) -> bool:
    if(elemento == '#'): return True
    else: return False


def WindAndTurth():
    total_frames = entrada_frames()
    lins = 32
    cols = 64
    dimesao_inicial = (lins, cols)
    quadro_atual = gerador_quadro_inicial(dimesao_inicial)
    frame_anterior = 0
    while frame_atual =< total_frames:
        infos_novo_bloco = check_novo_bloco()
        frame_atual = infos_novo_bloco[0]
        coords_elemento = infos_novo_bloco[1:len(infos_novo_bloco)-1]
        novo_quadro = adicionar_elemento(quadro_atual, coords_elemento)
        if(novo_quadro = 0):
            break
        if(frame_atual > frame_anterior):
           frame_anterior = frame_atual
           #ativar física
           #printar quadro
           pass 

        
