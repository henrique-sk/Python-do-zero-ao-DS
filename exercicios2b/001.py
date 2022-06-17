import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Crie uma coluna chamada: ”house_age”
# Se o valor da coluna “date” for maior que 2014-0101 => ‘new_house’
# Se o valor da coluna “date” for menor que 2014-0101 => ‘old_house’
# R:

dceo['house_age'] = ''
dceo['date'] = pd.to_datetime(dceo['date'])

dceo.loc[dceo['date'] >= pd.to_datetime(20140101), 'house_age'] = 'new_house'
dceo.loc[dceo['date'] < pd.to_datetime(20140101), 'house_age'] = 'old_house'

change = dceo.to_csv('../datasets/kc_house_data_ceo.csv', index=False)

print(dceo.sample(5))
