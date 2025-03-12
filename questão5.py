import os
os.system("clear")

#Questão 5.

primeiro_numero = int(input("Digite um numero: "))
operador = input("Digite uma operação que deseja (+ - * /): ")
segundo_numero = int(input("Digite um numero: "))

match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    
    case "-":
        resultado = primeiro_numero - segundo_numero
    
    case "/":
        resultado = primeiro_numero / segundo_numero
    
    case "*":
        resultado = primeiro_numero * segundo_numero
    
    case _:
        resultado ="opção inválida."

print(f"Primeiro numero: {primeiro_numero}")
print(f"Operação: {operador}")
print(f"Segundo numero: {segundo_numero}")
print(f"Resultado: {resultado}")
