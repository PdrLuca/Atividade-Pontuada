import os
os.system("clear")

#Questão 2.

nome = input("Digite seu nome: ")
sexo = str(input("Digite seu sexo: ")).lower()
estado_civil = str(input("Digite seu estado civil: ")).lower()

match sexo and estado_civil:
    case "F" | "casada":
        tempo_de_casada = input("Digite seu tempo de casada: ")
        print("==FIM==")
    case _:
        print("==FIM==")

print(nome)
print(sexo)
print(estado_civil)


    
