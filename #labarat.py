#Python
import random

# Definir as cartas
naipes = ["Ouro", "Espada", "Copo", "Pau"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Criar a pilha de cartas
baralho = []
for naipe in naipes:
  for valor in valores:
    carta = naipe + " " + valor
    baralho.append(carta)

# Embaralhar o baralho
random.shuffle(baralho)

# Distribuir as cartas
jogador1 = []
jogador2 = []

for i in range(len(baralho)):
  if i % 2 == 0:
    jogador1.append(baralho[i])
  else:
    jogador2.append(baralho[i])

# Mostrar as cartas do jogador 1
print("Cartas do Jogador 1:")
for carta in jogador1:
  print(carta)

# Mostrar as cartas do jogador 2
print("\nCartas do Jogador 2:")
for carta in jogador2:
  print(carta)

# Implementar a lógica do jogo (opcional)
# ...