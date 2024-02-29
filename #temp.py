#temp


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
















       

