print('Gerador de PA')
print('-=' * 15)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
pa = termo
while cont < 10:
    print('{}'.format(pa), end=' -> ')
    pa += razao
    cont += 1
print('FIM')