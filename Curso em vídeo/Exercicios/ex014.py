temperatura = float(input('Informe a temperatura em °C: '))
conversao = ((temperatura / 5) * 9) + 32
print('A temperatura de {}°C corresponde a {:.1f}°F'.format(temperatura, conversao))