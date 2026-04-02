import pandas as pd
import plotly.graph_objects as go # Importación de plotly.graph_objects como go
# vs code tiene problema para cargar streamlit
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# El encabezado
st.header('Analisis de Anuncios de venta de coches')
#Boton para crear un Histograma
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de Anuncios de venta de coches')

    fig = go.Figure(data=[go.Histogram(x=car_data['model_year'], y=car_data['price'],nbinsx=10000)])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Histograma modelo y precio')
    fig.update_xaxes(range=[1949, 2022])  # Limitando el eje x de 0 a 0.2M ya que la mayor parte de los datos stan en este rango
    fig.update_yaxes(range=[0, 5000])
    #fig.update_layout(title_text='Distribución del Odómetro (0-0.2m)')

    fig.update_traces(opacity=0.75,marker_color='#330C73')
    fig.update_layout(
    
    xaxis_title_text='Año', # xaxis label
    yaxis_title_text='Precio', # yaxis label
    )
    st.plotly_chart(fig, use_container_width=True)

# Boton para crear Grafico de Dispersion
dist_button = st.checkbox('Contruir grafico de dispersión')
#Logica
if dist_button:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de Anuncios de venta de coches')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, use_container_width=True)

