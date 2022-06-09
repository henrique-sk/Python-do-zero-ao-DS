import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantas casas estão disponíveis para compra dentro da plataforma?
# R: 21613

print(data[data.columns[0]].count())
# OU
print(len(data.index))
# OU
print(len(data)) # desempenho menor que o anterior
# OU
l, c = data.shape # linha e coluna
print(l)
# OU
print(data.shape[0]) # 0 para linhas e 1 para colunas
