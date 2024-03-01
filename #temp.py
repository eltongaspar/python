#temp

# 33 Lista de palavras proibidas 

def bloqtext(texto):
    import re
    lisbloqtext = ['teste','curintia']

    qtdetext = len(lisbloqtext)
    cont = 0
    
    while cont <= qtdetext:
        if re.search(lisbloqtext,text):
            print('Texto localizado',cont)
        else:
            print('Texto não localizado',cont)
        cont += 1


print('Informe um texto a ser analisado com palavras proibidas')
text = input('Texto:  ')
bloqtext(text)

#textexib = bloqtext(text)















       

