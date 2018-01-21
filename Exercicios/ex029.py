velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    ultrapassou = velocidade - 80
    pagar = ultrapassou * 7.00
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(pagar))
print('Tenha um bom dia! Dirija com segurança!')