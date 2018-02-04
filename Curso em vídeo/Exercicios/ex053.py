frase = str(input('Digite uma frase: ')).upper().strip()
juncao = ''.join(frase.split())
inverso = juncao[::-1]
print('O inverso de {} é {}'.format(juncao, inverso))
if juncao == inverso:
    print('Temos um palíndrono')
else:
    print('A frase digitada não é um palíndrono')