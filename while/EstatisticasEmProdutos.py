# Estatísticas em Produtos - Exercício 70
'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

valorTotal = totalMil = menorPreco = cont = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input(f'Digite o preço do produto: '))
    cont += 1
    valorTotal += preco
    if preco > 1000:
        totalMil += 1
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais algum produto? [S/N]\n')).strip().upper()[0]
    if resp == 'N':
        break
print('-'* 20 +' FIM DO CADASTRO ' + '-' * 20)
print(f'O total da compra foi de R${valorTotal:.2f}')
print(f'Foram cadastrados {totalMil} produtos que custam mais de R$1000,00.')
print(f'O produto mais barato foi {barato} que custa R${menorPreco:.2f}')
