import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Qual a data mais antiga da renovação de um imóvel?
# R: ???

print(dceo['yr_renovated'].min())
