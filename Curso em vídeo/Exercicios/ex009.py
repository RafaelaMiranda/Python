tabuada = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for n in range(1, 11):
    print('{} x {} = {}'.format(tabuada, n, (tabuada * n)))
print('-' * 12)