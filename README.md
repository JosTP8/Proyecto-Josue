# **Aplicación Web Interactiva de Visualización de Datos de Vehículos Usados**  
Desarrollada con **Streamlit**, **Pandas** y **Plotly Express**

---

## 📄 Descripción del Proyecto

Esta aplicación web permite explorar de forma interactiva un conjunto de datos sobre vehículos usados, facilitando el análisis visual a través de gráficos generados dinámicamente. Está pensada como una herramienta de apoyo para la comprensión de patrones en el mercado de autos en venta.

---

## 📂 Fuente de Datos

Se utiliza el archivo `vehicles_us.csv`, que contiene información detallada sobre vehículos a la venta. Algunas columnas relevantes del dataset incluyen:

- `model`: Marca del vehículo  
- `price`: Precio en dólares (USD)  
- `odometer`: Kilometraje registrado  
- `condition`: Condición general del vehículo  
- `type`, `transmission`, `fuel`, `paint_color`, entre otras  

---

## ⚙️ Funcionalidades de la Aplicación

### 🔘 Botones Interactivos

- **Histograma general**:  
  Muestra la distribución de precios por marca de vehículo.

- **Gráfico de dispersión**:  
  Compara el precio promedio de los vehículos por cada marca.

### 🔍 Análisis por Marca

- El usuario puede seleccionar una **marca específica** desde un menú desplegable.
- Se genera un **histograma personalizado** con la distribución de precios para la marca elegida.

---

## 🌐 Enlace a la Aplicación Web

Haz clic aquí para abrir la app:  
👉 [https://proyecto-josue.onrender.com](https://proyecto-josue.onrender.com)

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.13**
- **Streamlit**
- **Pandas**
- **Plotly Express**
