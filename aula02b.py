import pandas as pd
from numpy import int64

data = pd.read_csv('datasets/kc_house_data.csv')

#=====================================
# Criando novas variáveis
#=====================================

### Criar nova coluna (e atribuir conteúdo em todas linhas)
data['nome_do_henrique'] = 'henrique'
data['comunidade_ds'] = 80
data['data_fiz_aula2'] = pd.to_datetime('2022-02-28')
# print(data['data_fiz_aula2'].dtypes) # datetime64
# print(data.columns)
# print(data[['id', 'comunidade_ds', 'nome_do_henrique', 'data_fiz_aula2']].head())

#=====================================
# Deletando variáveis
#=====================================
print(data.columns)
cols = ['nome_do_henrique', 'comunidade_ds', 'data_fiz_aula2']
data = data.drop(cols, axis=1)
# o axis determina o sentido, se linhas(0) ou colunas(1)
print(data.columns)
# data.drop('nom')

# print(data[['id', 'comunidade_ds', 'nome_do_henrique', 'data_fiz_aula2']].head())
# print(data.dtypes)
