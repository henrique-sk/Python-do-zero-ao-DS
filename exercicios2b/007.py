import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Modifique o TIPO da coluna “yr_renovated” para DATE
# R:

dceo['yr_renovated'] = pd.to_datetime(dceo['yr_renovated'], format='%Y', errors='coerce')
print(dceo.dtypes)
print(dceo[['yr_built', 'yr_renovated']].head())

change = dceo.to_csv('../datasets/kc_house_data_ceo.csv', index=False)
