def jogar():

    print("***************************************")
    print("*******Bem Vindo ao jogo da Forca******")
    print("***************************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou  = False
    letras_acetadas = ["_", "_", "_", "_", "_", "_"]

    print(letras_acetadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra você deseja chutar?")
        chute = chute.strip() #remove os espaços que o usuário digitar
        
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acetadas[index] = letra #A letra chutada vai ser substituída na posição do index.
            index = index + 1

        print(letras_acetadas)

    print("Fim do jogo")

if(__name__ ==  "__main__"):
    jogar() 