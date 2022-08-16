''' Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
from datetime import date
from time import sleep

print('*=' * 10 + ' Confederação Nacional de Natação ' + '*=' * 10)
sleep(2)
print('Bem vindo ao nosso sistema de verificação de categoria dos atletas!')
sleep(1)
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print(f'O atleta tem {idade} anos.')
sleep(2)

if idade <= 9 and idade >= 1:
    print('Classificação: MIRIM')
elif idade >= 10 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade >= 20 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 26:
    print('Classificação: MASTER')
elif idade < 1:
    print('Idade inválida.')