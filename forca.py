import random

def jogar():

    print("***************************************")
    print("*******Bem Vindo ao jogo da Forca******")
    print("***************************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    enforcou = False
    acertou  = False
    erros = 0
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra você deseja chutar?")
        chute = chute.strip().upper() #remove os espaços que o usuário digitar
        
        if(chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra #A letra chutada vai ser substituída na posição do index.
                index += 1
        else:
            erros += 1

        enforcou = erros == 6 #quando der 6 erros ele ira retornar o valor True, parando o loop do while
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Parabéns, você ganhou o jogo da Forca :] ")
    else:
        print("Você perdeu :[ ")

    print("Fim do jogo")

if(__name__ ==  "__main__"):
    jogar() 