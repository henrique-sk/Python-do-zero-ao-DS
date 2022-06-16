import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantas casas possuem 2 banheiros?
# R: 1930

print(data['bathrooms'].unique())
# print(data['floors'] == 3.5) # retorna os booleanos
# print(data[data['bathrooms'] == 2][['id', 'bathrooms']])
print(data[data['bathrooms'] == 2].shape[0]) # shape[0] pra contar só as linhas
