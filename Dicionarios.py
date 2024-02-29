#Dicionarios 
# Indices literiais
# dicionarios = {}

dados = dict()
dados = {'nome':'Elton','idade':'40'}
print(dados['nome'])
#Adicionando dados 
dados['sexo'] = 'M'
print(dados)
#Deletatando dados 
del dados['sexo']
print(dados)

#Exibindo somente valores
print(dados.values())
#Exibindo Campos
print(dados.keys())
#Exibindo tudo
print(dados.items())

for k,v in dados.items():
    print(k,v)

#Criando listas com dicionarios    
brasil = []
estado = {'uf': 'Sao Paulo','sigla': 'SP'}
estado1 = {'uf': 'Rio de Jneiro','sigla': 'RJ'}
brasil.append(estado)
brasil.append(estado1)
print(brasil)
print(brasil[0]['sigla'])