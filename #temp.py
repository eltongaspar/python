#temp




# Numeros Primos 
# Diisivel por 1 por ele mesmo

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










       

