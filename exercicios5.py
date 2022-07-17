import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache(allow_output_mutation=True)
def show_types(data):
    print(data.dtypes)
    return None


def show_dimensions(data):
    print(f'\nNumber of rows: {data.shape[0]} \nNumber of columns: {data.shape[1]}', end='\n\n')
    return None


def data_collect(path):
    data = pd.read_csv(path)

    show_dimensions(data)

    show_types(data)

    return data


def data_transform(data):
    data['level'] = data['price'].apply(lambda x: '0' if x < 321950 else
                                        '1' if (x >= 321950) & (x < 450000) else
                                        '2' if (x >= 450000) & (x < 645000) else '3')

    data['is_waterfront'] = data['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')

    data['year'] = pd.to_datetime(data['date']).dt.strftime('%Y')
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    data['year_week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')

    return data


st.title("House Rocket Company")
st.markdown('Welcome to House Rocket Data Analysis')

st.header('Load data')

data_raw = data_collect('datasets/kc_house_data.csv')

data_processing = data_transform(data_raw)

st.dataframe(data_processing.head())

st.title('House Rocket Map')
is_check = st.checkbox('Display Map')

price_limit = st.slider('Price Range',
                        int(data_processing['price'].min()),
                        int(data_processing['price'].max()),
                        int(data_processing['price'].mean()))

if is_check:
    houses = data_processing[(data_processing['price'] <= price_limit)][['id', 'lat', 'long', 'price', 'level']].copy()

    fig = px.scatter_mapbox(houses,
                            lat='lat',
                            lon='long',
                            color='level',
                            size='price',
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=15,
                            zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r': 0, 'l': 0, 'b': 0, 't': 0})
    st.plotly_chart(fig)
