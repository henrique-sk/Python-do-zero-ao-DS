import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Quantos imóveis tem 2 andares?
# R: 8241

print(dceo[dceo['floors'] == 2].shape[0])
