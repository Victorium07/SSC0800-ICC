# [Sub - Recursão] Fractal - EXERCÍCIO SUB DO BEM

# funções úteis:
def gerar_canvas_quadrado(n: int) -> list:
    _canvas = [[' ' for i in range(0, n)] for j in range(0, n)]
    return _canvas

def entrada() -> int:
    profundidade = int(input())
    return profundidade

def H_na_horizontal(_canvas: list, _coord_min: int, _tamanho: int, _aux_coord: int) -> bool:
    tamanho = 2*_tamanho
    for z in range(tamanho):
        _canvas[_aux_coord][_coord_min + z] = 'H'
    return 0

def H_na_vertical(_canvas: list, _coord_min: int, _tamanho: int, _aux_coord: int) -> bool:
    tamanho = 2*_tamanho
    for z in range(0, tamanho+1):
        _canvas[_coord_min + z][_aux_coord] = 'H'
    return 0

def desenhar_horizontal(_canvas: list, _coord_central: int, _tamanho: int, _fixed_y: int) -> bool:
    coord_min = _coord_central - (_tamanho)
    H_na_horizontal(_canvas, coord_min, _tamanho, _fixed_y)
    return 0

def desenhar_vertical(_canvas: list, _coord_central: int, _tamanho: int, _fixed_x: int) -> bool:
    coord_min = _coord_central - (_tamanho)
    H_na_vertical(_canvas, coord_min, _tamanho, _fixed_x)
    return 0

def criar_aga(_canvas, _profundidade: int, _tamanho_matriz: int, _x_init: int, _y_init: int) -> bool:
    #parte 1: testar se profundidade é maior do que 0
    if(_profundidade < 0):
        return 0

    _comprimento = _tamanho_matriz//2

    #parte 2: criar linha horizontal
    desenhar_horizontal(_canvas, _x_init, _comprimento//2, _y_init)

    #parte 3: criar linhas verticais
    desenhar_vertical(_canvas, _y_init, _comprimento//2, _x_init - _comprimento//2)
    desenhar_vertical(_canvas, _y_init, _comprimento//2, _x_init + _comprimento//2)

    #parte 4: repetir na camada interior
    _profundidade -= 1
    criar_aga(_canvas, _profundidade, _comprimento, _x_init - _comprimento//2, _y_init - _comprimento//2)
    criar_aga(_canvas, _profundidade, _comprimento, _x_init - _comprimento//2, _y_init + _comprimento//2)
    criar_aga(_canvas, _profundidade, _comprimento, _x_init + _comprimento//2, _y_init - _comprimento//2)
    criar_aga(_canvas, _profundidade, _comprimento, _x_init + _comprimento//2, _y_init + _comprimento//2)


def desenhar_tela(_canvas: list) -> bool:
    tamanho_y = len(_canvas)
    tamanho_x = len(_canvas[0])
    for y in range(tamanho_y):
        for x in range(tamanho_x):
            print(_canvas[y][x], end = '')
        print()
    return 0

def WindAndTruth() -> bool:
    tam_mat = 128
    canvas = gerar_canvas_quadrado(tam_mat)
    profundidade = entrada()
    criar_aga(canvas, profundidade, tam_mat, tam_mat//2, tam_mat//2)
    desenhar_tela(canvas)
    return 0

WindAndTruth()