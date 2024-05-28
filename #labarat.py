import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "desenvolvimento", "jogo", "internet", "software"]
    return random.choice(palavras).upper()

def exibir_forca(tentativas):
    estagios = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
              |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
              |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
              |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
              |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
              |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
              |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
              |
        ---------
        """
    ]
    print(estagios[tentativas])

def jogar():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas = 6

    print("Bem-vindo ao jogo da Forca!")
    print("_ " * len(palavra))

    while tentativas > 0:
        letra = input("Digite uma letra: ").upper()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        letras_adivinhadas.add(letra)

        if letra in palavra:
            print(f"Boa! A letra {letra} está na palavra.")
        else:
            tentativas -= 1
            print(f"Errado! A letra {letra} não está na palavra. Você tem {tentativas} tentativas restantes.")
        
        exibir_forca(tentativas)

        palavra_oculta = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])
        print(" ".join(palavra_oculta))

        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra!")
            break
    else:
        print(f"Você perdeu! A palavra era {palavra}.")

if __name__ == "__main__":
    jogar()
