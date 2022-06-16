import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Qual o preço médio de todas as casas no conjunto de dados?
# R: O preço médio é R$ 540088.14.

print(f'O preço médio é R$ {data["price"].mean() :.2f}.')
