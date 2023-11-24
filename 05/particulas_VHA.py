# [5 - Funções] Simulação de Partículas - PESO 2x

#biblitecas úteis:
import copy

#funções úteis:
def entrada() -> int:
    n_frames = int(input())
    return n_frames

def adicionar_elemento(quadro_antigo: list, _lista_entradas: list) -> list:
    quadro_novo = copy.deepcopy(quadro_antigo)
    quadro_novo[_lista_entradas[1]][_lista_entradas[0]] = _lista_entradas[2]
    return quadro_novo

def gerador_quadro_inicial(_tuple:tuple) -> list:
    quadro = [' ' * _tuple[1] for _ in range(_tuple[0])]
    return quadro

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


def mover_areia(_quadro: list, _coords: list, _limites: tuple) -> tuple:
    if(checar_limites(_coords, _limites)):
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


def imprimir_quadro_atual(_quadro: list) -> bool:
    colunas = len(_quadro)
    linhas = len(_quadro[0])
    for coluna in range(colunas):
        for linha in range(linhas):
            print(_quadro[coluna][linha], end='')
        print()
    return 0


def WindAndTurth():
    total_frames = entrada()
    lins = 32
    cols = 64
    dimesao_inicial = (lins, cols)
    quadro = gerador_quadro_inicial(dimesao_inicial)
    for frame in range(total_frames):
        try:
            update = input().split()
            #separar entrada e coordenadas novas
        except EOFError:
            pass
        else:
            pass
        finally:
            pass