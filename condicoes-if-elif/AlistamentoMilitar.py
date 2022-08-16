# Alistamento Militar - Exercício 39

from time import sleep
from datetime import date

print('*'* 30)
print('Bem vindo ao sistema de analise de Alistamento Militar!')
sleep(2)

anoAtual = date.today().year
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
sleep(1)
print(f'Você nasceu em {anoNasc} e em {anoAtual} está com {idade} anos.')

if idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Faltam {saldo} anos para seu alistamento')
elif idade > 18:
    saldo = 18 - idade
    print(f'Você deveria ter se alistado há {saldo} ano(s) atrás.')