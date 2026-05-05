# For com try e except, aqui ele continua executando o looping mesmo se tiver algum erro
print('----- Cálculo de Produtividade -----')

for i in range(5):
    try:
        total_produzido = float(input('Valor total da venda: R$ '))
        funcionarios = int(input('Quantos funcionários tem? '))

        media_por_funcionario = total_produzido / funcionarios
        print(f'Média por funcionário: {media_por_funcionario:.2f}')
    except ValueError:
        print('Digite apenas número(s).')
    except ZeroDivisionError:
        print('Número de Funcionários não pode ser 0.')