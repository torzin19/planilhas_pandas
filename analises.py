import pandas as pd


#lendo a planilha excel 

# Altere a linha 6 para o caminho completo do arquivo:
df = pd.read_csv('dados_alunos_escola.csv')


# exibindo os dados na tela

#print(df) #leitura de planilha inteira

# 1. visualizar as primeiras linhas
print(df.head()) # exibe as primeiras 5 linhas do Dataframe

# 2. verificar o resumo estatístico (médias, mínimos, maxímos)
#print(df.describe())

# 3. ver os tipos de dados e se há valores nulos
print(df.info())
