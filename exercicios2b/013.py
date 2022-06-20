import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Quantos imóveis estão com a condição igual a “good” e são “new_house”?
# R: 1701

print(dceo[(dceo['condition_type'] == 'good') & (dceo['house_age'] == 'new_house')].shape[0])
