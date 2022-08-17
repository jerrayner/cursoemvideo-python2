# Validação de Dados - Exercício 57
'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

from colorama import Fore, Back, Style, init, deinit

sexoUsuario = str(input('Digite seu sexo: \n [ M ] | [ F ]\n    ')).strip().upper()[0]

while sexoUsuario != 'M' and sexoUsuario != 'F':
    sexoUsuario = str(input('Dados inválidos, digite novamente seu sexo: \n [ M ] | [ F ]\n    ')).strip().upper()[0]
print(f'Sexo {sexoUsuario} armazenado.')