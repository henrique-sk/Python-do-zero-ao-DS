import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Qual a data do imóvel mais antigo no portfólio?
# R: 02/05/2014

data['date'] = pd.to_datetime(data['date'])
print(data['date'].dtypes)
print(data.sort_values('date', ascending=True).head(1))
