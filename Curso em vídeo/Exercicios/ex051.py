print('=' * 25)
print('   10 TERMOS DE UMA PA   ')
print('=' * 25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo = termo + (10 - 1) * razao

for i in range(termo, decimo + razao, razao):
    print('{} '.format(i), end='→ ')
print('ACABOU')
