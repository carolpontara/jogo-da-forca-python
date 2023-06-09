import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogo']
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem", len(palavra), "letras.")

    while True:
        print("\n" + "-" * 30)
        print("Letras corretas: ", end="")
        for letra in letras_corretas:
            print(letra, end=" ")
        print("\nLetras erradas: ", end="")
        for letra in letras_erradas:
            print(letra, end=" ")

        if tentativas == 0:
            print("\n\nVocê perdeu! A palavra correta era:", palavra)
            break

        if len(letras_corretas) == len(set(palavra)):
            print("\n\nParabéns! Você venceu!")
            break

        palpite = input("\n\nDigite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if palpite in palavra:
            letras_corretas.append(palpite)
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

jogar_forca()
