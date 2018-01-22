from datetime import date
ano = int(input('Ano de nascimento: '))
sexo = str(input('Digite seu sexo (F para mulheres e M para homens): '))
anoAtual = date.today().year 
idade =  anoAtual - ano

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))

if idade < 18 and sexo == 'M':
    falta = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(falta))
    print('Seu alistamento será em {}'.format(anoAtual + falta))
elif idade > 18 and sexo == 'M':
    passou = idade - 18
    print('Você já deveria ter alistado há {} anos'.format(passou))
    print('Seu alistamento foi em {}'.format(anoAtual - passou))
elif idade == 18 and sexo == 'M':
    print('Você tem que se alistar IMEDIATAMENTE')
else:
    print('Alistamento militar NÃO OBRIGATÓRIO!')