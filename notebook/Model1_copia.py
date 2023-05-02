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
    "Ingrese el título del trabajo y las habilidades requeridas para ver si el candidato es apto o no.")

title = st.multiselect("Título del trabajo", df.job_title.unique())
skills = st.multiselect("Habilidades requeridas", sorted(list(all_skills)))


# Crear una función que predice la aptitud para un nuevo título y habilidades
def predict_aptitude(title, skills):
    # Crear una matriz de características con las habilidades de la nueva entrada
    skills_str = ", ".join(skills)
    X_new = vectorizer.transform([skills_str])

    # Predecir la aptitud con el modelo
    y_pred = clf.predict(X_new)
    y_prob = clf.predict_proba(X_new)

    # Retornar la predicción y la probabilidad
    return y_pred[0], y_prob[0][1]


if title and skills:
    # Predecir la aptitud con el modelo
    skills_list = [skill.strip() for skill in skills]
    aptitude, probability = predict_aptitude(title, skills_list)

    # Mostrar la predicción con un color de fondo basado en la probabilidad
    if probability >= 0.8:
        st.markdown(
            f"<div style='background-color: green; padding: 0.25em 0.5em; border-radius: 0.25em;'>El candidato es <b>{'apto' if aptitude == 1 else 'no apto'}</b> para el trabajo de <b>{title}</b> con una probabilidad del <b>{probability:.2f}</b>.</div>",
            unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color: red; padding: 0.25em "
                    f"0.5em; border-radius: 0.25em;'>El candidato es <b>{'apto' if aptitude == 0 else 'no apto'}</b> para el trabajo de <b>{title}</b> con una probabilidad del <b>{probability:.2f}</b>.</div>",
                    unsafe_allow_html=True)
