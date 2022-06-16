import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Qual a casa com maior número de quartos?
# R: A casa com maior número de quartos é a de ID 2402100895 e possui 33 quartos.

print(f'A casa com maior número de quartos é a de ID {data.set_index("id")["bedrooms"].idxmax()} e possui {data["bedrooms"].max()} quartos.')
