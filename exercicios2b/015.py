import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Quantos imóveis do tipo “apartment” foram reformados em 2015?
# R: 0

print(dceo[(dceo['dormitory_type'] == 'apartament') & (dceo['yr_renovated'] == '2015-01-01')].shape[0])
