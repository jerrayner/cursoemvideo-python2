# Menu com Opções em Python - Exercício 59
'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. '''
from time import sleep

print('-' * 30 + '\n     Sistema de Operações\n' + '-' * 30)
numero1 = int(input(f'Digite um 1º número: \n'))
numero2 = int(input(f'Digite um 2º número: \n'))

opcao = 0
while opcao != 5:
    sleep(1)
    print('-' * 20 + '\n[ 1 ] SOMAR \n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA\n' + '-' * 20)
    opcao = int(input(f'>>> Digite o número correspondente a operação desejada: '))
    sleep(1)
    if opcao == 1:
        somar = numero1 + numero2
        print(f'A soma ente {numero1} + {numero2} é de {somar}!\n')
    elif opcao == 2:
        multiplicar = numero1 * numero2
        print(f'A multiplicação ente {numero1} x {numero2} é de {multiplicar}!\n')
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f'Entre {numero1} e {numero2} o maior valor é {maior}!\n')
    elif opcao == 4:
        print('Informe os novos números desejados: \n')
        numero1 = int(input(f'Digite um 1º número: \n'))
        numero2 = int(input(f'Digite um 2º número: \n'))
    elif opcao == 5:
        print('Até mais!')
else:
    print('Opção inválida. Tente novamente.\n')