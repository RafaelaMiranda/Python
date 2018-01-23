from time import sleep
from random import randint

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jog = int(input('Qual é a sua jogada? '))

comp = randint(0,2)

sleep(0.7)
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
print('-=' * 10)

print('Computador jogou',end = ' ')
if comp == 0:
    print('Pedra')
elif comp == 1:
    print('Papel')
elif comp == 2:
    print('Tesoura')


print('Jogador jogou', end = ' ')
if jog == 0:
    print('Pedra')
elif jog == 1:
    print('Papel')
elif jog == 2:
    print('Tesoura')

print('-=' * 10)

if jog == 0 and comp == 2 or jog == 1 and comp == 0 or jog == 2 and comp == 1:
    print('JOGADOR VENCE')
elif jog == 0 and comp == 0 or jog == 1 and comp == 1 or jog == 2 and comp == 2:
    print('EMPATE')
else:
    print('COMPUTADOR VENCE')

    


