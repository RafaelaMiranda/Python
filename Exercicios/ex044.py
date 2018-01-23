print('=' * 10, end='')
print('LOJAS RAFAELA',end='')
print('=' * 10)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = input('Qual é a opção? ')

if opcao == '1':
    pagamento = preco - (preco * 0.1 )
    total = pagamento
elif opcao == '2':
    pagamento = preco - (preco * 0.05 )
    total = pagamento
elif opcao == '3':
    pagamento = preco / 2
    total = preco
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(pagamento))
elif opcao == '4':
    parc = int(input('Quantas parcelas? '))
    juros = preco * 0.2
    total = preco + juros
    pagamento = total / parc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc, pagamento))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))