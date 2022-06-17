import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

data['level'] = 'standard'
data.loc[data['price'] > 540000, 'level'] = 'high level'
data.loc[data['price'] <= 540000, 'level'] = 'low level'
dceo = data.to_csv('../datasets/kc_house_data_ceo.csv', index=False)

# Gostaria de um relatório ordenado pelo preço e  contendo as seguintes informações:
# (id do imóvel,
# data que o imóvel ficou disponível para compra
# o número de quartos,
# o tamanho total do terreno
# o preço,
# a classificação do imóvel (alto e baixo padrão)
# R:

report = data[['id', 'date', 'bedrooms', 'sqft_lot', 'price', 'level']]\
    .sort_values('price', ascending=False)

report.to_csv('../datasets/report_aula02.csv', index=False)
# index=False para não replicar os índices do arquivo orignal,
# mas sim criar seus próprios do zero

print(report.head())
