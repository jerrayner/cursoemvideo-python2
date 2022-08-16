# Versão de Tabuada com For - Exercício 49

from time import sleep

print('#*' * 20 )
print('TABUADA ONLINE!')
sleep(1)
numero = int(input('Digite um número para ver sua tabuada de multiplicação:'))
for c in range(1, 11):
    print(f'{numero} X {c:2} = {numero*c}')
