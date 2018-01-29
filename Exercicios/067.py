while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 30)
    if n < 0:
        break
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n * i))
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')