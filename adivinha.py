import random

print("***************************************");
print("Seja bem-vindo a um jogo de Adivinhação");
print("***************************************");

numero_secreto = random.randrange(1,101)
numero_tentativas = 0
tentativa_atual = 1
pontos = 1000

print("Qual dificuldade voce deseja?")
print("(1) Facil (2) Medio (3) Dificil (4) Extremo")
nivel = int(input("Define o nivel: "))

if(nivel == 1):
    numero_tentativas = 20
elif(nivel == 2):
    numero_tentativas = 15
elif(nivel == 3):
    numero_tentativas = 10
else:
    numero_tentativas = 3


while(tentativa_atual <= numero_tentativas):
    print("Tentativa {} de {}"  .format(tentativa_atual, numero_tentativas))
    chute_str = input("Digite o seu numero: ");

    chute = int(chute_str)
    ##print("Voce digitou o numero: ", chute)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero maior que 0 e menor que 100")
        continue

    acertou = numero_secreto == chute
    menor   = numero_secreto < chute
    maior   = numero_secreto > chute

    if(acertou):    
        print("Voce Ganhou!!!")
        break
    else: 
        if(maior):
            print("Voce errou, chutou um numero que esta abaixo do numero secreto.")
        elif(menor):
            print("Voce errou, chutou um numero que esta acima do numero secreto.")
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos    
    tentativa_atual = tentativa_atual + 1

print("Fim do jogo")