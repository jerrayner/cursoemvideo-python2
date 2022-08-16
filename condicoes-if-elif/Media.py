# Calculando Média Escolar - Exercício 40

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota obtida: '))
nota2 = float(input('Digite a segunda nota: ')

media = (nota1 + nota2) / 2

if media >= 7.0 and media < 10:
    print(f'O aluno {nome} teve a media de {media} e está APROVADO.')
elif media >= 5.0 and media <= 6.9:
    print(f'O aluno {nome} teve a media de {media} e está em RECUPERAÇÃO.')
elif media < 5.0:
    print(f'O aluno {nome} teve a media de {media} e está REPROVADO.')
elif media > 10:
    print('Valor inválido. Tente novamente.')