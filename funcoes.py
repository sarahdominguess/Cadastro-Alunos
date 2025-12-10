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

# Função para inserir aluno
def inserir(nome = [], rua = [], numero = [], bairro = [], cidade = [], uf = [], telefone = [], email = [], matricula = []):
  print("\nÓtimo! Vamos inserir um aluno no sistema! Me informe:\n")
  nome.append(input("NOME: ").lower())
  rua.append(input("RUA: "))
  numero.append(input("NÚMERO: "))
  bairro.append(input("BAIRRO: "))
  cidade.append(input("CIDADE: "))
  uf.append(input("UF: "))
  telefone.append(input("TELEFONE: "))
  email.append(input("EMAIL: "))
  matricula.append(matricula[-1] + 1)
  print(f"\nA matrícula desse aluno é: {matricula[-1]}")

  if matricula[0] == 0:
    matricula.remove(0)
  
def salvar_csv(df, dicionario, nome_arquivo):
  df_linha_dados = pd.DataFrame([dicionario])
  df = pd.concat([df, df_linha_dados], ignore_index=True)
  df.to_csv(nome_arquivo, index=False)

def pesquisar(df):
  print("\nÓtimo! Vamos pesquisar um aluno no sistema!")
  aluno = input("NOME do aluno ou NÚMERO DA MATRÍCULA: ")
  if aluno.isdigit():
    aluno = int(aluno)
    pesquisa = df.loc[df['matricula'] == aluno]
  else:
    aluno = aluno.lower()
    pesquisa = df.loc[df['nome'] == aluno]

  if pesquisa.empty == True:
    print("\nNão foi possível encontrar esse aluno!\n")
  else:
    print(f"\nDados do aluno:\n\n{pesquisa}\n")
