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
def inserir(df):
  print("\nÓtimo! Vamos inserir um aluno no sistema! Me informe:\n")
  nome = input("NOME: ").lower()
  rua = input("RUA: ")
  numero = input("NÚMERO: ")
  bairro = input("BAIRRO: ")
  cidade = input("CIDADE: ")
  uf = input("UF: ")
  telefone = input("TELEFONE: ")
  email = input("EMAIL: ")
  matricula = len(df) + 1
  
  print(f"\nA matrícula desse aluno é: {matricula}")

  cadastros = {
    'nome': nome,
    'rua': rua,
    'numero': numero,
    'bairro': bairro,
    'cidade': cidade,
    'uf': uf,
    'telefone': telefone,
    'email': email,
    'matricula': matricula
  }

  df_linha_dados = pd.DataFrame([cadastros])
  df = pd.concat([df, df_linha_dados], ignore_index=True)

  return df

def pesquisar(df):
  print("\nÓtimo! Vamos pesquisar um aluno no sistema!")
  aluno = input("NOME do aluno ou NÚMERO DA MATRÍCULA: ")

  if aluno.isdigit() == False:
    aluno = aluno.lower()
    pesquisa = df.loc[df['nome'] == aluno]
    if len(pesquisa) > 1:
      print("\nMais de um aluno com esse nome.")
      while aluno.isdigit() == False:
        aluno = input("Por favor, digite o NÚMERO DE MATRÍCULA do aluno desejado: ")
      aluno = int(aluno)
      pesquisa = df.loc[df['matricula'] == aluno]
  else:
    aluno = int(aluno)
    pesquisa = df.loc[df['matricula'] == aluno]

  if pesquisa.empty == True:
    print("\nNão foi possível encontrar esse aluno!\n")
  else:
    print(f"\nDados do aluno:\n\n{pesquisa}\n")
