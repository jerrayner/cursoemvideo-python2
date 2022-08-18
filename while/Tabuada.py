# Tabuada Versão 3.0 - Exercício 67
'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
while True:
    print('-' * 40 + '\n        TABUADA DE MULTIPLICAÇÃO\n' + '-' * 40)
    num = int(input('Digite o número desejado para ver sua tabuada: \n'))
    print('-' * 40, '\n')
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}\n')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO.')