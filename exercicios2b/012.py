import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Quantos imóveis estão com a condição igual a “bad” e possuem “vista para água”?
# R: 2

print(dceo[(dceo['condition_type'] == 'bad') & (dceo['waterfront'])].shape[0])
