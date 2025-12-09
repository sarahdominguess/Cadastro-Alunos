# Importando bibliotecas pandas e os
import pandas as pd
import os

# Função para carregar o arquivo csv
def carrega_csv(caminho_arquivo):
  if os.path.exists(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    return df
  else:
    print(f'\nErro: O arquivo a seguir nao existe:\n{caminho_arquivo}\n')
    return None

# Função para mostrar o menu e escolher a ação
def menu():
    print("Qual das opções abaixo deseja realizar?\n  1- INSERIR aluno\n  2- PESQUISAR aluno\n  3- SAIR")
    opcao = input("\nDigite o número da opção que deseja realizar: ")
    if opcao.isdigit():
        opcao = int(opcao)
    
    while isinstance(opcao, str) or opcao < 1 or opcao > 3:
        print("\nVocê deve digitar o NÚMERO da ação desejada, sendo 1, 2 ou 3.\n  1- INSERIR aluno\n  2- PESQUISAR aluno\n  3- SAIR")
        opcao = input("\nDigite o número da opção que deseja realizar: ")
        if opcao.isdigit():
            opcao = int(opcao)

    return opcao
