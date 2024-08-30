import random

# --- Funções auxiliares (equivalentes às suas funções .prg) ---

import random

def GeraNumAleatMinMax(quantidade, minimo, maximo):
    """Gera uma lista de números aleatórios, permitindo duplicatas."""
    numeros = random.choices(range(minimo, maximo + 1), k=quantidade)
    return numeros


def MsgLoad(mensagem, qtde_msgs=1):
    """Simula a função MsgLoad do Clipper."""
    print(mensagem)

def GeraBarAuto(quantidade, minimo, maximo):
    """Gera um baralho ordenado."""
    baralho = []
    for i in range(minimo, maximo + 1):
        baralho.append(i)
    return baralho

def FuncaoTelaPergunt():
    """Perguntas para a Funcao Tela Parada e Tempo - Wait e Inkey"""

    lWait = False
    lInkey = False
    iWaittValid = 0
    iInkeytValid = 1
    iTempInkey = 1

    while iWaittValid != 1 and iWaittValid != 2:
        iWaittValid = int(input('Deseja ter Parada de Tela (Wait) - 1-Sim/2-Nao: '))

        if iWaittValid == 1:
            lWait = True
        elif iWaittValid == 2:
            lWait = False

    while iInkeytValid != 1 and iInkeytValid != 2:
        iInkeytValid = int(input('Deseja ter Tempo de Tela (Inkey) - 1-Sim/2-Nao: '))

        if iInkeytValid == 1:
            lInkey = True
            iTempInkey = int(input('Informe o Tempo de Espera de Tela em segundos: '))
        elif iInkeytValid == 2:
            lInkey = False

    return lWait, lInkey, iTempInkey



def FuncaoTela():
    """Simula a função FuncaoTela do Clipper."""
    input("Pressione Enter para continuar...")

# --- Fim das funções auxiliares ---

def main():
    # Baralho (equivalente ao seu array multidimensional)
    baralho = [
        [101, 3, "A", "Copas"], [101, 4, "A", "Ouro"], [101, 5, "A", "Paus"], [101, 6, "A", "Espadas"],
        [102, 3, "2", "Copas"], [102, 4, "2", "Ouro"], [102, 5, "2", "Paus"], [102, 6, "2", "Espadas"],
        [103, 3, "3", "Copas"], [103, 4, "3", "Ouro"], [103, 5, "3", "Paus"], [103, 6, "3", "Espadas"],
        [104, 3, "4", "Copas"], [104, 4, "4", "Ouro"], [104, 5, "4", "Paus"], [104, 6, "4", "Espadas"],
        [105, 3, "5", "Copas"], [105, 4, "5", "Ouro"], [105, 5, "5", "Paus"], [105, 6, "5", "Espadas"],
        [106, 3, "4", "Copas"], [106, 4, "6", "Ouro"], [106, 5, "6", "Paus"], [106, 6, "6", "Espadas"],
        [107, 3, "7", "Copas"], [107, 4, "7", "Ouro"], [107, 5, "7", "Paus"], [107, 6, "7", "Espadas"],
        [108, 3, "8", "Copas"], [108, 4, "8", "Ouro"], [108, 5, "8", "Paus"], [108, 6, "8", "Espadas"],
        [109, 3, "9", "Copas"], [109, 4, "9", "Ouro"], [109, 5, "9", "Paus"], [109, 6, "9", "Espadas"],
        [110, 3, "10", "Copas"], [110, 4, "10", "Ouro"], [110, 5, "10", "Paus"], [110, 6, "10", "Espadas"],
        [111, 3, "Q", "Copas"], [111, 4, "Q", "Ouro"], [111, 5, "Q", "Paus"], [111, 6, "Q", "Espadas"],
        [112, 3, "J", "Copas"], [112, 4, "J", "Ouro"], [112, 5, "J", "Paus"], [112, 6, "J", "Espadas"],
        [113, 3, "K", "Copas"], [113, 4, "K", "Ouro"], [113, 5, "K", "Paus"], [113, 6, "K", "Espadas"]
    ]

    infinito = 0
    while infinito != 1 and infinito != 2:
        infinito = int(input('Deseja ativar Modo Loop: 1-Sim/2-Nao: '))

        if infinito == 1:
            lInfinit = True

        if infinito == 2:
            lInfinit = False

    if not lInfinit:
        FuncaoTelaPergunt()
        FuncaoTela()

    while lInfinit:
        # Gerando Baralho Auto
        MsgLoad('Criando Baralho Auto', 5)
        baralho_gerado = GeraBarAuto(13, 101, 113)

        # Exibe Baralho
        MsgLoad('Carregando Baralhos', 5)
        print(baralho)

        FuncaoTela()

        # Embaralhando Cartas
        MsgLoad('Embaralhando Cartas Resultado', 5)
        cartas_embaralhadas = GeraNumAleatMinMax(52, 101, 113)

        FuncaoTela()

        # Embaralhando Naipes
        MsgLoad('Embaralhando Naipes', 5)
        naipes_embaralhados = GeraNumAleatMinMax(52, 3, 6)

        FuncaoTela()

        # Cartas Embaralhadas (Cartas + Naipes)
        cartas_embaralhadas_completo = []
        for i in range(52):
            carta = cartas_embaralhadas[i]
            naipe = naipes_embaralhados[i]

            # Encontrando a descrição da carta e naipe
            for carta_info in baralho:
                if carta_info[0] == carta and carta_info[1] == naipe:
                    cCartaDesc = carta_info[2]
                    cNaipeDesc = carta_info[3]
                    break

            cartas_embaralhadas_completo.append([carta, naipe, cCartaDesc, cNaipeDesc])

        MsgLoad('Carregando Baralhos Embaralhados', 5)
        print(cartas_embaralhadas_completo)

        FuncaoTela()

        # Embaralhando 21 Cartas
        MsgLoad('Cartas Embaralhadas (21 Cartas)', 5)
        for i in range(21):
            print(cartas_embaralhadas_completo[i])

        FuncaoTela()

        # Embaralhando 21 Cartas (Matriz 7x3)
        matriz_cartas = []
        indice_carta = 20
        for i in range(3):
            linha = []
            for j in range(7):
                linha.append(cartas_embaralhadas_completo[indice_carta])
                indice_carta -= 1
            matriz_cartas.append(linha)

        MsgLoad('Cartas Embaralhadas (21 Cartas Matriz 7x3)', 5)
        print(matriz_cartas)

        FuncaoTela()

        # Pesquisa de Carta (Automatizada)
        MsgLoad('Pesquisa Auto - Carta Aleatoria', 5)
        carta_pesquisa = random.randint(101, 113)
        print(f"Carta para pesquisa: {carta_pesquisa}")

        MsgLoad('Pesquisa Auto - Naipe Aleatoria', 5)
        naipe_pesquisa = random.randint(3, 6)
        print(f"Naipe para pesquisa: {naipe_pesquisa}")

        FuncaoTela()

        # Encontrando a posição da carta na lista
        for i, carta_info in enumerate(cartas_embaralhadas_completo):
            if carta_info[0] == carta_pesquisa and carta_info[1] == naipe_pesquisa:
                posicao_carta = i
                break

        print("Posicao Matriz")
        print(posicao_carta)

        FuncaoTela()

        print("Cartas")
        print(cartas_embaralhadas_completo[posicao_carta])

        FuncaoTela()

        # Troca de Carta (Automatizada)
        MsgLoad('Troca Auto - Carta Aleatoria', 5)
        nova_carta = random.randint(101, 113)
        print(f"Nova carta: {nova_carta}")

        MsgLoad('Troca Auto - Naipe Aleatoria', 5)
        novo_naipe = random.randint(3, 6)
        print(f"Novo naipe: {novo_naipe}")

        FuncaoTela()

        # Encontrando a nova carta no baralho
        for carta_info in baralho:
            if carta_info[0] == nova_carta and carta_info[1] == novo_naipe:
                nova_carta_info = carta_info
                break

        # Substituindo a carta na matriz
        matriz_cartas[posicao_carta // 7][posicao_carta % 7] = nova_carta_info

        MsgLoad('Cartas Trocadas', 5)
        print('Posicao')
        print(posicao_carta)

        FuncaoTela()

        print('Cartas Trocadas')
        print(matriz_cartas[0][0])  # Posição 1

        FuncaoTela()

        MsgLoad('Cartas Trocadas Pos. 1 a 7 / 8 a 14 / 15 a 21)', 5)
        print(matriz_cartas)

        FuncaoTela()

        # Exibindo as primeiras 11 cartas
        MsgLoad('Cartas Embaralhadas (21 Cartas)', 5)
        for i in range(11):
            print(cartas_embaralhadas_completo[i])

        FuncaoTela()

        # Exibindo todas as cartas do baralho
        MsgLoad('Cartas do Baralho', 5)
        for carta_info in baralho:
            print(carta_info)

        FuncaoTela()

        # Exibindo todas as cartas embaralhadas
        MsgLoad('Cartas Embaralhadas', 5)
        for carta_info in cartas_embaralhadas_completo:
            print(carta_info)

        FuncaoTela()

if __name__ == "__main__":
    main()
