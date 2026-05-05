# Cálculo de produtividade com tratamento de erro (try e except)

print('----- Cálculo de Produtividade -----')

try:
    total_produzido = float(input('Valor total da venda: R$ '))
    funcionarios = int(input('Quantos funcionários tem? '))

    media_por_funcionario = total_produzido / funcionarios
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
except ValueError:
    print('Digite apenas número(s).')
except ZeroDivisionError:
    print('Número de Funcionários não pode ser 0.')

# se eu quiser que seja na mesma linha, sera assim: except (ValueError, TypeError)