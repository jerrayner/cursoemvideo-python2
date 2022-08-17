# Maior e Menor Peso - Exercício 55
'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

print('*' * 20 + '\n ACADEMIA PERCA PESO \n' + '*' * 20)

maiorPeso = 0
menorPeso = 0
for pessoas in range(1, 6):
    pesos = float(input(f'Digite o peso da {pessoas}ª pessoa? '))
    if pessoas == 1:
        maiorPeso = pesos
        menorPeso = pesos
    else:
        if pesos > maiorPeso:
            maiorPeso = pesos
        if pesos < menorPeso:
            menorPeso = pesos
print(f'O maior peso lido foi de {maiorPeso}Kg.')
print(f'O menor peso lido foi de {menorPeso}Kg.')