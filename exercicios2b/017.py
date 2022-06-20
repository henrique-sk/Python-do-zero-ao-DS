import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Quantos imóveis “new_house” foram reformados no ano de 2014?
# R: 91

print(dceo[(dceo['house_age'] == 'new_house') & (dceo['yr_renovated'] == '2014-01-01')].shape[0])
