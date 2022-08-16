# Progressão Aritmética - Exercício 51
'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print('='* 25 + '\n 10 TERMOS DE UMA PA \n' + '=' * 25)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo =  primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' → ')
print('FIM')