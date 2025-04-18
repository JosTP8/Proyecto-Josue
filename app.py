import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('C:/Users/Josué/Documents/Github/Proyecto-Josue/notebooks/vehicles_us.csv')



# Crear encabezado
st.header('Análisis de vehículos de segunda mano')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creando un histograma para la columna "odometer"')
    # Crear histograma con Plotly Express
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odometer")
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creando un gráfico de dispersión entre "price" y "odometer"')
    # Crear gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Odometer vs Price")
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

# Desafío adicional: Casillas de verificación
st.sidebar.header('Opciones de visualización')

build_histogram = st.sidebar.checkbox('Construir un histograma')
build_scatter = st.sidebar.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Construir un histograma para la columna "odometer"')
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma de Odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Construir un gráfico de dispersión entre "price" y "odometer"')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Odometer vs Price")
    st.plotly_chart(fig_scatter, use_container_width=True)
