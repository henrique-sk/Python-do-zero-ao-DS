import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantos atributos as casas possuem?
# R: 21

l, c = data.shape
print(c)
# OU
print(data.shape[1]) # 0 para linhas e 1 para colunas
# OU
print(len(data.columns))
