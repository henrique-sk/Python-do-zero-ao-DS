import pandas as pd
import plotly.express as px

data = pd.read_csv('../datasets/kc_house_data.csv')

# Gostaria de um Mapa indicando onde as casas estão localizadas geograficamente
# R:

data_mapa = data[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(data_frame=data_mapa, lat='lat', lon='long',
                         hover_name='id', hover_data=['price'],
                         color_discrete_sequence=['fuchsia'],
                         zoom=3,
                         height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
# right, top, left, bottom
mapa.show()

mapa.write_html('../datasets/mapa_house_rocket.html')
