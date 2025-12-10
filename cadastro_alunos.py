# Importando bibliotecas pandas e funcoes
import pandas as pd
import funcoes as fc

# Recolhendo ação que usuario deseja realizar
opcao = 0

while opcao != 3:
    opcao = fc.menu()

    # Carregando arquivo csv com função
    df = fc.carrega_csv("cadastro_alunos.csv")

    # Se o usuário escolher inserir um aluno
    if opcao == 1:
        df = fc.inserir(df)
        fc.salvar(df, "cadastro_alunos.csv")
        opcao = 0

    elif opcao == 2:
        pesquisa = fc.pesquisar(df)
        
        if pesquisa.empty == False:
            opcao_pesquisa = fc.pesquisa_menu()

            if opcao_pesquisa == 1:
                df = fc.editar(df, pesquisa)
                fc.salvar(df, "cadastro_alunos.csv")
            elif opcao_pesquisa == 2:
                df = fc.remover(df, pesquisa)
                fc.salvar(df, "cadastro_alunos.csv")
        
        opcao = 0

print("\nPrograma finalizado!")
