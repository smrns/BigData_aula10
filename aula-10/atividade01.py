def caixa_eletronico():
    saldo = 1000
    print('----- Bem vindo ao banco Python!! -----')
    print(f'Saldo disponível: R$ {saldo:.2f}')

    try:
        saque = float(input('\nDigite o valor que deseja sacar: R$ '))

        if saque <= 0:
            print('Operação cancelada. O valor do saque deve ser maior que zero.')
        elif saque > saldo:
            print(f'Operação negada. Saldo insuficiente. Seu saldo é de R$ {saldo:.2f}')
        else:
            saldo -= saque #To dizendo que saldo recebe o saldo menos o saque
            print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
            print(f'Saldo atualizado: R$ {saldo:.2f}')
    except ValueError:
        print('Entrada inválida. Por favor, digite apenas números (ex: 150.50).')
    finally:
        print('\nObrigada por ultilizar nossos serviços.')

caixa_eletronico()

# ----------------------------------------------------------------------------------------------
# Feito pelo professor

print('\n----- CAIXA ELETRÔNICO -----')

try:
    saldoo = 1000
    saquee = float(input('Informe o valro do saque: R$ '))

except ValueError:
    print('Valor inválido!!')
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário!!!')
else:
    if saquee > saldoo:
        print('Saldo insuficiente!!!')
    elif saquee <= 0:
        print('Saque precias ser maior ou igual a R$ 2,00 reais')
    else:
        saldoo -= saquee 
        print('\nSaque realizado com sucesso')
        print(f'Saldo em conta R$ {saldoo:.2f}')

finally:
    print('Operação realizada!!')

print('Programa encerrado!!')
