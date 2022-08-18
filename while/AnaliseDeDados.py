# Analise de Dados do Grupo - Exercício 69

'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

print('-=' * 10)
print('CADASTRO DE PESSOAS')
print('-=' * 10)
print('')
maioridade = homens = mulheres = 0
while True:
    nome = str(input('Digite o nome: ')).strip().title()
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F] ')).strip().upper()[0]
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('-' * 20)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    print('-' * 20)
    if cont == 'N':
        break
print('Encerrando...')
print('')
print(f'{maioridade} pessoas possuem mais de 18 anos.')
print(f'Foram cadastrados ao todo {homens} homens.')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos.')
print('')
print('-=' * 20)