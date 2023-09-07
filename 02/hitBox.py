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

#Comparação linear ok!
def linearCheck(reta1, reta2):
    if((reta2[0] > reta1[1] and reta2[1] > reta1[1])
       or ((reta1[0] > reta2[0]) and (reta1[0] > reta2[1]))):
        return False
    else: return True        

#devolve qual é a sobreposição linear
def linearOverlap(reta1, reta2):
    if (reta1[0] >= reta2[0]):
        valorInicial = reta1[0]
    else: valorInicial = reta2[0]
    if (reta1[1] >= reta2[1]):
        valorFinal = reta2[1]
        valorFinal = valorFinal - valorInicial
    else: 
        valorFinal = reta1[1]
        valorFinal = valorFinal - valorInicial
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
    # print("Infos objeto 1:\n")
    # o = "xi: "+str(x1[0])+" xf: "+str(x1[1])+" yi: "+str(y1[0])+" yf:"+str(y1[1])
    # print(o)
    x2, y2 = coords(e2)
    # print("Infos objeto 2:\n")
    # o = "xi: "+str(x2[0])+" xf: "+str(x2[1])+" yi: "+str(y2[0])+" yf:"+str(y2[1])
    # print(o)

    if(linearCheck(x1, x2) and linearCheck(y1, y2)):
        print("HIT: "+" ".join(hitBox(x1, x2, y1, y2)))
    else:
        print("MISS")

# Entradas
entradaUm = inputConverter(input().split())
entradaDois = inputConverter(input().split())

WordsOfRadiance(entradaUm, entradaDois)