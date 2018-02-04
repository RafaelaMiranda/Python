cont = soma = n = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print('A soma dos {} valores foi {}!'.format(cont, soma))
