# Calculo do Fatorial - Exercicio 60
'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120 '''
from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: \n'))
c = num
fatorial = 1
print(f'Calculando os fatoriais de {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial += c
    c -= 1
print(f'{fatorial}')
