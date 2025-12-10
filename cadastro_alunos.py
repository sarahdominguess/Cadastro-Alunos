# Importando bibliotecas pandas e funcoes
import pandas as pd
import funcoes as fc

# Carregando arquivo csv com função
df = fc.carrega_csv("cadastro_alunos.csv")

# Recolhendo ação que usuario deseja realizar
opcao = fc.menu()

# Se o usuário escolher inserir um aluno
if opcao == 1:
    df = fc.inserir(df)

elif opcao == 2:
    pesquisa = fc.pesquisar(df)
    opcao_pesquisa = fc.pesquisa_menu()

    if opcao_pesquisa == 1:
        df = fc.editar(df, pesquisa)
    elif opcao_pesquisa == 2:
        df = fc.remover(df, pesquisa)
        print(df)

elif opcao == 3:
    print("\nPrograma finalizado!")
