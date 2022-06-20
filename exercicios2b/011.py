import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Quantos imóveis estão com a condição igual a “regular”?
# R: 19710

print(dceo[dceo['condition_type'] == 'regular'].shape[0])
