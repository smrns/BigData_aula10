print('----- Cálculo de Produtividade -----')

try:
    total_produzido = float(input('Valor total da venda: R$ '))
    funcionarios = int(input('Quantos funcionários tem? '))

    media_por_funcionario = total_produzido / funcionarios

except ValueError:
    print('Digite apenas número(s).')
except ZeroDivisionError:
    print('Número de Funcionários não pode ser 0.')

# Se não der erro, executa o else
else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
