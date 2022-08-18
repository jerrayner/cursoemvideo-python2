# Vários Números com Flag - Exercício 66

'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

soma = cont = 0
while True:
    num = int(input('Digite um número:\n [999 PARA PARAR]\n'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A quantidade de números digitados foram {cont} números,\ne a soma de todos os números digitados é de {soma}.')