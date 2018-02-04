maiores = homens = mulheres = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('-' * 30)
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print('Total de pessoas com mais de 18 anos: {}'.format(maiores))

if homens > 1:
    print('Ao todo temos {} homens cadastrados'.format(homens))
elif homens == 1:
    print('Temos um homem cadastrado')
else:
    print('Não temos homens cadastrados')

if mulheres > 1:
    print('E temos {} mulheres com menos de 20 anos'.format(mulheres))
elif mulheres == 1:
    print('Temos uma mulher com menos de 20 anos')
else:
    print('Não temos mulheres com menos de 20 anos')