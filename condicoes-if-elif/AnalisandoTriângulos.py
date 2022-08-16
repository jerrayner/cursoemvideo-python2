# Analisando Triângulo - Exercício 42

med1 = float(input('Insira a primeira medida: '))
med2 = float(input('Insira a segunda medida: '))
med3 = float(input('Insira a terceira medida: '))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('Os seguimentos acima PODEM formar um triângulo...')
    if med1 == med2 == med3:
        print('EQUILÁTERO!')
    if med1 != med2 != med3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo.')