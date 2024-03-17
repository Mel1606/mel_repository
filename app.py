import pandas as pd
import plotly.express as px
import streamlit as st
        
st.header('Diagramas')        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
dis_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
# crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dis_button: # al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
# crear un histograma
    dis = px.scatter(car_data, x="odometer", y='price')
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(dis, use_container_width=True)