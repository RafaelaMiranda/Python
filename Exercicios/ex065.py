continuar = 'S'
soma = cont= maior = menor = 0
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    continuar = str(input('Quer continuar: [S/N] ')).upper()
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
    