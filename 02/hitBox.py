#Solção usando classes
# class box:
#     def __init__(self, entry):
#         self.entry = entry

#     def separator(self, x0, y0, x1, y1):
#         data = self.split()
#         self.x0 = data[0]
#         self.y0 = data[1]
#         self.x1 = data[2]
#         self.y1 = data[3]

#funções úteis

#converte a lista de str em int
def inputConverter(listaCoordenadas):
    obs = [int(numero) for numero in listaCoordenadas]
    return obs

#separa as entradas em suas correspondêntes dimensões
def axis(entrada):
    return ([entrada[0],entrada[2]], [entrada[1], entrada[3]])

#converte largura e altura em posição final.
def coords(entrada):
    x, y = axis(entrada)
    finalX = x[0] + x[1]
    finalY = y[0] + y[1]
    return([x[0], finalX], [y[0], finalY])

#avalia se há sobreposição
def interseptCheck(x1, x2, y1, y2):
    if(((x2[0] <= x1[1]) and (y2[0] <= y1[1])) or ((x2[0] >= x1[1]) and (y2[1] >= y1[0]))):
        return True
    else: 
        return False

#devolve qual é a sobreposição linear
def linearOverlap(regiao_obj_1, regiao_obj_2):
    if (regiao_obj_1[0] >= regiao_obj_2[0]):
        valorInicial = regiao_obj_1[0]
    else: valorInicial = regiao_obj_2[0]
    if (regiao_obj_1[1] >= regiao_obj_2[1]):
        valorFinal = regiao_obj_2[1]
        valorFinal = valorFinal - regiao_obj_1[1]
    else: 
        valorFinal = regiao_obj_1[1]
        valorFinal = valorFinal - regiao_obj_1[1]
    return [valorInicial, valorFinal]

#devolve as coordenadas da região de sobreposição no formato x_inicial, y_inicial, x_final, y_final
def hitBox(x1, x2, y1, y2):
    coordX = linearOverlap(x1, x2)
    coordY = linearOverlap(y1, y2)
    listafinal = [str(coordX[0]), str(coordY[0]), str(coordX[1]), str(coordY[1])]
    return listafinal

#função final que chama tudo
def WordsOfRadiance(e1, e2):
    x1, y1 = coords(e1)
    x2, y2 = coords(e2)
    if(interseptCheck(x1, x2, y1, y2)):
        print("HIT: {}".join(hitBox(x1, x2, y1, y2)))
    else:
        print("MISS")

# Entradas
entradaUm = inputConverter(input().split())
entradaDois = inputConverter(input().split())

WordsOfRadiance(entradaUm, entradaDois)