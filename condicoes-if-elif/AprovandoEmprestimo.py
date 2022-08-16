# Aprovando Empréstimo - Exercício 36

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

print('Vamos realizar a analise do seu emprestimo?')
sleep(1)
valorCasa = float(input('Digite o valor da casa desejada: R$'))
salarioComprador = float(input('Digite seu salário: R$'))
anosFinanciamento = int(input('Quantos anos de financiamento? '))
prestacao = valorCasa / (anosFinanciamento * 12)
minimo = salarioComprador * 30 / 100

print(f'Para pagar uma casa de R${valorCasa:.2f} em {anosFinanciamento} anos a prestação será de {prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo aceito!')
else:
    print('Empréstimo negado!')
