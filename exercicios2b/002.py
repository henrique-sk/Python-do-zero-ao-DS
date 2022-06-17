import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Crie uma coluna chamada: ”dormitory_type”
# Se o valor da coluna “bedrooms” for igual à 1 => “studio”
# Se o valor da coluna “bedrooms” for igual à 2 => “apartament”
# Se o valor da coluna “bedrooms” for maior que 2 => “house”
# R:

dceo['dormitory_type'] = ''

dceo.loc[dceo['bedrooms'] == 1, 'dormitory_type'] = 'studio'
dceo.loc[dceo['bedrooms'] == 2, 'dormitory_type'] = 'apartament'
dceo.loc[dceo['bedrooms'] > 2, 'dormitory_type'] = 'house'

change = dceo.to_csv('../datasets/kc_house_data_ceo.csv', index=False)

print(dceo[['id', 'bedrooms', 'dormitory_type']].sample(5))
