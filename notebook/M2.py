import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

def generar_rango_salarial(seniority, cantidad_de_skills):
    base_salary = 30000
    skill_factor = 1000
    seniority_factor = {'Entry': 1, 'Mid': 1.5, 'Senior': 2, 'Executive': 2.5, 'Full Time': 1.25}

    salario = base_salary + (cantidad_de_skills * skill_factor) * seniority_factor[seniority]
    rango_salarial = (salario * 0.9, salario * 1.1)  # Establece un rango salarial con un +/- 10% de variación
    return rango_salarial

# Carga tu dataframe de pandas
data = pd.read_csv('df_modelo_1_v2.csv')
data['cantidad_de_skills'] = data['skills'].apply(lambda x: len(x.split(',')))
data['rango_salarial'] = data.apply(lambda row: generar_rango_salarial(row['level_job'], row['cantidad_de_skills']), axis=1)

# Reemplazar los valores nulos en las columnas 'job_title' y 'level_job' con 'Desconocido'
data['job_title'] = data['job_title'].fillna('Desconocido')
data['level_job'] = data['level_job'].fillna('Desconocido')

# Preprocesamiento: One-hot encoding para las variables categóricas 'rol' y 'seniority'
preprocessor = make_column_transformer(
    (OneHotEncoder(), ['job_title', 'level_job']),
    remainder='passthrough'
)

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Crear el pipeline de preprocesamiento y el modelo
pipeline = make_pipeline(preprocessor, modelo)

# Dividir los datos en conjuntos de entrenamiento y prueba
X = data[['job_title', 'level_job', 'cantidad_de_skills']]
y = data['rango_salarial']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Definir las opciones para el selector múltiple de Streamlit
roles = data['job_title'].unique()
seniorities = data['level_job'].unique()

st.title('Predicción de rango salarial')

selected_rol = st.selectbox('Selecciona el rol', options=sorted(roles))
selected_seniority = st.selectbox('Selecciona la seniority', options=sorted(seniorities))
selected_skills = st.slider('Cantidad de habilidades', min_value=1, max_value=50, value=10)

# Realizar predicciones con las opciones seleccionadas
input_data = pd.DataFrame({'job_title': [selected_rol], 'level_job': [selected_seniority], 'cantidad_de_skills': [selected_skills]})
