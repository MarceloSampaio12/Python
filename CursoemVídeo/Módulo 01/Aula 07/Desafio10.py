# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.

dinheiro = float(input('Digite quanto você tem na carteira para fazer a conversão em dólar: '))
dolar = dinheiro * 3.27
print(f'Saldo em reais R${dinheiro} - Saldo em dólar U${dolar}')