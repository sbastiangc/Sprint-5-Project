import pandas as pd
import plotly.express as px
import streamlit as st

# Introducir un header
st.header('Estudio anuncios de venta de vehículos')

# historgrama
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

hist_var = list(car_data.columns.values)
selected_var = st.selectbox("Seleccionar una variable", hist_var)
st.write('Crea una gráfica para conocer más acerca de los anuncios')

hist_button = st.button('Construir histograma')  # crear un botón


def histogram():

    if hist_button:  # al hacer clic en el botón
        # escribir un mensaje

        # crear un histograma
        fig = px.histogram(car_data, selected_var, color="condition",
                           title=f"Histograma de: {selected_var} por cada categoría de condición")

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True, theme=None)


# ejecutar funcion de histograma
if hist_button:
    histogram()


# grafico de dispersion
show_scatter_checkbox = st.checkbox(
    "Gráfico de Dispersión de Precio vs. Año vs. Condición para cada modelo")


# definir un grafico de dispersion interactivo
# filtros para el grafico
def dispersion():

    car_type = car_data['type'].unique()
    car_model = car_data['model'].unique()

    if show_scatter_checkbox:
        # variables para selecion del usuario
        selected_type = st.selectbox("Seleccionar tipo de automóvil", car_type)

        car_model = car_data[car_data['type']
                             == selected_type]['model'].unique()
        # car_model = car_data['model'].unique()

        seleceted_model = st.selectbox(
            "Seleccionar modelo de automóvil", car_model)

        # data frame a graficar
        filtered_data = car_data[(car_data['type'] == selected_type) & (
            car_data['model'] == seleceted_model)]

        # crear grafico de dispersion
        fig = px.scatter(filtered_data, x="model_year", y="price", color="condition",
                         title=f"Gráfico de Dispersión de Precio vs. Año por condición del Modelo: {selected_type} - {seleceted_model}")
        st.plotly_chart(fig, use_container_width=True)


# ejecutar grafico de dispersion
if show_scatter_checkbox:
    dispersion()
