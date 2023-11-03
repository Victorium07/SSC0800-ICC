# [4 - Vetores] O Enigma

#funções úteis:

# Limpeza de espaços vazios durante a entrada das listas originais.
def ajustandoRotor(_rotor: str) -> list:
    _rotor = _rotor.split(' ')
    _rotor = [int(num) for num in _rotor if(num != '')]
    return _rotor

# Verifica se a letra atual é maiúscula ou minúscula.
def checkMin(_charNum: int) -> bool:
    if(_charNum < 97): return False
    else: return True

# Devolve o índice da letra atual no alfabeto.
def pegarIndiceChar(_numCarac: int) -> int:
    '''
    Eu vi essa sacanagem num vídeo de branchless programming em C e desde então queria usar em algum local.
    Peço desculpas pela lógica feia, apesar de correta. Prometo não fazer novamente.
    '''
    _novoIndice = (1-checkMin(_numCarac))*(_numCarac - 65) + (checkMin(_numCarac))*(_numCarac - 97)
    return _novoIndice

# Devolve o caracter pós criptografia.
def pegarCharAtual(_numCarac: int, _nIndex: int) -> str:
    _caract = (1-checkMin(_numCarac))*chr(65 + _nIndex) + (checkMin(_numCarac))*chr(97 + _nIndex)
    return _caract

# "rotaciona" um dado vetor.
def rodandoFila(_rotor: list) -> list:
    _rotor.append(_rotor.pop(0))
    return _rotor

# Verifica se é o momento correto de "rotacionar" um  dado rotor baseado em seu "número".
def checkRodar(_contador: int,_n_dentes: int, _n_rotor: int):
    if(_contador%(_n_dentes**(_n_rotor-1)) != 0):
        return False
    else: 
        return True

# Realiza as rotações.
def atualizarRotores(_r1: list, _r2: list, _r3: list, _contador: int) -> bool:
    numDentes = len(_r1)
    rodandoFila(_r1)
    if(checkRodar(_contador, numDentes, 2)): rodandoFila(_r2)
    if(checkRodar(_contador, numDentes, 3)): rodandoFila(_r3)
    return 0

def RhythmOfWar():
    cont = 0
    alfaCont = 0
    while True:
        try:
            line = input()
        except EOFError:
            break   
        
        if(cont == 1):
            r1 = ajustandoRotor(line)
        if(cont == 2):
            r2 = ajustandoRotor(line)
        if(cont == 3):
            r3 = ajustandoRotor(line)

        if(cont > 5):
            for i in range(len(line)):
                if(line[i].isalpha()):
                    numCarac = ord(line[i])
                    indiceLetraAtual = pegarIndiceChar(numCarac)
                    novoIndice = r3[r2[r1[indiceLetraAtual]]]
                    novoCaract = pegarCharAtual(numCarac, novoIndice)
                    print(novoCaract, end='')
                    alfaCont += 1
                    atualizarRotores(r1, r2, r3, alfaCont)
                    
                else: 
                    print(line[i], end='')
            print()
        cont +=1
    return 0

RhythmOfWar()