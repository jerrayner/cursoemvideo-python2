# Tratando Vários Valores - Exercício 64

cont = n = soma = 0

while n != 999:
    n = int(input('Digite um número: \n[Digite 999 para parar]\n'))
    if n != 999:
        soma += n
        cont += 1

print(f'No total, foram {cont} números digitados e a soma entre eles é {soma}.')
