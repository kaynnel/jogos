import random

def jogar():

    print("Bem vindo ao jogo de Adivinhação!")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100

    print("Escolha o nível de dificuldade: ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 5
    elif(nivel == 2):
        total_de_tentativas = 10
    else:total_de_tentativas = 15

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Digite um número ente 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, o seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou, o seu chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()