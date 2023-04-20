import datetime
import time

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

st.title('Predicción de nuevos puestos de trabajo')

# Cargar los datos
df = pd.read_csv('/home/catriel/Documents/data_world_jobs/data/ds_salaries.csv')

# Seleccionar las columnas relevantes
df_relevant = df[['job_title', 'work_year']]

# Transformar la columna work_year en un tipo date en la columna date
df_relevant['date'] = pd.to_datetime(df_relevant['work_year'], format='%Y')

# Agregar una columna con el año de creación
df_relevant['year'] = pd.DatetimeIndex(df_relevant['date']).year

# Contar la cantidad de job_title creados por año
job_title_count = df_relevant.groupby('year').count()['job_title']

# Crear un dataframe con la cantidad de job_title creados por año
df_job_title_count = pd.DataFrame(
    {'year': job_title_count.index, 'job_title_count': job_title_count.values})

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos históricos
X = df_job_title_count[['year']]
y = df_job_title_count['job_title_count']
model.fit(X, y)

# Obtener el año actual
current_year = datetime.datetime.now().year

# Predecir la cantidad de nuevos job_title que se crearán este año
current_year_input = st.number_input('Ingresa un año:', value=current_year,
                                     min_value=current_year,
                                     max_value=2050, step=1)
if current_year_input < current_year:
    st.warning('Solo se pueden hacer predicciones para años futuros.')
    current_year_input = current_year
    st.write('Se usará el año actual:', current_year_input)

with st.spinner('Prediciendo...'):
    time.sleep(2)
    job_title_count_pred = model.predict([[current_year_input]])

# Obtener el último año del dataset
last_year = df_job_title_count['year'].max()
last_year_count = \
    df_job_title_count.loc[df_job_title_count['year'] == last_year][
        'job_title_count'].values[0]

# Imprimir los resultados
st.write(
    "Se crearán aproximadamente **{}** nuevos puestos de trabajo este año **{}**.".format(
        int(job_title_count_pred), current_year_input))
percentage_change = (
                            job_title_count_pred - last_year_count) / last_year_count * 100
percentage_change = float(percentage_change)
if percentage_change >= 0:
    st.write("Esto representa un aumento del {:.2f}% con respecto al año {}.".format(percentage_change,
                                                       last_year))
else:
    st.write("Esto representa una disminución del {:.2f}% con respecto al año {}".format(abs(percentage_change), last_year))
