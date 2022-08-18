# Jogo do Par ou Ímpar - Exercício 68

'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

vitoria = 0
while True:
    jogador = int(input('Digite um valor de 1 a 10: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]\n')).strip().upper()[0]# pegando so a primeira letra digitada e convertendo para sempre aceitar
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Você Perdeu! DEU ÍMPAR!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
        else:
            print('Você Perdeu! DEU PAR!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes!')