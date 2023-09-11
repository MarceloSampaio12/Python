# Operadores Aritméticos

# == -> Sinal de igual
# + -> Adição Ex: 5+2 == 7
# - -> Subtração Ex: 5-2 == 3 
# / -> Divisão Ex: 5/2 == 2.5
# * -> Multiplicação Ex: 5*2 == 10
# ** -> Potência Ex: 5**2 == 25 ou pode utilizar o 'pow(5,2)', mas perde a ordem de precedência
# // -> Divisão inteira Ex: 5//2 == 2
# % -> Resto da divisão Ex: 5%2 == 1
# 81**(1/2) -> Raíz quadrada, 81**(1/3) -> Raíz cúbica 

# Ordem de precedência
# 1 -> ()
# 2 -> **
# 3 -> *, /, //, %
# 4 -> +, -

# Utilizando operadores aritméticos com String
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome)) # Alinhamento à direita.
print('Prazer em te conhecer {:<20}!'.format(nome)) # Alinhamento à esquerda.
print('Prazer em te conhecer {:^20}!'.format(nome)) # Alinhamento à centralizado.
print('Prazer em te conhecer {:=^20}!'.format(nome)) # Alinhamento à centralizado com o preenchimento do sinal digital, nesse caso o sinal de igual.