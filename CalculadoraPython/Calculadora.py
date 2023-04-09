n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))

op = int(input('1 - Adição'
           '\n2 - Subtração'
           '\n3 - Multiplicação'
           '\n4 - Divisão: '))
match op:
    case 1:
        op = n1 + n2
    case 2:
        op = n1 - n2
    case 3:
        op = n1 * n2
    case 4:
        op = n1 / n2
    case _:
        op = 'nd'
print('Resultado: ', op)