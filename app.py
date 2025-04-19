import pandas as pd
import plotly.express as px
import streamlit as st
import os

# Verificar si el archivo existe
if os.path.exists('vehicles_us.csv'):
    car_data = pd.read_csv('vehicles_us.csv')
else:
    st.error("El archivo 'vehicles_us.csv' no se encuentra en el directorio del proyecto.")

# Encabezado personalizado
st.title("Proyecto Josué")
st.subheader("Herramientas de desarrollo de software")

# Configuración de colores
color_histogram = 'red'
color_scatter = 'blue'

# Botones principales
st.markdown("### Visualizaciones")
col1, col2 = st.columns(2)

with col1:
    hist_button = st.button('Construir histograma')
with col2:
    scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write('Creando un histograma para comparar "model" y "price"')
    fig = px.histogram(car_data, x="model", y="price", title="Histograma de Precio por Modelo", color_discrete_sequence=[color_histogram])
    st.plotly_chart(fig, use_container_width=True, key="histograma")

if scatter_button:
    st.write('Creando un gráfico de dispersión entre "model" y "price"')
    fig_scatter = px.scatter(car_data, x="model", y="price", title="Gráfico de Dispersión: Modelo vs Precio", color_discrete_sequence=[color_scatter])
    st.plotly_chart(fig_scatter, use_container_width=True, key="dispersion")

# Lista desplegable para gráfico de barras por marca
st.markdown("### Análisis por marca")
brands = car_data['model'].dropna().unique()
selected_brand = st.selectbox("Selecciona una marca", sorted(brands))

filtered_data = car_data[car_data['model'] == selected_brand]
fig_bar = px.histogram(filtered_data, x="price", title=f"Distribución de precios - {selected_brand}", color_discrete_sequence=['darkblue'])
st.plotly_chart(fig_bar, use_container_width=True, key="bar_chart")
