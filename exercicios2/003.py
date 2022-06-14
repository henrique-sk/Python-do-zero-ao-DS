import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# Criar uma classificação para imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
# Acima de R$ 540.000 -> alto padrão
# Abaixo de R$ 540.000 -> baixo padrão
# R:

data['level'] = 'standard'

# Todas as linhas em que 'price' for maior do que 540000
# Em 'level', atribua 'high level'
data.loc[data['price'] > 540000, 'level'] = 'high level'
data.loc[data['price'] <= 540000, 'level'] = 'low level'

print(data.head())
