import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Qual o preço médio das casas com 2 banheiros?
# R: 457889.

# print(data[data['bathrooms'] == 2][['id', 'bathrooms']])
# print(data.loc[data['bathrooms'] == 2, ['id', 'bathrooms']])

print(data.loc[data['bathrooms'] == 2, 'price'].mean())

# data.loc[data['bathrooms'] == 2, 'level'] = 'high level'
