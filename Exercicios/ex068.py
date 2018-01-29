from random import randint
cont = 0
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    computador = randint(0, 10)
    print('=-' * 30)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).upper()
    resultado = computador + jogador
    print('-' * 30)
    print('Você jogou {} e o computador {}. Total de {} DEU '.format(jogador, computador, resultado), end='')
    if resultado % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')
    print('-' * 30)
    if escolha == 'P' and resultado % 2 != 0:
        break
    elif escolha == 'I' and resultado % 2 == 0:
        break
    cont += 1
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
print('Você PERDEU!')
print('=-' * 30)
if cont > 1:
    print('GAME OVER! Você venceu {} vezes'.format(cont))
elif cont == 1:
    print('GAME OVER! Você venceu uma vez')
else:
    print('GAME OVER! Você ainda não venceu')