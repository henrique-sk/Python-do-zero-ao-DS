import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Qual o valor do imóvel mais caro do tipo “studio”?
# R: 1247000.0

print(dceo['price'].loc[dceo['dormitory_type'] == 'studio'].max())
