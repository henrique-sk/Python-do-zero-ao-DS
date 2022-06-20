import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Qual o maior número de quartos que um imóvel do tipo “house” possui?
# R: 33

print(dceo['bedrooms'].loc[dceo['dormitory_type'] == 'house'].max())
