import pandas as pd
from numpy import int64

data = pd.read_csv('datasets/kc_house_data.csv')

# tipos de variáveis de cada coluna
print(data.dtypes)
# o date é mostrado como objeto

print(data.head())

#=====================================
# Como converter os tipos de variáveis
#=====================================
### String -> date (e já armazena na mesma coluna de date)
data['date'] = pd.to_datetime(data['date'])
# convertido para o tipo datetime64

### Integer -> Float
data['bedrooms'] = data['bedrooms'].astype(float)
print(data[['id', 'bedrooms']].head(3))
# print(data.dtypes)  # mostrar tipos de variáveis em cada coluna

### Float -> Integer (deixar todos com mesmo padrão, 32 ou 64)
data['bedrooms'] = data['bedrooms'].astype(int64)
# print(data.dtypes)

### Integer -> String
data['bedrooms'] = data['bedrooms'].astype(str)
# print(data.dtypes)
# assim, volta a ser objeto

### String -> Integer
data['bedrooms'] = data['bedrooms'].astype(int64)
print(data.dtypes)
