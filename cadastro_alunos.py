# Importando bibliotecas pandas e os
import pandas as pd
import funcoes as fc

# Carregando arquivo csv com função
df = fc.carrega_csv("cadastro_alunos.csv")

# Recolhendo ação que usuario deseja realizar
opcao = fc.menu()
