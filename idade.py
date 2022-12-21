idade_maior = 0

i = 1

quantidade_pessoas = input("Quantas pessoas voce deseja saber que sao maiores? ")

while i <= int(quantidade_pessoas):
    idade = input("Digite a idade: ")
    i = i + 1
    if int(idade) >= 18:
        idade_maior = idade_maior + 1

print("A quantidade de pessoas maiores de 18 anos foram :", idade_maior)

