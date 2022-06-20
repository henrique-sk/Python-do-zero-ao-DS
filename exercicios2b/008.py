import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Qual a data mais antiga da construção de um imóvel?
# R: 1900

print(dceo['yr_built'].min())
