from colorama import Fore
n = int(input('Digite um número: '))
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(Fore.YELLOW + '{}'.format(i), end=' ')
        cont += 1
    else:
        print(Fore.RED + '{}'.format(i), end=' ')
print(Fore.WHITE +'\nO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print(Fore.WHITE + 'E por isso ele É PRIMO')
else:
    print(Fore.WHITE + 'E por isso ele NÃO É PRIMO')
    