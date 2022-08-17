# Sequencia de Fibonacci = Exercício 63
''' Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8 '''

n = int(input('Quantos números da sequência você gostaria de mostrar?'))
a = 1
b = 0
c = 0
cont = 0
cont1 = 1
cont2 = 2
cont3 = 3
while cont < n+1:
    if cont == 0:
        b=a+a
        print(b)
        cont+=1
    elif cont1==cont:
        c = a+b
        print(c)
        cont+=1
        cont1+=3
    elif cont2==cont:
        a = c + b
        print(a)
        cont +=1
        cont2+=3
    elif cont3==cont:
        b = a + c
        cont+=1
        cont3+=3
        print(b)