# Contagem Regressiva - Exercício 46

import emoji
from time import sleep

print('Prepare-se para a contagem regressiva! ')
sleep(2)
print('Iniciando...')
sleep(3)

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks::fireworks::fireworks:'))