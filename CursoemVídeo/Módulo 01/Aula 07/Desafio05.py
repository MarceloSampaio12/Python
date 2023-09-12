# Desafio 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e se antecessor.

num = int(input('Digite um número: '))
print(f'O número que você digitou: {num} seu sucessor é: {num+1} e seu antecessor é {num-1}!')

# Outra maneira seria criar as variáveis sucessor e antecessor.
n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print(f'Número digitado: {n}, seu sucessor: {s} e seu antecessor: {a}!')