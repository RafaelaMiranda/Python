barato = cont = mil = total = 0
nomeBarato = ''
while True:
    print('-' * 30)
    print('CADASTRE UM PRODUTO')
    print('-' * 30)
    nome = str(input('Nome: '))
    preco = float(input('Preço: R$'))
    print('-' * 30)
    total += preco
    if preco > 1000:
        mil += 1
    if cont == 0:
        barato = preco
        nomeBarato = nome
    if barato > preco:
        barato = preco
        nomeBarato = nome
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    cont += 1
print('===== FIM DO PROGRAMA =====')
print('O total da compra doi R${:.2f}'.format(total))
if mil > 1:
    print('Temos {} produtos custando mais de R$1000.00'.format(mil))
elif mil == 1:
    print('Temos 1 produto custando mais de R$1000.00')
else:
    print('Não temos produtos custando mais de R$1000.00')
print('O produto mais barato foi {} que custa R${}'.format(nomeBarato, barato))