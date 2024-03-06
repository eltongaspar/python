# Exercicicos 

#1 - print
print(f'Olá Mundo')

#2 Print Nome 
print(f'Elton Gaspar de Moura')

#3 Strings combinadas 
print('Python' + 'Progranação')

#4 Print numeros
result = (3+5)
print(result)

#5 Escrever um poema em várias linhas formatadas 
print(f'''De tudo, ao meu amor serei atento
Antes, e com tal zelo, e sempre, e tanto
Que mesmo em face do maior encanto
Dele se encante mais meu pensamento.
Quero vivê-lo em cada vão momento
E em louvor hei de espalhar meu canto
E rir meu riso e derramar meu pranto
Ao seu pesar ou seu contentamento.
E assim, quando mais tarde me procure
Quem sabe a morte, angústia de quem vive
Quem sabe a solidão, 
fim de quem amaEu possa me dizer do amor (que tive):
Que não seja imortal, posto que é chama
Mas que seja infinito enquanto dure.\n''')

#6 Print com end
print('Teste End',end='')
print('Na mesma linha com 2 comandos prints')

# 7 Calculos
#f(x) = x^2 + 3x - 1 0
x = input(f'Informe o valor de X:  ')
x = float(x)
f = (x**2) + (x*3) - 10
print(f'Resultado f(x) {f} ')

#8 Calculo velocidade final 
# V**2 = V0**2 + 2*A*DS
print(f'Calculo velovidade final')
V0 = input(f'Velocidade Inicial V0:  ')
A = input(f'Aceleração A:  ')
DS = input(f'Deslocamento DS:  ')
V0 = float(V0)
A = float(A)
DS = float(DS)

V = ((V0**2) + (2*A*DS))**(0.5)


#9 Convertat() a temperatura de Celsius para Fahrenheit.
#C/5 = F-32 / 9
C = input('Informe a Temperatura Cº: ')
C = float(C)
F = (C * 9/5) + 32 
print(f'A Temperatura ºC:', C)
print(f'A Temperatura ºF:', F)


#10 Compra com desconto
import datetime
total = input(f'Informe o valor total da compra:  ')
total = float(total)

desconto = input('Informe o Percentual do desconto % : ')
desconto = float(desconto)

totalpagar = total - (total*(desconto/100))
data_hora_atual = datetime.datetime.now()

print('------------------------------------')
print('Lojas Super')
print(f'Total das Compras:R$ ',total)
print(f'Percentual deconto: ',desconto,'%')
print(f'Total a pagar:R$  ',totalpagar)
print('Cupom Fiscal - Versão 1.0')
print('------------------------------------')

print(f"Data e hora atual: {data_hora_atual}")

#11 Idade do uuário e informar se é maior de 18 anos 

idade = input('Informe sua idade: ')
idade = int(idade)
print('Sua idade é : ', idade)

if idade >= 18:
    print('Você tem mais de 18 anos:')
else:
    print('Você possue menos de 18 anos')

#12 Notas de pontuação 

pontos = input(f'Informe a sua pontuação: ')
pontos = int(pontos)

if pontos >= 80:
    print(f'Parabens, Exlente, sua pontuação é: ',pontos)
elif pontos >  50 and pontos <= 79:
    print(f'Parabens, Bom, sua pontuação é: ',pontos)
elif pontos <= 49:
    print(f'Precisa melhorar,sua pontuação é: ',pontos)



#13 Analisar numero maior e se e divisivel
num1 = input('Informe o numero 1: ')
num2 = input('Informe o numero 2: ')
num1 = int(num1)
num2 = int(num2)

#Comparando numeros
if num1 > num2:
    print(f'Numero 1 é maior',num1)
    print(f'Numero 2 é menor',num2)
else:
    print(f'Numero 2 é maior',num2)
    print(f'Numero 1 é menor',num1)
    
#Dividindo 

div = num1 % num2 

if div == 0:
    print(f'O Numero 1 é divisivel pelo Numero 2')
else:
    print(f'O Numero 1 não é divisivel pelo Numenro 2')

print(f'Resultado',div)

# 14 Preisao do tempo

prevtempo = ''

while prevtempo != 'ensolarado' and prevtempo !='chuvoso' and prevtempo != 'nublado':
    print(f'Qual a previsao do tempo?')
    prevtempo = input(f'ensolarado,chuvoso ou nublado: ')

if prevtempo == 'ensolarado':
    print(f'Leve ssu óculos de sol, aproveite!')
elif prevtempo == 'nublado':
    print(f'Existe grande possibilidade de chuvas, leve seu guarda-chuvas!')
else:
    print(f'Dia de chuva, não esqueça seu guarda-chuvas!')


#15 Idade Crianca, Adolescente, Adulto e Idoso

idade = -1

while idade < 0:
    idade = input(f'Informe sua idade: ')
    idade = int(idade)
    

if idade < 13:
    print(f'Criança')
elif idade >= 13 and idade <= 19:
    print(f'Adolecente')
elif idade >= 20 and idade <= 59:
    print(f'Adulto')
elif idade >= 60:
    print(f'Idoso') 


#16 Analisar 03 numeroe , vericar se numero é maior que os dos, e a soma de B + C > A
a = input(f'Digite número A :')
b = input(f'Digite número B :')
c = input(f'Digite número C :')

a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print(f'A é o maior número: ',a)
    if a > (b+c):
        print(f'O primeiro número é maior que a soma dos outros dois','A',a,'Soma',(b+c))
    else:
        print(f'O primeiro número é maior que a soma dos outros dois','A',a,'Soma',(b+c))

else:
    print('O primeiro número não é o maior.')

    #17 Numero informado é par ou impar

num = input(f'Informe um número')
num = int(num)
div = 2

result = num % div

if result == 0:
    print(f'Número informado é par',num)
elif result != 0:
    print(f'Número informado é impar',num)

    #18 - Compras valor total, valor desconto e valor a pagar 

import datetime


def linhas():
    print('------------------------------------')


linhas()
valtotal = input(f'Informe o valor Total da Compra R$')
linhas()
valtotal = float(valtotal)

if valtotal < 100:
    percent = 5
elif valtotal >= 100 and valtotal < 1000:
    percent = 10
elif valtotal >= 1000:
    percent = 15

desc = ((percent/100)*valtotal)
valpagar = valtotal - desc

linhas()
print(f'Valor Total R$',valtotal)
print(f'Percentual Desconto:',percent,'%')
print(f'Valor desconto R$',desc)
print(f'Valor a pagar R$',valpagar)
linhas()
data_hora_atual = datetime.datetime.now()
print(f"Data e hora atual: {data_hora_atual}")


#19 Informar 10 numeros e contar pares e impares 

div = 2
listanum = []
par = 0
impar = 0

for cont in range(10):
    num = input(f'Informe um numero:  10')
    num = int(num)
    print(f'Numero:',cont+1)
    result = num % div 
    if result == 0:
        par = par +1
    elif result != 0:
       impar = impar + 1
    listanum.insert(cont,num)

print(f'Total némros pares:',par)
print(f'Total númros impares:',impar)
print(f'Total numeros informados',cont)
print(f'Lista Numeros',listanum)


# 20 - Calculo Fatorial 

numinform = -1
cont = 1
fatlist = []
resultfat = 1

while numinform <= 0:
    numinform = input(f'Informe um nuemro para calcular o Fatorial:  ')
    numinform = int(numinform)

numfat = numinform

while cont <= numinform:
    fatlist.insert(cont,numfat)
    cont = cont + 1
    resultfat = resultfat * numfat
    numfat = numfat - 1
    


fatlist.sort(reverse=True)
print(fatlist)
print(resultfat)

#Numeros Primos 
# 21 - Diisivel por 1 por ele mesmo

num = input(f'Informe um número para ver se é primo:  ')
num = int(num)
div = 0
result = 0
qtdenumdiv = -1
qtdenumdivnot = 0
cont = 0

for cont in range(num+1):
    
    if div > 0:
        result = num % div
    
    div  += 1

    if result == 0:
        qtdenumdiv = qtdenumdiv + 1
    elif result != 0:
        qtdenumdivnot = qtdenumdivnot + 1
   

if qtdenumdiv == 1 or qtdenumdiv == 2:
    print(f'Numero Primo',num)
elif qtdenumdiv > 2:
    print(f'Numero não é Primo',num)


#22 Meta de econmia 

valmes = input(f'Informe o valor mensal a ser economizado:  ')
meta = input(f'Informe o valor da Meta:  ')
valmes = float(valmes)
meta = float(meta)
qtdemesmeta = meta / valmes

print(f'O total de meses para atingir a meta é',qtdemesmeta,'meses')


#23 - Informar temperatura
# informar sair para finalizar programa 
#(Celsius * 9/5) + 32.

valid = False
celsus = ''
fahrenheit = 0

while valid == False:
    celsus = input(f'Informe a temperatura ºC para conversão em ºF, para terminar digite sair  ')

    if celsus == 'sair':
        valid = True
    elif celsus != 'sair' and valid == False:
        celsus = int(celsus)
        fahrenheit = (celsus * (9/5) + 32)
        print(f'A temperatura ºC',celsus,'é ºF',fahrenheit)

#24 - Analisar triangulo 

print(f'Calculo de tipo de triangulo')
print(f'Informar os tres lados do triangulo')
la = input(f'Informa lado A:  ')
lb = input(f'Informa lado B:  ')
lc = input(f'Informa lado C:  ')

la = int(la)
lb = int(lb)
lc = int(lc)

if la == lb and la == lc:
    print('Triangulo Equilatero, todos lado iguais')

elif (la == lb and la != lc ) or (la == lc and la != lb)  or (lb == lc and lb != la):
    print('Triangulo Isosceles, dois lados iguais e um diferente')

elif la != lb and la != lb and lb != lc:
    print('Triangulo Escaleno, todos lados diferentes')


#25 - Ano de nascimento 
from datetime import date 
dataatual = date.today().year


anonasc = -1
totalanos = 0
cont = 0
anolist = 0

while anonasc < 0:
    anonasc = input(f'Informe seu Ano de nascimento:  ')
    anonasc = int(anonasc)

totalanos = dataatual - anonasc
anolist =anonasc

print(f'Você nasceu em:',anonasc)
print(f'Ano Atual',dataatual)
print(f'Você viveu',totalanos,'anos')

while cont <= totalanos:
    print('Você viveu em: ',anolist)
    anolist += 1
    cont += 1


#26 - Funcao Calculo Fatorial


def calcfatorial():
    numinform = -1
    cont = 1
    fatlist = []
    resultfat = 1

    while numinform <= 0:
        numinform = input(f'Informe um nuemro para calcular o Fatorial:  ')
        numinform = int(numinform)

    numfat = numinform

    while cont <= numinform:
        fatlist.insert(cont,numfat)
        cont = cont + 1
        resultfat = resultfat * numfat
        numfat = numfat - 1


    fatlist.sort(reverse=True)
    print(fatlist)
    print(resultfat)

    exib = 0
    cont = 0
    while cont <= numinform:
        exib = (resultfat[1])
        cont += 1

    return fatlist 

calcfatorial()

#27 -  Calculos aritmeticos 

#funcao aritmetica 

def operaritmetica(a,b,oper):
    if oper == '+':
        c = a+b
        mens = 'Soma' 
    elif oper == '-':
        c = a-b 
        mens = 'Subtração'
    elif oper =='*':
        c = a*b 
        mens = 'Multiplicação'
    elif oper == '/':
        if b == 0:
            mens = 'Erro divisão por zero!'
            c = 0
        elif b != 0:
            c = a/b 
            mens = 'Divisão'

    print(f'Numeros Informados','A:',a,'B:',b)
    print(f'Operação aritmética',oper)
    print(mens)
    print(f'Resultado:',c)
    
    return c,mens

#programa principal 
a = input(f'Informe valor A:  ')
a = int(a)

b = input(f'Informe valor B:  ')
b = int(b)

oper = ''
while oper != '+' and oper != '-' and oper != '*' and oper != '/':
    oper = input('Informe a operação aritmética: Soma +,Subtração -,Multiplicação*,Divisão/ :  ')

operaritmetica(a,b,oper)



#28 
import cmath 
# Funcao Calcular Graus radianos 

def linhas(qtdetracos):
    linha = ''
    cont = 0
    while cont <= qtdetracos:
        linha = linha + '-'
        cont += 1
    print(linha)


def calcular_pi(n):
    """
    Calcula o valor de Pi usando a série de Leibniz.

    Args:
    n: Número de termos da série a serem usados.

    Returns:
    O valor de Pi calculado.
    """
    pi = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            pi += 4 / (2 * i - 1)
        else:
            pi -= 4 / (2 * i - 1)

    print(f"Valor de Pi (série de Leibniz): {pi}")
    return pi


def calc_pi_graus_radianos():
    linhas(qtdetracos=50)
    print('Calculo Graus Radianos')
    print('Calculos com Cmath e Padrão')
    linhas(qtdetracos=50)

    import cmath

    n = input('Informe a precisão de PI:')
    n = int(n)
    pi = calcular_pi(n)
    
    graus = input('Informe o valor dos Graus para calculo ')
    graus = float(graus)
    radianospad = 0
    radianospad = graus * pi /180

    linhas(qtdetracos=50)
    print(f'PI Padrao',pi)
    print(f'Graus Radianos Padrao',radianospad)
    linhas(qtdetracos=50)

    picmath = cmath.pi
    radianoscalcmath = graus * picmath / 180
    linhas(qtdetracos=50)
    print(f'PI Cmath',picmath)
    print(f'Graus Radianos Cmath',radianoscalcmath)
    linhas(qtdetracos=50)


calc_pi_graus_radianos()

# 29 - JogoAdivinha Numero

# Funcao Gerar numero
def num_aleat(num_min,num_max):
    import random
    num_ger = random.randrange(num_min,num_max)
    return num_ger

def exibcontagem(conttela):
    cont = 0
    while cont <= conttela:
        print('Processando',cont)
        cont += 1
    


#programa principal
    
num_min = 1
num_max = 100
num_ger = num_aleat(num_min,num_max)

print('Jogo Adivinha Numero')
print('Gerando Numero Aleatório de ',num_min,num_max )
conttela = 10
exibcontagem(conttela)

numinfor = 0
erro = 0
print(num_ger)

while numinfor != num_ger and numinfor != 'sair':
    print('Numero sorteado de',num_min,num_max)
    numinfor = input('Informe um numero de, sair para terminar  ')
    numinfor = int(numinfor)

    if numinfor != num_ger:
        print('Voce errou, tente novamente')
        erro += 1
        if numinfor < num_ger:
            print('Valor Baixo')
        elif numinfor > num_ger:
            print('Valor Alto')

    elif numinfor == num_ger:
        print('Parabens, voce acertou!')
        print('Total Erros',erro)
        


    #30 Calculos triangulo por cmath

#Funcao print linhas
def linhas(qtdetracos):
    linha = ''
    cont = 0
    while cont <= qtdetracos:
        linha = linha + '-'
        cont += 1
    print(linha)

#Funcao arrendodar numeros 
def roundnum(num,casasdec):
    import cmath
    # Convertendo para número real
    num, phase = cmath.polar(num)
    
    # Arredondando o número real
    numround = round(num,7)
    return numround


# Funcao calculo triangulo retangular
def calctriangulo():

    import cmath
    
    print(f'Calculo de um Triangulo Retangular')

    
    a = input(f'Informe o Cateto 1 :  ')
    a = int(a)
    b = input(f'Informe o Cateto 2:  ')
    b = int(b)

    hipotenusa = cmath.sqrt(a**2 + b**2)
    c = hipotenusa
    seno = cmath.sin(cmath.acos(a/c))
    cosseno = cmath.cos(cmath.acos(a / c))
    tangente = cmath.tan(cmath.acos(a/c))

    num = hipotenusa
    casasdec = 7
    hipotenusa = roundnum(num,casasdec)

    num = seno
    seno = roundnum(num,casasdec)

    num = cosseno
    cosseno = roundnum(num,casasdec)

    num = tangente
    tangente = roundnum(num,casasdec)
     
    linhas(qtdetracos=50)
    print('Triangulo Retangular, cálculos')
    print(f'Hiponenusa',hipotenusa)
    print(f'Seno',seno)
    print(f'Cosseno',cosseno)
    print(f'Tangente',tangente)
    linhas(qtdetracos=50)

#programa principal 

calctriangulo()

# 31 Palavras invertidas 

# funcao para inverter texto
def textoinvert(text):
    textinvert = text
    return textinvert[::-1]

#program principal 

print(f'Informe seu texto para inversão')
textdigit = input(f'Informe seu texto:')

textinvertexib =  textoinvert(textdigit)
print('Seu Texto invertido',textinvertexib)

# 32 - Informar texto e retonat posicoes impares

def exibtextposimpar(textodigit):
    textposimpar = textodigit
    return textposimpar[0::2]

print('Exibir texto com posições de letras impares')
textdigit = input('Informe seu texto:  ')

textexib = exibtextposimpar(textdigit)
print('Texto com posições impares')
print(textexib)

# 33 Lista de palavras proibidas 

def bloqtext(texto):
    import re
    lisbloqtext = ['teste','valid']

    qtdetext = len(lisbloqtext)
    cont = 0
    valid = False
    
    
    for temp in lisbloqtext: 
        texttemp = temp 
        
        if re.search(texttemp,text):
            print('Texto localizado Posição',cont)
            lisbloqtext.pop(cont)
            lisbloqtext.insert(cont,'*******')
            cont += 1
            textret = '*******'
            valid = True
                     
        elif not re.search(texttemp,text):
            print('Texto não localizado',cont)
            cont += 1
            
        if valid == False:
            textret = text
           

    
    return textret
        
print('Informe um texto a ser analisado com palavras proibidas')
text = input('Texto:  ')
textexib = bloqtext(text)
print(textexib)


#34 Criar template e substituir campos informados 

# Funcao Template 
def template_alter(nome,data):
    template = (f""" 
    Olá [nome], tudo bem?
    Esperamos que sim!
    Gostariamos de informar que estamso notificando você,
    para entar em contato conosco urgente.
    Att.
                
    [data]
    Empresa S.A
    """)

    template_ret = template.replace("[nome]",nome).replace("[data]",data)
    
    return template_ret

#programa principal
    
# Imoportar biblioteca data 
import datetime

print(f'Templat Notificação')
nome = input(f'Informe o nome:  ')
data = datetime.datetime.now()
data =  data.strftime("%D")

template_exib = template_alter(nome,data)
print(template_exib)


# 36 - Contar caracter

#funcao cont caracteres 
def cont_carater(text,text_localiz):
    import re 
    
    
    cont = 0
    qtd_caracter = len(text)
    qtde_caracter_localiz = 0

    while cont < qtd_caracter:
        temp = text[cont]   
        if re.search(text_localiz,temp):
            print('Localizado posição!',cont)
            qtde_caracter_localiz += 1

        cont += 1
    
    return qtde_caracter_localiz

#programa principal 

print('Contar quantidade de caracteres eum um texto ou palavra')
text = input('Informe aqui seu Texto / palavras:  ')
text_localiz = input('Informe o caracter a ser contado:  ')

cont_caracter = cont_carater(text,text_localiz)

print('Total de repetições do caracter:  ',cont_caracter)


#38 string é um palíndromo (uma palavra que é lida da mesma forma de trás para frente, como "radar").


#Funcao para string ser reversa

def func_text_reverse(text):

    text_revers = ''.join(reversed(text))

    if text == text_revers:
        print(f'''A palavra é um palíndromo,
              uma palavra que é lida da mesma forma de trás para frente''')
        print(f'Palavra original:  ',text)
        print(f'PAlavra reversa: ',text_revers)

    elif text != text_revers:
        print(f'A palavra não é um palíndromo ')

    tam_text = len(text)
    cont = 0
    is_palíndromo = 0
    not_palíndromo = 0

    while cont <  tam_text:
        if text[cont] == text_revers[cont]:
            is_palíndromo += 1
        elif text[cont] != text_revers[cont]:
            not_palíndromo += 1

        cont += 1

    if not_palíndromo == 0:
        print(f'A palavra é um palíndromo Funcao While',text,text_revers)
    elif not_palíndromo > 0:
        print(f'A palavra Não é um palíndromo Funcao While',text,text_revers)
       

    
#programa principal 
print('Palíndromo, se uma palavra é igual escrita de tras para frente')

text = input('Digite a palavra:  ') 

func_text_reverse(text)


#39 Criando arquivos 
import os

file = open('D:/Dados/meu_arquivo.txt','x')
file.close()

if os.path.exists('D:/Dados/meu_arquivo.txt'): 
    print('Arquivo criado com sucesso')
else:
    print('Atquivo não localiado!')


# 40 Abrir aquivo e exibir seus dados 

#Abrindo o arquivo

file = 'D:/Dados/meu_arquivo.txt'


def open_file(file):
    file = open(file,'r')
    return file
    

def close_file(file):
    file.close()
    

#valida se o arquivo e valida 
print('Validador:',open_file(file).readable())
close_file(open_file(file))

#Ler contudo do arquivo
print(open_file(file).read())
close_file(open_file(file))

#Ler contudo do arquivo
print(open_file(file).readline())
close_file(open_file(file))

#Ler contudo do arquivo
print(open_file(file).readlines())
close_file(open_file(file))

#Arquivo em lista
lista = open_file(file).readlines()
print(lista)
close_file(open_file(file))


#41 Alterando arquivo sem perder dados 
file = 'D:/Dados/meu_arquivo.txt'

def open_file(file):
    file = open(file,'r')
    return file
    

def close_file(file):
    file.close()
    

#Funcao open alteracao e close file
def open_file_alt(file):
    file = open(file,'a')
    return file
    

def close_file(file):
    file.close()

#programa principal 

# Alterando arquivo
open_file_alt(file).write('Adicionando uma nova linha ao arquivo.\n')
close_file(open_file_alt(file))

#Ler contudo do arquivo
print(open_file(file).read())
close_file(open_file(file))



#42 Lista diretori e imprimir conteudo 

# Usandoa biblioteca os
import os
import time

#defindo diretorio
dir = 'D:/Dados'

# Listando diretorio 
files = os.listdir(dir)
#Contagem de arquivos 
num_files = len(files)

print(f'Listando, contando e exibindo arquivos')
print(f'Diretorio',dir)
print(f'Total Arquivos:',num_files)
time.sleep(5)

for file_conteud in files:
    with open(os.path.join(dir,file_conteud),'r') as f:
        conteudo = f.read
        print(file_conteud)
        print(conteudo)
        time.sleep(1)


#43 - Copiando dados de um arquivo para outr

import os
file = 'D:/Dados/meu_arquivo.txt'
file_des = 'D:/Dados/meu_arquivo-copia.txt'

with open(file,'r') as origem:
    with open(file_des,'w') as destino:
        dados = origem.read()
        os.write(destino.fileno(),dados.encode())

if os.path.exists(file_des):
    print(f'Arquivo Existe, copiado!')
    
else: 
    print(f'Hum, não achei o arquivo:(!')

error = 0
acept = 0

with open(file,'r') as origem:
    with open(file_des,'r') as destino:
        for lin1,lin2 in zip(origem,destino):
            if lin1 != lin1:
                error += 1
            else:
                acept += 1
                


if error == 0 :
    print('Arquivos iguais, copia exata!')

elif error > 0:
    print(f'''Arquivos diferentes, 
            algo de errado não esta certo, 
            verifique!!!''')



# 44 - Contar linhas e caracter de um arquivos

import os
import re

files = 'D:/Dados/meu_arquivo.txt'

open_files = open(files, 'r')

# Validando se arquivo existe
if (open_files.readable()):
    print('Arquivo valido')
else:
    print('Arquivo não existe!')
open_files.close()   


# Validando se arquivo existe, sem necessidade de abrir
if os.path.exists(files):
    print('Arquivo Existe!')
    
else: 
    print('Hum, não achei o arquivo:(!')

#Exibindo dados do aquiro, linha a linha
print('Exibindo dados do arquivo, linha a linha, metodo 1')
with open (files,'r') as temp:
    for linha in temp:
        print(linha)


#Exibindo dados do arquiro, linha a linha
open_files = open(files, 'r')
print('Exibindo dados do arquivo, linha a linha, metodo 2')
print(open_files.readlines())
open_files.close()   


print(f'Contagem de palavras')
with open (files,'r') as temp:
    texto = temp
    texto = temp.read()
    #Contando palavras 
    palavras = texto.split()

num_palavras = len(palavras)
print(f'Numero de palavras é:',num_palavras)


#Contando linhas
print('Contagem de linhas no arquivo')
with open(files,'r') as linhas:
    num_linhas = len(linhas.readlines())
print(f'Numero de linhas: ',num_linhas)

#Contando caracteres 
print(f'Contagem de caracteres')
with open(files,'r') as temp_caracter:
    caracter = temp_caracter.read() 
    num_caracter = len(re.findall(r".",caracter))
print('Total caractres',num_caracter)


#45 Ler arquivo com as palavras Python

files = 'D:/Dados/meu_arquivo.txt'
open_files = open(files, 'r')

palavra_localiz = input('Informe a palavra a ser localizada no arquivo:  ')
localiz = 0
localiz_not = 0

with open(files,'r') as temp:

    for linha in temp:
        if palavra_localiz in linha:
            localiz += 1
        else:
            localiz_not += 1

if localiz > 0:
    print('Palavra encontrada!')
else:
    print('Palavra não encontrada no arquivo')


#47 Criar arquivo manualmente e ler linhas em modo formatado

files = 'D:/Dados/dados.txt'
open_files = open(files, 'r')

#with open(files,'r') as temp:



#Exibindo dados do aquiro, linha a linha
print('Exibindo dados do arquivo, linha a linha, metodo 1')
with open (files,'r') as temp:
    for linha in temp:
        print(''.join(linha))

        #48 Criando arquivos de logs, sem perder dados 
files = 'D:/Dados/logs.txt'
open_files = open(files, 'a')

import datetime
import os
import re


if os.path.exists(files):
    print('Arquivo Log localizado, incluindo novos logs!')
else: 
    print('Hum, não achei o arquivo, criando arquivo de logs!(!')


data_hora_atual = datetime.datetime.now()
data_hora_atual = str(data_hora_atual)




with open (files,'r') as temp:
    texto = temp
    texto = temp.read()
    #Contando palavras 
    palavras = texto.split()

num_palavras = len(palavras)
num_palavras = str(num_palavras)

#Contando linhas
with open(files,'r') as linhas:
    num_linhas = len(linhas.readlines())
    num_linhas = str(num_linhas)


#Contando caracteres 
with open(files,'r') as temp_caracter:
    caracter = temp_caracter.read() 
    num_caracter = len(re.findall(r".",caracter))
    num_caracter = str(num_caracter)

sequenc = num_linhas + num_palavras + num_caracter + data_hora_atual


#Criando arquivos logs.
with open (files,'a') as temp:
    temp.write(f'Logs' + ' ' + num_linhas + ' ' + data_hora_atual + ' ' + 'Sequencia'+ ' ' + sequenc + '\n')
    #temp.write(f'Logs' + ' '+ num_linhas + '  ' + data_hora_atual + ' ' + 'Sequncial' + num_linhas + num_palavras + num_caracter + '\n')
    print('Logs salvos com sucesso!')

# 48 - Tuplas 

# Criação de tuplas - imutaveis
tuplas_numeros = (1,2,3,4,5)
#Exibindo o 3 item, inicio do indece = 0
print('Exibir Item 03 da Tuplas',tuplas_numeros[3])

#49 Tuplas de cores, alterar sequncia.
#Criacao tupla
tuplas_cores = ('vermelho','azul','verde','azul','amarelo')

#Contagem do item
cor_azul_qtde = tuplas_cores.count('azul')
#Posicao item
cor_verde_pos = tuplas_cores.index('verde')

print(f'Total(is) Cor Azul:',cor_azul_qtde)
print(f'Posicao Cor Verde',cor_verde_pos)


#50 Inventario frutas alterar dados da Lista 

#Criando listas
frutas = ['maçã','banana','cereja']
print(f'Frutas disponiveis',frutas)

#Adicionando item da lista - fim da lista 
frutas.append('laranja')

#Removendo item da lista remove = texto

frutas.remove('banana')

print(f'Frutas disponiveis',frutas)

#Adiciona item por indice - refazendo lista 
frutas.insert(1,'banana')
frutas.pop()

print(f'Frutas disponiveis',frutas)

#Remvendo item por indice - 
del_item = frutas.index('banana')
del frutas[del_item]

#Adicionando item da lista - fim da lista 
frutas.append('laranja')

print(f'Frutas disponiveis',frutas)


# 51 Ordenando lista 

#Lista 
numeros = [3, 1, 4, 1, 5, 9, 2]

#Ordenaso lista
numeros.sort()

#Exibindo resultados
print('Lista ordenada',numeros)


#52 - Lista de numeros de 1 a 10 e calcular sua raiz quadrada

#impostando biblioteca
import math

#Criandi lista vazia
num_lista  = []

#Gerando numeros de 1 a 10
for num in range(1,11):
    num_lista.insert(num,num)

#exibi lista 
print(f'Lista Numeros',num_lista)

result = []
for num in num_lista:
    result.insert(num,num**2)

#exibi lista 
print(f'Lista Resultado Ao **',result)


#53 - Criar dicionario de aluno nome,idade,curso e nota
# informar nota e exclir idade 

dic_aluno =dict()
dic_aluno = {'aluno': 'Elton','idade' : '40', 'curso' : 'TI-AI', 'nota' : '0'}

#Exibir dados
print(f'Dados antes das modificações',dic_aluno)

#atualizando dados chave nota
dic_aluno['nota'] = '10'

#deletando chave 
del dic_aluno['idade']

#Exibir dados
print(dic_aluno)


#Exibindo somente valores
print(dic_aluno.values())
#Exibindo Campos
print(dic_aluno.keys())
#Exibindo tudo
print(dic_aluno.items())


#54 Relação de numeros e seus quadrados 
# Gerando graficos 

import matplotlib.pyplot as plt

# Dados
x = range(1, 11)
y = [i**2 for i in x]

# Criando o gráfico
plt.plot(x, y)

# Adicionando títulos
plt.title("Relação entre Números e Seus Quadrados")
plt.xlabel("Número")
plt.ylabel("Quadrado do Número")

# Mostrando o gráfico
plt.show()


#55 - Gerando Grafico Produtos x Vendas

import matplotlib.pyplot as plt

#Dados 
x = range (1,6)
y = [1000,1500,2500,3200,1100]

#Criando Grafico barras
#plt.plot(x,y)

#Define grafico em barras 
plt.bar(x,y)

#Rotulos
plt.title('Produtos x Vendas')
plt.xlabel('Produtos')
plt.ylabel('Vendas')

#Define escala 
plt.xlim(1,6)

#Exibi grafico
plt.show()









