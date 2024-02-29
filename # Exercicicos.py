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


