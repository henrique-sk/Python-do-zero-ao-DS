import pandas as pd
import plotly.express as px

data = pd.read_csv('../datasets/kc_house_data.csv')

# Modifique a cor dos pontos no mapa de “pink” para “verde-escuro”
# R:

data_mapa_verde = data[['id', 'lat', 'long', 'price']]

mapa_verde = px.scatter_mapbox(data_frame=data_mapa_verde, lat='lat', lon='long',
                         hover_name='id', hover_data=['price'],
                         color_discrete_sequence=['darkgreen'],
                         zoom=3, height=600,
                         mapbox_style='open-street-map')

mapa_verde.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})

mapa_verde.write_html('../datasets/mapa_house_rocket_verde.html')
