# Importando bibliotecas pandas e funcoes
import pandas as pd
import funcoes as fc

# Carregando arquivo csv com função
df = fc.carrega_csv("cadastro_alunos.csv")

nomes = []
rua = []
numero = []
bairro = []
cidade = []
uf = []
telefone = []
email = []
matricula = []

cadastros = {
    'nome': nomes,
    'rua': rua,
    'numero': numero,
    'bairro': bairro,
    'cidade': cidade,
    'uf': uf,
    'telefone': telefone,
    'email': email,
    'matricula': matricula
}

# Recolhendo ação que usuario deseja realizar
opcao = fc.menu()

# Se o usuário escolher inserir um aluno
if opcao == 1:
    fc.inserir(nomes, rua, numero, bairro, cidade, uf, telefone, email)
