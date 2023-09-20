# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = int(input('Digite o preço do produto: '))
desc = preço * 0.05
pnovo = preço + desc
print(f'preço {preço}, desconto {desc}, preço novo {pnovo} ')