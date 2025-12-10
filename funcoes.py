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
  opcao = input("\nDigite o número da opção que deseja realizar: ") # Recolhendo ação q o usuário quer realizar
  if opcao.isdigit(): # Se for digito transforma de str para int
    opcao = int(opcao)
    
  while isinstance(opcao, str) or opcao < 1 or opcao > 3: # Se for str ou se não estiver entre 1 e 3
    print("\nVocê deve digitar o NÚMERO da ação desejada, sendo 1, 2 ou 3.\n  1- INSERIR aluno\n  2- PESQUISAR aluno\n  3- SAIR")
    opcao = input("\nDigite o número da opção que deseja realizar: ")
    if opcao.isdigit(): # Se for digito transforma de str para int
      opcao = int(opcao)

  return opcao # Retorna a opçao escolhida

# Função para inserir aluno
def inserir(df):
  print("\nÓtimo! Vamos inserir um aluno no sistema! Me informe:\n")
  # Recolhendo dados
  nome = input("NOME: ").lower() # Utilizando lower para tornar pesquisas case-insensitive
  rua = input("RUA: ")
  numero = input("NÚMERO: ")
  bairro = input("BAIRRO: ")
  cidade = input("CIDADE: ")
  uf = input("UF: ")
  telefone = input("TELEFONE: ")
  email = input("EMAIL: ")
  
  if df['matricula'].empty == True: # Se não houver nenhuma matrícula anterior, a primeira será 1
    matricula = 1
  else:
    matricula = df['matricula'].max() + 1 # Se já houverem matrículas, ela será igual a maior mais 1
  
  print(f"\nA matrícula desse aluno é: {matricula}\n") # Informa a matrícula para usuário

  # Dicionário para armazenar dados
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

  # Transformando dicionário em DataFrame e adicionando ao DataFrame já existente
  df_linha_dados = pd.DataFrame([cadastros])
  df = pd.concat([df, df_linha_dados], ignore_index=True)

  return df # Retorna o DataFrame

# Função para pesquisar aluno
def pesquisar(df):
  print("\nÓtimo! Vamos pesquisar um aluno no sistema!")
  aluno = input("NOME do aluno ou NÚMERO DA MATRÍCULA: ") # Recolhe nome ou matrícula do aluno

  if aluno.isdigit() == False: # Se não for dígito (caso seja o nome do aluno)
    aluno = aluno.lower() # Usando lower para tornar a pesquisa case-insensitive
    pesquisa = df.loc[df['nome'] == aluno] # Busca aluno pelo nome
    if len(pesquisa) > 1: # Se houver mais de um aluno com esse nome
      print("\nMais de um aluno com esse nome.")
      while aluno.isdigit() == False: # Enquanto não for dígito (caso seja o nome do aluno)
        aluno = input("Por favor, digite o NÚMERO DE MATRÍCULA do aluno desejado: ")
      aluno = int(aluno) # Transformando de str para int
      pesquisa = df.loc[df['matricula'] == aluno] # Busca aluno pela matrícula
  else:
    aluno = int(aluno) # Transformando de str para int
    pesquisa = df.loc[df['matricula'] == aluno] # Busca aluno pela matrícula

  if pesquisa.empty == True: # Caso o aluno não seja encontrado
    print("\nNão foi possível encontrar esse aluno!\n")
  else: # Se o aluno for encontrado
    print(f"\nDados do aluno:\n\n{pesquisa}\n")

  return pesquisa # Retorna pesquisa

# Função para mostrar opções após a pesquisa (remover ou editar)
def pesquisa_menu():
  print("Deseja realizar uma das ações a seguir?\n  1- EDITAR informações\n  2- REMOVER aluno\n  3- Não quero realizar nenhuma das ações acima\n")
  
  opcao = input("Digite o NÚMERO da opção que deseja: ") # Recolhendo ação q o usuário quer realizar
  if opcao.isdigit(): # Se for digito transforma de str para int
    opcao = int(opcao)
  
  while isinstance(opcao, str) or opcao < 1 or opcao > 3: # Se for str ou se não estiver entre 1 e 3
    print("\nVocê deve digitar o NÚMERO da opção desejada, sendo 1, 2 ou 3.\n  1- EDITAR informações\n  2- REMOVER aluno\n  3- Não quero realizar nenhuma das ações acima\n")
    opcao = input("Digite o NÚMERO da opção que deseja: ") # Recolhendo ação q o usuário quer realizar
    if opcao.isdigit(): # Se for digito transforma de str para int
      opcao = int(opcao)

  match opcao:
      case 1: # Caso escolha opção 1
        print("\nÓtimo! Vamos editar as informações desse aluno no sistema!\n")
      case 2: # Caso escolha opção 2
        print("\nÓtimo! Vamos remover esse aluno do sistema!\n")
      case 3: # Caso escolha opção 3
        print("\nÓtimo! Fim da pesquisa!\n")
  
  return opcao # Retorna o número da opção escolhida

# Função para editar insformações do aluno
def editar(df, pesquisa):
  print("Qual das informações desse aluno deseja editar?")
  print("  1- Nome\n  2- Rua\n  3- Número\n  4- Bairro\n  5- Cidade\n  6- UF\n  7- Telefone\n  8- Email")

  opcao = input("\nDigite o NÚMERO da informação que deseja: ") # Recolhendo opçao que usuário deseja
  if opcao.isdigit(): # Se for digito transforma de str para int
    opcao = int(opcao)
    
  while isinstance(opcao, str) or opcao < 1 or opcao > 8: # Se for str ou se não estiver entre 1 e 8
    print("\nVocê deve digitar o NÚMERO da informação desejada, sendo entre 1 e 8.\n  1- Nome\n  2- Rua\n  3- Número\n  4- Bairro\n  5- Cidade\n  6- UF\n  7- Telefone\n  8- Email")
    opcao = input("\nDigite o número da opção que deseja realizar: ") # Recolhendo opçao que usuário deseja
    if opcao.isdigit(): # Se for digito transforma de str para int
      opcao = int(opcao)
  
  # Indice da linha que deseja alterar no DataFrame
  indice = pesquisa.index

  match opcao:
    case 1: # Caso escolha opção 1
      edicao = input("\nDigite novo NOME: ")
      df.loc[indice, 'nome'] = edicao
    case 2: # Caso escolha opção 2
      edicao = input("\nDigite nova RUA: ")
      df.loc[indice, 'rua'] = edicao
    case 3: # Caso escolha opção 3
      edicao = input("\nDigite novo NÚMERO: ")
      df.loc[indice, 'numero'] = edicao
    case 4: # Caso escolha opção 4
      edicao = input("\nDigite novo BIARRO: ")
      df.loc[indice, 'bairro'] = edicao
    case 5: # Caso escolha opção 5
      edicao = input("\nDigite nova CIDADE: ")
      df.loc[indice, 'cidade'] = edicao
    case 6: # Caso escolha opção 6
      edicao = input("\nDigite novo UF: ")
      df.loc[indice, 'uf'] = edicao
    case 7: # Caso escolha opção 7
      edicao = input("\nDigite novo TELEFONE: ")
      pesquisa.loc['telefone'] = edicao
      df.loc[indice, 'telefone'] = edicao
    case 8: # Caso escolha opção 8
      edicao = input("\nDigite novo EMAIL: ")
      df.loc[indice, 'email'] = edicao
    
  print(f"\nEdição realiza com sucesso! Novos dados:\n\n{df.loc[indice]}\n")

  return df # Retorna Dataframe

# Função para remover aluno
def remover(df, pesquisa):
  print("Tem certeza que deseja REMOVER esse aluno?")
  print("Para confirmar, digite 'SIM', com todas as letras maiúsculas. Respostas como 'Sim', 'sim' ou qualquer outras diferentes de 'SIM' serão desconsideradas.\n") # Informando resposta esperada do usuário. Estou cobrando a confirmação dessa forma por questão de segurança, uma vez que não será possível recuperar os dados do aluno removido
  confirmacao = input("Digite 'SIM' para confirmar: ") # Recolhendo confirmação do usuário

  if confirmacao == "SIM": # Se a confirmação for positiva
    indice = pesquisa.index # Indice da linha que deseja alterar no DataFrame
    df = df.drop(indice) # Removendo aluno
    print("\nAluno removido!\n")
  else:
    print("\nObrigada pela confirmação! Aluno NÃO removido!\n")

  return df # Retorna DataFrame

# Função para salvar Dataframe em arquivo CSV
def salvar(df, nome_arquivo):
  df.to_csv(nome_arquivo, index=False)
