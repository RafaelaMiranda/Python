#variaveis
nome = ''
idade = 0
sexo = ''
media = 0
total = 0
velho = 0
nomeVelho = ''
mulheres = 0
homens = 0

for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i)) 
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    total += idade
    if idade > velho and sexo == 'M':
        velho = idade
        nomeVelho = nome
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

print('A média de idade do grupo é de {:.1f} anos'.format(total / i))

if homens >= 1:
    print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomeVelho))
else:
    print('Não possui homens')

if mulheres == 1:
    print('E uma mulher com menor de 20 anos.')
elif mulheres > 1:
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
else:
    print('E sem mulheres com menos de 20 anos.')
