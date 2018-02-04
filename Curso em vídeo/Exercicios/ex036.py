valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? ')) * 12
prestacao = valor / anos
print('Para pagar uma casa de de R${:.2f} em {:.0f} vezes a prestação será de R${:.2f} por mês'.format(valor, anos, prestacao))

if prestacao > (salario * 0.3):
    print('Empréstimo NEGADO')
else:
    print('Empréstimo pode ser CONCEDIDO')
