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
def overlapCalc(e1x0, e1x1, e2x0, e2x1, e1y0, e1y1, e2y0, e2y1):
    

#opção alternativa: comparar x separadamente e depois y separadamente.
def interseptCheck(e1x0, e1x1, e2x0, e2x1, e1y0, e1y1, e2y0, e2y1):
    if(((e2x0 <= e1x1) and (e2y0 <= e1y1)) or ((e2x1 >= e1x0) and (e2y1 >= e1y0))):
        return True
    else: 
        return False


def resultPrinter(e1x0, e1x1, e2x0, e2x1, e1y0, e1y1, e2y0, e2y1):
    if(interseptCheck(e1x0, e1x1, e2x0, e2x1, e1y0, e1y1, e2y0, e2y1)):
        print("HIT: {} {} {} {}".join(overlapCalc(e1x0, e1x1, e2x0, e2x1, e1y0, e1y1, e2y0, e2y1)))
    else:
        print("MISS")


# Entradas das coordenadas
entradaUm = input()
entradaDois = input()