import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Delete as colunas: “sqft_living” e “sqft_lot15”
# R:

print(dceo[['sqft_living15', 'sqft_lot15']].sample(5))
dceo = dceo.drop(columns=['sqft_living15', 'sqft_lot15'])

change = dceo.to_csv('../datasets/kc_house_data_ceo.csv', index=False)
