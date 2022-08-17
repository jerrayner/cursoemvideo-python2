# Jogo de Adivinhação com While - Exercício 58
'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''


from time import sleep
from random import randint

computador = randint(0, 10)
print('*' * 30 + '\n ADIVINHE O NÚMERO! \n' + '*' * 30)
sleep(1)
print('Irei pensar em um número de 0 a 10.. tente adivinhar qual será! \nO jogo só será finalizado quando você acertar !')
sleep(1)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente novamente.')
        elif jogador > computador:
            print('Menos.. Tente novamente.')
print('Acertou!')
print(f'\nVocê levou {palpites} tentativas para acertar!')