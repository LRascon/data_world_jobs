import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Cargar los datos
df = pd.read_csv('dataset_modelo_1.csv')

# Crear una lista con todas las skills disponibles
all_skills = set()
for skills in df.skills:
    all_skills.update(skills.split(", "))

# Crear un diccionario que relaciona cada skill con su índice en el vector
skill_indices = {skill: i for i, skill in enumerate(all_skills)}

# Crear una matriz de características con la frecuencia de cada skill en cada fila
vectorizer = CountVectorizer(vocabulary=skill_indices.keys(), lowercase=False)
X = vectorizer.fit_transform(df.skills)

# Entrenar el modelo
clf = MultinomialNB()
clf.fit(X, df.Aptitude)

# Crear la interfaz de usuario con Streamlit
st.title("Predicción de aptitud para un trabajo")
st.write(
    "Ingrese el título del trabajo para ver las habilidades más importantes.")

title = st.multiselect("Título del trabajo", df.job_title.unique())

# Crear una función que encuentra las habilidades más importantes para un título dado
def get_top_skills(title, limit):
    # Filtrar el dataframe por el título dado
    filtered_df = df[df.job_title == title]

    # Crear una matriz de características con la frecuencia de cada skill en el dataframe filtrado
    X_filtered = vectorizer.transform(filtered_df.skills)

    # Calcular la frecuencia de cada habilidad en el dataframe filtrado
    skill_frequencies = X_filtered.sum(axis=0).A1

    # Obtener los nombres de las habilidades
    skill_names = vectorizer.vocabulary_.keys()

    # Crear un diccionario que relaciona cada habilidad con su frecuencia
    skill_freq_dict = dict(zip(skill_names, skill_frequencies))

    # Ordenar las habilidades por frecuencia descendente y devolver las más importantes (según el límite dado)
    top_skills = sorted(skill_freq_dict, key=skill_freq_dict.get,
                        reverse=True)[:limit]
    return top_skills

if title:
    limit = st.number_input("Cantidad de habilidades a mostrar", value=5, min_value=1, max_value=len(all_skills))
    top_skills = get_top_skills(title[0], limit)
    st.write(f"Las {limit} habilidades más importantes para el trabajo de '{title[0]}' son:")
    for skill in top_skills:
        st.write(f"- {skill}")
