# Detector de Palindromo - Exercício 53
'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

print('Um palíndromo é uma frase que lida de trás para frente\ncontinua sendo a mesma frase!\nQuer descobrir se sua frase é um palindromo? \n')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # separando a frase em uma lista/vetor
concatena = ''.join(palavras) # eliminando os espaços da frase
inverso = ''
for letra in range(len(concatena) - 1, -1, -1): # pegando o número de letras da frase, e vai voltando de um em um as letras para que ela seja exibida ao inverso
    inverso += concatena[letra]
print(f'O inverso de {concatena} é {inverso}!')
if inverso == concatena:
    print(f'A frase é um palíndromo!')
else:
    print(f'Não é um palíndromo!')
# print(f'Você digitou a frase {concatena}')