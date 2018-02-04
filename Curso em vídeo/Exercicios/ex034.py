salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = salario + (salario * 0.1)
else:
    aumento = salario + (salario * 0.15)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento))