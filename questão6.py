import os
os.system("clear")

#Questão 6.

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))


soma = primeira_nota + segunda_nota
media = soma/2

print(f"media: {media}")

if media >= 6:
    print("Parabéns!")
elif 4 <= media < 6:
    print("Recuperação!")
elif media < 4:
    print("Reprovado")

print(media)