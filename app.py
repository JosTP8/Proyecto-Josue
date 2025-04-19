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
    st.write('Creando un histograma para la columna "odometer"')
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odometer", color_discrete_sequence=[color_histogram])
    st.plotly_chart(fig, use_container_width=True, key="histograma")

if scatter_button:
    st.write('Creando un gráfico de dispersión entre "price" y "odometer"')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Odometer vs Price", color_discrete_sequence=[color_scatter])
    st.plotly_chart(fig_scatter, use_container_width=True, key="dispersion")

# Opciones en barra lateral
st.sidebar.header('Opciones de visualización')
build_histogram = st.sidebar.checkbox('Construir un histograma')
build_scatter = st.sidebar.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Histograma para la columna "odometer"')
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma de Odometer", color_discrete_sequence=[color_histogram])
    st.plotly_chart(fig_hist, use_container_width=True, key="histograma_sidebar")

if build_scatter:
    st.write('Gráfico de dispersión entre "price" y "odometer"')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Odometer vs Price", color_discrete_sequence=[color_scatter])
    st.plotly_chart(fig_scatter, use_container_width=True, key="dispersion_sidebar")

# Lista desplegable para gráfico de barras por marca
st.markdown("### Análisis por marca")
brands = car_data['model'].dropna().unique()
selected_brand = st.selectbox("Selecciona una marca", sorted(brands))

filtered_data = car_data[car_data['model'] == selected_brand]
fig_bar = px.histogram(filtered_data, x="price", title=f"Distribución de precios - {selected_brand}", color_discrete_sequence=['darkblue'])
st.plotly_chart(fig_bar, use_container_width=True, key="bar_chart")
