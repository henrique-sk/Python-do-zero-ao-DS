import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Quantas casas tem vista para o mar?
# R: 163.

# data['waterfront'].value_counts()
# # Retorna:
# 0    21450
# 1      163
# Name: waterfront, dtype: int64

print(data['waterfront'].value_counts()[1])
