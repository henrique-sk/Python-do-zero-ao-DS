import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Qual o preço mínimo entre as casas com 3 quartos?
# R: 82000,00.

print(data.loc[data['bedrooms'] == 3]['price'].min())
