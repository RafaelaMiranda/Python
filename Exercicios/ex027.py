nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
listagem = nome.split()
tamanho = len(listagem)
print('Seu primeiro nome é {}'.format(listagem[0]))
print('Seu último nome é {}'.format(listagem[tamanho - 1]))