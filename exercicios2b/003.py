import pandas as pd

dceo = pd.read_csv('../datasets/kc_house_data_ceo.csv')

# Crie uma coluna chamada: ”condition_type”
# Se o valor da coluna “condition” for menos ou igual à 2 => “bad”
# Se o valor da coluna “condition” for igual à 3 ou 4 => “regular”
# Se o valor da coluna “condition” for igual à 5 => “good”
# R:

dceo['condition_type'] = ''

dceo.loc[dceo['condition'] <= 2, 'condition_type'] = 'bad'
dceo.loc[(dceo['condition'] == 3) | (dceo['condition'] == 4), 'condition_type'] = 'regular'
dceo.loc[dceo['condition'] == 5, 'condition_type'] = 'good'

change = dceo.to_csv('../datasets/kc_house_data_ceo.csv', index=False)

print(dceo[['condition', 'condition_type']].sample(5))
