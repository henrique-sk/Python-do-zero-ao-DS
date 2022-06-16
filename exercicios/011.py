import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantas casas possuem mais de 300 metros quadrados na sala de estar?
# R: 2258.

# converter pés quadrados para metros quadrados
data['m2_living'] = data['sqft_living'] * 0.092903
# print(data.sample(3))

print(data.loc[data['m2_living'] > 300].shape[0])
