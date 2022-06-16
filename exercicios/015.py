import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
# R: 2201.

data['m2_living'] = data['sqft_living'] * 0.092903
print(data.loc[(data['m2_living'] > 300) & (data['bathrooms'] > 2)].shape[0])
