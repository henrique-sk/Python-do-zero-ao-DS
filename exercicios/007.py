import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantas casas possuem 2 banheiros?
# R:

print(f'A soma é {data[data["bedrooms"].sum(data["price"])} quartos.')