#importando bibliotecas
import codecs
import time

#funções úteis
def checker(entrada):
    try:
        entrada = int(entrada)
        return False
    except:
        print("Relembrando, precisamos de números inteiros! ;)")
        return True

#apresentação
apresentacao = "Olá! \nEste programa vai permitir que números inteiros sejam convertidos em palavras! \nMas lembre-se, precisamos entrar NÚMEROS INTEIROS."
#print(apresentacao)

#solicitações de entrada
#entrada = input("Entre agora o seu número inteiro: ")
entrada = input()

#teste de entrada correta
while (checker(entrada)):
    #entrada = input("Entre agora o seu número inteiro: ")
    entrada = input()

#conversão pra hex
entrada = int(entrada)
hex = '{:x}'.format(entrada)

#conversão pra bytes
bts = bytes.fromhex(hex)

#conversão para idiomas humanos (ou quase...)
expressao = codecs.decode(bts, errors = 'replace')
print(expressao)