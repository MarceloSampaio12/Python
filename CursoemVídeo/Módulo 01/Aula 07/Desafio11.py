# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
area = largura * altura
tinta = area / 2
print(f'A área é {area} e a vai precisar de {tinta} litros de tinta')