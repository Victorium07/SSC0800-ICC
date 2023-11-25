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

def check_ar(elemento: str) -> bool:
    if(elemento == ''): return True
    else: return False

def check_areia(elemento: str) -> bool:
    if(elemento == '#'): return True
    else: return False

def checar_limites(_coords: list, _limites: tuple) -> bool:
    if(_coords[0]-1 > _limites[0]): return False
    elif(_coords[1]-1 >_limites[1]): return False
    else: return True



## funções de física:
# finalizar função
def mover_areia(_quadro: list, _coords: list) -> tuple:
    limites = pegar_limites(_quadro)
    if(checar_limites(_coords, limites)):
        pass
    elif(check_areia(_quadro[_coords[1]-1][_coords[0]+1])):
        pass
    elif(check_areia(_quadro[_coords[1]+1][_coords[0]+1])):
        pass
    else:
        pass


def atualizar_quadro_atual(_quadro: list) -> list:
    colunas = len(_quadro)
    linhas = len(_quadro[0])
    for linha in range(linhas):
        for coluna in range(colunas):
            if(check_ar(_quadro[coluna][linha])):
                continue
            if(check_areia(_quadro[coluna][linha])):
                continue
    return 0


def imprimir_quadro_atual(_quadro: list, _frame: int) -> bool:
    colunas = len(_quadro[1])
    linhas = len(_quadro[0])
    print(f'frame: {_frame}')
    for coluna in range(colunas):
        for linha in range(linhas):
            print(_quadro[coluna][linha], end='')
        print()
    return 0


def WindAndTurth():
    total_frames = entrada_frames()
    lins = 32
    cols = 64
    dimesao_inicial = (lins, cols)
    quadro_atual = gerador_quadro_inicial(dimesao_inicial)
    frame_atual = 0
    while frame_atual =< total_frames:
        infos_novo_bloco = check_novo_bloco()
        frame_atual = infos_novo_bloco[0]
        coords_elemento = infos_novo_bloco[1:len(infos_novo_bloco)-1]
        novo_quadro = adicionar_elemento(quadro_atual, coords_elemento)
        if(novo_quadro = 0):
            return False
        
