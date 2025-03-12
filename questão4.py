import os 
os.system("clear")

#Questão 4.

morangos = float(input("Digite a quantidade de morangos (kg):"))
maças = float(input("Digite a quantidade de maças (kg):"))

if morangos <= 5:
    preço_morango = 2.50
else:
    preço_morango = 2.20

if maças <= 5:
    preço_maças = 1.80
else:
    preço_maças = 1.50

total_morango = morangos * preço_morango
total_maças = maças * preço_maças
total_compra = total_morango * total_maças

if (morangos + maças) > 10 or total_compra > 15.00:
    total_compra*=0.90

print(f"Valor a ser pago: R$ {total_compra:.2f}")