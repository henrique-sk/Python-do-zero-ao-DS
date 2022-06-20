import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Salve um arquivo .csv com somente as colunas do item 10 ao 17.
# R:

print(dceo.iloc[10:18])
change = dceo.iloc[10:18].to_csv('../datasets/kc_house_data_10-17.csv', index=False)
