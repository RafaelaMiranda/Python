sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while sexo not in 'MF':
    print('Dados inválidos.',end=' ')
    sexo = str(input('Por favor, informe seu sexo: ')).upper().strip()
if sexo == 'M' or sexo == 'F':
    print('Sexo {} registrado com sucesso!'.format(sexo))