print('----- Cálculo de Produtividade -----')

try:
    total_produzido = float(input('Valor total da venda: R$ '))
    funcionarios = int(input('Quantos funcionários tem? '))

    media_por_funcionario = total_produzido / funcionarios

except Exception as e: #Aqui ele vai mostrar o tipo de erro
    print(f'Ops! Erro nos valores de entrada: {e}')
except KeyboardInterrupt:
    print('Operação encerrada pelo usuário.')
else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
finally: 
    print('Programa encerrado!!!')

