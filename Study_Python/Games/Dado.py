import random

print("************************")
print("****** JOGO DADO *******")
print("************************")

resposta = input("Você gostaria de jogar o dado? (s/n)")

if(resposta == 's'):
    print("Você aceitou jogar")
    numero_dado = random.randrange(1,7)

    print("O número do dado foi", numero_dado)

else:
    print("Que pena, você não quer jogar :(")
