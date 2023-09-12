# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Calculando direto no print.
m = float(input('Digite um valor em metros: '))
print(f'Valor digitado {m}m, convertido em centímetros fica {m*100}cm e convertido em milímetros fica {m*1000}mm!')

# Utilizando variável para calculo.
metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mm = metros * 1000
print(f'Valor digitado {metros}m, convertido em centímetros fica {cm}cm e convertido em milímetros fica {mm}mm!')
