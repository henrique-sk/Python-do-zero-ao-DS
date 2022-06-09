import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Qual a soma total de quartos do conjunto de dados?
# R: A soma é 72854 quartos.

print(f'A soma é {data["bedrooms"].sum()} quartos.')
