# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salbruto = int(input('Digite o seu salário para acrescentarmos 15%: '))
aumento = salbruto * 0.15
salfinal = salbruto + aumento
print(f'Salário inicial {salbruto}, aumento {aumento}, novo salário {salfinal}')