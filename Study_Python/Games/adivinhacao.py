import random

def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação !")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1)Fácil  (2)Médio  (3)Difícil")

    nivel = int (input("Defina o nível"))

    if(nivel==1):
        tentativas=20

    if(nivel==2):
        tentativas=10

    if(nivel==3):
        tentativas=5

    for rodada in range (1,tentativas + 1) :

        print("Tentativas {}  de  {} ".format(rodada, tentativas))
        chute = input("Digite o seu número: ")
        chute = int(chute)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue


        if(acertou):
            print("Você acertou e fez {} pontos !".format(pontos))
            break
        else:
            if(maior):
                print("Você errou :(, seu chute é maior que o número secreto")
            elif(menor):
                print("Você errou :(, seu chute é menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()