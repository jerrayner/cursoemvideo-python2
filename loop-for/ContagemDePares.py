# Contagem de Pares - Exercício 47

from itertools import count
from time import sleep


print('Você sabe quais são os números pares do intervalo de 1 e 50?')
sleep(2)
print('Vou te mostrar!')
sleep(1)

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=" ")
print('Até logo!')