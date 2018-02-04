soma = 0
cont = 0
for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('-=' * 25)
if cont > 1:
    print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
elif cont == 1:
    print('Você informou 1 número PAR e a soma foi {}'.format(soma))
else:
    print('Você não informou números PARES')
print('-=' * 25)