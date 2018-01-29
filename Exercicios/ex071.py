_50 = _20 = _10 = _01 = 0
print('=' * 30)
print('BANCO BRUGNARO')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
sobra = valor
while sobra > 0:
    if sobra > 50:
        _50 = (valor // 50)
        print('Total de {} cédulas de R$50'.format(_50))
        sobra = valor - (_50 * 50)
    if sobra > 20:
        _20 = (sobra // 20)
        print('Total de {} cédulas de R$20'.format(_20))
        sobra -= (_20 * 20)
    if sobra > 10:
        _10 = (sobra // 10)
        print('Total de {} cédulas de R$10'.format(_10))
        sobra -= (_10 * 10)
    if sobra > 1:
        _01 = (sobra // 1)
        print('Total de {} cédulas de R$1'.format(_01))
    break
print('=' * 30)
print('Volte sempre ao BANCO BRUGANARO! Tenha um bom dia!')