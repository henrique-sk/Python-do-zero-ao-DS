import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Selecione as colunas: “id”, “date”, “price”, “floors”, “zipcode” pelo método:
# Direto pelo nome das colunas.
# Pelos índices.
# Pelos índices das linhas e o nome das colunas
# Índices booleanos
# R:

print(dceo[['id', 'date', 'price', 'floors', 'zipcode']])
print(dceo.iloc[:, [0, 1, 2, 7, 16]])
print(dceo.loc[:, ['id', 'date', 'price', 'floors', 'zipcode']])
print(dceo.loc[:, [True, True, True, False, False, False, False, True, False, False, False, False,
                  False,False, False, False, True, False, False, False, False, False, False]])
