import pandas as pd

# carregar os dados do CSV
data = pd.read_csv('datasets/kc_house_data.csv')

# 5 primeiras linhas da DB
# print(data.head())

# número de linhas e colunas
# print(data.shape)

#nome das colunas
# print(data.columns)

# dados ordenados pela coluna indicada
# print(data[['id', 'price']].sort_values('price'))

# dados ordenados pela coluna indicada classificada do maior para o menor
# print(data[['id', 'price']].sort_values('price', ascending=False))

# Qual a soma total de quartos do conjunto de dados?
# R: A soma é 72854 quartos.

somaPrices = data["price"].sum() / data.shape[0]
print(somaPrices)

data["bedrooms"].sum()

print(data.shape[0])

# print(f'A soma é {data["bedrooms"].sum()} quartos.')
