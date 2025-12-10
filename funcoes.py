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

  return pesquisa

def pesquisa_menu():
  print("Deseja realizar uma das ações a seguir?\n  1- EDITAR informações\n  2- REMOVER aluno\n  3- Não quero realizar nenhuma das ações acima\n")
  
  opcao = input("Digite o NÚMERO da opção que deseja: ")
  if opcao.isdigit():
    opcao = int(opcao)
  
  while isinstance(opcao, str) or opcao < 1 or opcao > 3:
    print("\nVocê deve digitar o NÚMERO da opção desejada, sendo 1, 2 ou 3.\n  1- EDITAR informações\n  2- REMOVER aluno\n  3- Não quero realizar nenhuma das ações acima\n")
    opcao = input("Digite o NÚMERO da opção que deseja: ")
    if opcao.isdigit():
      opcao = int(opcao)

  match opcao:
      case 1:
        print("\nÓtimo! Vamos editar as informações desse aluno no sistema!\n")
      case 2:
        print("\nÓtimo! Vamos remover esse aluno do sistema!\n")
      case 3:
        print("\nÓtimo! Fim da pesquisa!\n")
  
  return opcao

def editar(df, pesquisa):
  print("Qual das informações desse aluno deseja editar?")
  print("  1- Nome\n  2- Rua\n  3- Número\n  4- Bairro\n  5- Cidade\n  6- UF\n  7- Telefone\n  8- Email")

  opcao = input("\nDigite o NÚMERO da informação que deseja: ")
  if opcao.isdigit():
    opcao = int(opcao)
    
  while isinstance(opcao, str) or opcao < 1 or opcao > 8:
    print("\nVocê deve digitar o NÚMERO da informação desejada, sendo entre 1 e 8.\n  1- Nome\n  2- Rua\n  3- Número\n  4- Bairro\n  5- Cidade\n  6- UF\n  7- Telefone\n  8- Email")
    opcao = input("\nDigite o número da opção que deseja realizar: ")
    if opcao.isdigit():
      opcao = int(opcao)
  
  indice = pesquisa.index

  match opcao:
    case 1:
      edicao = input("\nDigite novo NOME: ")
      df.loc[indice, 'nome'] = edicao
    case 2:
      edicao = input("\nDigite nova RUA: ")
      df.loc[indice, 'rua'] = edicao
    case 3:
      edicao = input("\nDigite novo NÚMERO: ")
      df.loc[indice, 'numero'] = edicao
    case 4:
      edicao = input("\nDigite novo BIARRO: ")
      df.loc[indice, 'bairro'] = edicao
    case 5:
      edicao = input("\nDigite nova CIDADE: ")
      df.loc[indice, 'cidade'] = edicao
    case 6:
      edicao = input("\nDigite novo UF: ")
      df.loc[indice, 'uf'] = edicao
    case 7:
      edicao = input("\nDigite novo TELEFONE: ")
      pesquisa.loc['telefone'] = edicao
      df.loc[indice, 'telefone'] = edicao
    case 8:
      edicao = input("\nDigite novo EMAIL: ")
      df.loc[indice, 'email'] = edicao
    
  print(f"\nEdição realiza com sucesso! Novos dados:\n\n{df.loc[indice]}\n")

  return df

def remover(df, pesquisa):
  print("Tem certeza que deseja REMOVER esse aluno?")
  print("Para confirmar, digite 'SIM', com todas as letras maiúsculas. Respostas como 'Sim', 'sim' ou qualquer outras diferentes de 'SIM' serão desconsideradas.\n")
  confirmacao = input("Digite 'SIM' para confirmar: ")

  if confirmacao == "SIM":
    indice = pesquisa.index
    df = df.drop(indice)
    print("\nAluno removido!\n")
  else:
    print("\nObrigada pela confirmação! Aluno NÃO removido!\n")

  return df
