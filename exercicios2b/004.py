import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Modifique o TIPO da coluna “condition” para STRING
# R:int64
# object

print(dceo['condition'].dtypes)
dceo['condition'] = dceo['condition'].astype(str)
print(dceo['condition'].dtypes)

change = dceo.to_csv('../datasets/kc_house_data_ceo.csv', index=False)
