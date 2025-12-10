# Importando bibliotecas pandas e funcoes
import pandas as pd
import funcoes as fc

# Iniciando variável
opcao = 0

while opcao != 3: # Enquanto opcao for diferente de 3 (diferente de SAIR)
    opcao = fc.menu()

    # Carregando arquivo csv com função
    df = fc.carrega_csv("cadastro_alunos.csv")

    if opcao == 1: # Se o usuário escolher inserir um aluno
        df = fc.inserir(df) # Inserindo aluno com função
        fc.salvar(df, "cadastro_alunos.csv") # Salvando o dataframe em csv com função
        opcao = 0 # 'Resetando' opcao

    elif opcao == 2: # Se o usuário escolher pesquisar um aluno
        pesquisa = fc.pesquisar(df) # Pesquisando aluno com função
        
        if pesquisa.empty == False: # Se o aluno for encontrado no sistema
            opcao_pesquisa = fc.pesquisa_menu() # Pesquisando aluno com Função

            if opcao_pesquisa == 1: # Se o usuário escolher editar alguma informação
                df = fc.editar(df, pesquisa) # Editando informação com função
                fc.salvar(df, "cadastro_alunos.csv") # Salvando o dataframe em csv com função
            elif opcao_pesquisa == 2: # Se o usuário escolher remover algum aluno
                df = fc.remover(df, pesquisa) # Removendo aluno com função
                fc.salvar(df, "cadastro_alunos.csv") # Salvando o dataframe em csv com função
        
        opcao = 0 # 'Resetando' opcao

print("\nPrograma finalizado!") # Mensagem de finalização
