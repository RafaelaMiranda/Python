from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = factorial(n)
print('Calculando {}! = '.format(n),end=' ')
while n >= 1:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
print('{}'.format(fatorial))