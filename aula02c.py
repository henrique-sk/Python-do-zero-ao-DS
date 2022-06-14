import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

#=====================================
# Seleções de dados
#=====================================
### Forma 1: Direto pelo nome das colunas
print(data['price'].sample(3))

# Para várias colunas, deve-se chamar em forma de lista
cols = ['id', 'price', 'date']
print(data[cols].sample(3))

### Forma 2: Pelos Índices das linhas e colunas
### iloc -> index localize
# Ex.: ds[l, c]
print(data.iloc[0:4, 0:3]) # linhas 0 a 10 e colunas 0 a 3
# print(data.iloc[:, 0:3]) # todas linhas e colunas 0 a 3

### Forma 3: Pelos Índices das linhas e nome das colunas
### loc -> localize
print(data.loc[0:4, ['id', 'price', 'date']])

### Forma 4: Índices Booleanos
# ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#        'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#        'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#        'lat', 'long', 'sqft_living15', 'sqft_lot15']
cols2 = [True, False, True, True, False, False, False, False, False, False, False,
 False, False, False, False, False, False, False, False, False, False]
print(data.loc[0:4, cols2])
