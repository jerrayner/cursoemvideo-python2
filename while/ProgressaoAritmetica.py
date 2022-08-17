# Progressao Aritmetica - Exercício 61
'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

num1 = int(input('Valor do primeiro termo: '))
razao = int(input('Valor da razão: '))
n10 = num1 +(10-1)*razao
n = 10
a = 0
print(n10)
print(f'Os 10 primeros termo da P.A de razão {razao} e o primero termo {num1}')
while a!= n10:
    a = num1 + (10-n)*razao
    n=n-1
    print(a,end=',' if a != n10 else '...')
print('\nFIM! ')