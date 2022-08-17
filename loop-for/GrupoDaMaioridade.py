# Grupo da Maioridade - Exercício 54
'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date

print('Vamos verificar quantas pessoas já atingiram a maioridade?')
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print(f'Ao todo são {totalMaior} pessoas maiores de idade.')
print(f'E ao todo são {totalMenor} pessoas menores de idade.')