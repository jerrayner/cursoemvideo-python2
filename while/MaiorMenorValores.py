# Maiores e Menores Valores - Exercício 65

lista = []
soma = media = quantidade = 0
pergunta = 'S'
while pergunta in 'Ss':
    n = int(input('Digite um número: '))
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()
    soma += n
    quantidade += 1
    lista += [n]
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {media}')
print(f'O maior valor digitado foi ', max(lista))
print(f'E o menor valor digitado  foi ', min(lista))