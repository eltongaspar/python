#Tuplas
# Tuplas são imutaveis, não pode mudar valores
# Tuplas = ()

Lanche = 'hamburguer'
lanches = ('hamburguer','refri','sorvete','suco')
print(lanches[:2])
print(len(lanches))

for c in lanches:
    print(f'Seu prato é',c)

for cont in range(0,len(lanches)):
    print(f'Seu prato é',lanches[cont])

#Ordenar Campos
print(sorted(lanches))

#lanches[1] = 'combo'

#Junçao de Tuplas
a = (1,2,3)
b = (4,5,6,7)
c = a+b
print(c)

# contador de valores
print(f'Contagem',c.count(7))

# Tamanho da tupla
print(f'Posicao',len(c)) 

# Indice, index
print(f'Index',c.index(7)) 

#Tuplas com dados difentes 
pessoa = ('Elton',39,'M',86)
print(f'{pessoa}')
# Tuplas podemser apagadas por completo, e não por item
#del pessoa[0] - tuple' object doesn't support item deletion
del pessoa # Apagando tuplas
