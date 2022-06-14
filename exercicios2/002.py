import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantos imóveis possuem o número máximo de andares?
# R: 8

print(data['floors'].unique())
# print(data['floors'] == 3.5) # retorna os booleanos
print(data[data['floors'] == 3.5][['id', 'floors']])
print(data[data['floors'] == 3.5].shape[0]) # shape[0] pra contar só as linhas

#     = pd.to_datetime(data['date'])
# print(data['date'].dtypes)
# print(data.sort_values('date', ascending=True))
