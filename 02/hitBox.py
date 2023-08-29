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

#opção alternativa: comparar x separadamente e depois y separadamente.
def interseptCheck(e1=[0,0,0,0], e2 = [0,0,0,0]):
    if(((e2[0] <= e1[2]) and (e2[1] <= e1[3])) or ((e2[2] >= e1[0]) and (e2[3] >= e1[1]))):
        return True
    else: 
        return False

def linearOverlap(e1, e2):
    if (e1[0] >= e2[0]):
        valorInicial = e1[0]
    else: valorInicial = e2[0]
    if (e1[1] >= e2[1]):
        valorFinal = e2[1]
    else: valorFinal = e1[1]
    return [valorInicial, valorFinal]

def areaOverlap(e1, e2):
    coordX = linearOverlap(e1[0], e1[2], e2[0], e2[2])
    coordY = linearOverlap(e1[1], e1[3], e2[1], e2[3])
    listafinal = [coordX[0], coordY[0], coordX[1], coordY[1]]
    return listafinal

def WordsOfRadiance(e1, e2):
    if(interseptCheck(e1x0, e1x1, e2x0, e2x1, e1y0, e1y1, e2y0, e2y1)):
        print("HIT: {} {} {} {}".join(areaOverlap(e1x0, e1x1, e2x0, e2x1, e1y0, e1y1, e2y0, e2y1)))
    else:
        print("MISS")

# Entradas das coordenadas
entradaUm = input().split()
entradaDois = input().split()