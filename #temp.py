#temp

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

















       

