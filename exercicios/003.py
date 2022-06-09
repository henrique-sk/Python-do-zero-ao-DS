import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quaia são os atributos?
# R: Index(['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
      #  'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
      #  'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
      #  'lat', 'long', 'sqft_living15', 'sqft_lot15'],
      # dtype='object')

print(data.columns)
