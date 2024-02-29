# Listas 
#Listas = []

lanches = ['refri','hamburguer','sorvete','suco']
print(lanches)

#incluindo item no fim da lista 
lanches.append('cook') 
print(lanches)

# incluindo item em qq posição da lista 
lanches.insert(0,'hot dog') 
print(lanches)

#Excluindo itens 
del lanches[3]
lanches.pop(4)
lanches.remove('hot dog')
# Valida item antes da exclusa 
if 'hot dog' in lanches:
    lanches.remove('hot dog')
#Exclui ultimo item da lista
lanches.pop
print(lanches)

# Criando listas 
valores = list(range(4,11))
print(valores)
#Ordenando lista
valores.sort
print(valores)
#Ordenado lista reversa
valores.sort(reverse=True)
print(valores)
print(len(valores))
del valores



import random 
min = 0
max = 100
cont = 1

def num_aleat(min,max):
    num = random.randrange(min,max)
    #print(f'Numero Gerado',num)
    return num

valores = list(range(0,0))

for cont in range(max):
    valores.insert(cont,(num_aleat(min,max)))
    cont += 1
  
print(valores)
print(len(valores))

valores = list(range(0,0))
cont = 1
while cont <= max:
    valores.insert(cont,(num_aleat(min,max)))
    cont += 1
   

print(valores)
print(len(valores))



