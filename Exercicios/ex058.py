from random import randint
numero = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar qual foi?')
palpite = int(input('Qual é seu palpite? '))
cont = 1
while palpite != numero:
    cont += 1
    if palpite > numero:
        print('Menos... Tente mais uma vez')
    else:
        print('Mais... Tente mais uma vez')
    palpite = int(input('Qual é seu palpite? '))
    
if cont == 1:
    print('Acertou na primeira tentativa. Parabéns!')
else:
    print('Acertou com {} tentativas. Parabéns!'.format(cont))