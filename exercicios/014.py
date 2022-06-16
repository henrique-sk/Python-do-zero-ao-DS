import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Das casas com vista para o mar, quantas tem 3 quartos?
# R: 64.

print(data.loc[(data['bedrooms'] == 3) & (data['waterfront'])].shape[0])
