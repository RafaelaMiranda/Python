from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        print('Entre {} e {} o maior valor é '.format(n1, n2), end='')
        if n1 > n2:
            print('{}'.format(n1))
        elif n2 > n1:
            print('{}'.format(n2))
        else:
            print('OS DOIS :)')
    elif opcao == 4:
        print('Informe os números novamente...')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 20)
    sleep(1)
print('Fim do programa! Volte sempre')
 