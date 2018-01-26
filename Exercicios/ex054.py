from datetime import datetime
anoAtual = datetime.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input('Em que ano a {}ª nasceu? '.format(i)))
    idade = anoAtual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
if maior > 1:
    print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
elif maior == 1:
    print('Ao todo tivemos 1 pessoa maior de idade')
else:
    print('Não tivemos pessoas maiores de idade')

if menor > 1:
    print('E também tivemos {} pessoas menores de idade'.format(menor))
elif maior == 1:
    print('E também tivemos 1 pessoa menor de idade')
else:
    print('E não tivemos pessoas menores de idade')

    
