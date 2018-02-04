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
print('PAUSA')

novo = 1
while novo != 0:
    novo = int(input('Quantos termos você quer mostrar a mais? '))
    for i in range(1, novo + 1):
        print('{}'.format(pa), end=' -> ')
        pa += razao
        cont += 1
    if novo > 0:
        print('PAUSA')
print('Progressão finalizada com {} termos mostrados'.format(cont))