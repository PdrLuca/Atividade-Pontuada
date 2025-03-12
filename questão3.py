import os
os.system("clear")

#Questão 3.

valor_A = int(input("Digte o valor A: "))
valor_B = int(input("Digte o valor B: "))

if valor_A == valor_B:
    soma = valor_A + valor_B
    print("soma:", soma)
else:
    multiplicação = valor_A * valor_B
    print("multiplicação:", multiplicação)