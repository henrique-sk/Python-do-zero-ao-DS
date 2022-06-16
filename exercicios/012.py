import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantas casas tem mais de 2 andares?
# R: 782.

print(data[data['floors'] > 2].shape[0])
