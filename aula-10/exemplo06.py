# Calcula média das notas - Não sabemos quantos alunos, mas terão 4 notas sempre
def calcula_media(lista_notas):
    totall = sum(lista_notas)
    mediaa = totall / len(lista_notas)
    return totall, mediaa


contator = 1

while True:
    print(f'Aluno {contator}')
    aluno = input('Digite o nome do aluno: ')
    
    notas = []
    try:
        for i in range(4):
            nota = float(input('Digite a nota: '))
            notas.append(nota)

    except ValueError:
        print('Erro! Informe apenas valores válidos!!')
    else:
        total, media = calcula_media(notas)
        print('\nRESULTADO')
        print(f'Aluno: {aluno}')
        print(f'Total de pontos: {total}')
        print(f'Média: {media:.2f}')
    
    finally:
        print('Processo encerrado para o aluno!!!')
    
    opcao = input('\nDeseja calcular a média de outro aluno? [S/N] ').strip().upper() #o strip tira o espaço que vem antes e depois
    if opcao != 'S':
        break
    contator += 1
print('\nPrograma encerrado!!!')
