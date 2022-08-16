# Comparação de Maior e Menor Números - Exercício 38

from time import sleep

print('Olá! Vamos descobrir qual número é maior que o outro? ')
sleep(2)

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um segundo número inteiro: '))

print('Analisando os números digitados...')
sleep(3)

if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}.')
elif num2 > num1:
    print(f'O número {num2} é maior que o número {num1}.')
elif num1 == num2:
    print(f'Os números {num1} e {num2} são iguais, não existe um maior.')