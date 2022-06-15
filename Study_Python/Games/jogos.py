import forca
import adivinhacao

def escolhe_jogo():

    print("***********************************")
    print("***** Escolha o seu jogo ! ********")
    print("***********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo ==1):
        print("Jogo da forca")
        forca.jogar()
    elif(jogo==2):
        print("Jogo da adivinhação")
        adivinhacao.jogar()

if(__name__=="__main__"):
    escolhe_jogo()