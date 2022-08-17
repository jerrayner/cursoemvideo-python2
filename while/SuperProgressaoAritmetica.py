# Super Progressão Aritmetica - Exercício 62
'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print(f'Gerador de PA\n{"="*35}')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

c = False
cont = 0
new = 10

while c != True:
    if c == False and cont < 10:
        print(f'{termo}', end=' - ')
        cont += 1
        if cont < 10:
            termo = termo + razao
    elif cont >= new:
        new = int(input(f'\nQuantos termos voce quer mostrar a mais? '))
        c2 = 0
        if new == 0:
            c = True
        while c2 < new and new != 0:
            termo = termo  + razao
            print(f'{termo}', end=' - ')
            cont += 1
            c2 += 1
print(f'Progressão finalizada com {cont} termos mostrados.\nFIM')