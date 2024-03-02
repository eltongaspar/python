# Manipulacao de arquivos 
# r - leitura
# a - apend / incrementar
# w - escrita
# r+ - leitura + escrita
# x - criar arquivo 

#Modo	Resultado
#'r'	Abre o arquivo para leitura. Esse é o padrão, caso o modo não seja especificado.
#'w'	Abre o arquivo para escrita e trunca o seu conteúdo. Nesse modo, tudo o que estiver escrito no arquivo é perdido. Se o arquivo não existir, ele é criado.
#'x'	Cria um arquivo novo, aberto para escrita no “modo de criação exclusiva”. Esse modo significa que o arquivo não pode existir antes de ser aberto. Se o arquivo já existir, um erro é gerado.
#'a'	Abre o arquivo para escrita sem truncar seu conteúdo. Os dados são escritos no final do arquivo. Se o arquivo não existir, ele é criado.
#'b'	Usado em conjunto com os modos anteriores para abrir um arquivo binário. Por exemplo, 'rb' abre um arquivo em modo binário para leitura e 'wb' abre um arquivo em modo binário para escrita.
#'t'	Abre o arquivo em modo texto. Esse é o padrão, então o uso desse modo é opcional. Por exemplo, o modo 'r' funciona de mesma maneira que o modo 'rt'.
#'+'	Abre o arquivo para leitura e escrita. Nesse caso, o arquivo não é truncado. Exemplo: 'r+' A escrita sempre acontece no fim do arquivo.


import os

#arquivo = open('D:/Dados/arquivo.txt', 'a')
#print(arquivo.readable())
#print(arquivo.read())
#print(arquivo.readline())
#print(arquivo.readlines())
#lista = arquivo.readlines()
#print(lista)

#arquivo.write('Teste\n')
#os.remove('D:/Dados/arquivo.txt')

if os.path.exists('D:/Dados/arquivo.txt'):
    print('Arquivo Existe, apagado!')
    os.remove('D:/Dados/arquivo.txt')
else: 
    print('Hum, não achei o arquivo:(!')


#arquivo.close()
