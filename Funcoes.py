# Funcoes 

import random 

def mostralinhas():
    print('------------------------------')


def mostralinhasauto():
    print('-'*30)


def mensagem(msg):
    mostralinhas()
    print(msg)
    mostralinhasauto()

print('------------------')
print('Print Normal')
print('------------------')

mostralinhas()
print('Print Funcao')
mostralinhasauto()

mensagem('Funcao Mensagem')

def soma(a,b):
    s = a + b 
    print(s)

soma(7,7)


def num_aleat():
    num = random.randrange(1, 1000000)
    print(num)
    return num



soma(a=num_aleat(),b=num_aleat())

def contador(*num):
    print(num)

contador(1,2,3,4,5,6,7)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    

valores = [0,1,2,3,4,5,6,7]
dobra(valores)
print(valores)







