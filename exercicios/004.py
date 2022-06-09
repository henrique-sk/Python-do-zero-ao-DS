import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Qual a casa mais cara do portfólio?
# R: A casa mais cara custa 7700000.00 é a de ID 6762700020.

print(f'A casa mais cara custa {data["price"].max():.2f} é a de ID {data.set_index("id")["price"].idxmax()}.')
