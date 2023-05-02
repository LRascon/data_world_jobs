import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

df = pd.read_csv('dataset_modelo_1.csv')

# Agregar una columna que represente la aptitud del conjunto de habilidades de cada fila en relación al cargo de trabajo correspondiente
aptitude_by_category_job = df.groupby(['category_job', 'Aptitude']).size().unstack().fillna(0)
aptitude_by_category_job['aptitude_ratio'] = aptitude_by_category_job[1] / (aptitude_by_category_job[0] + aptitude_by_category_job[1])
aptitude_by_category_job = aptitude_by_category_job['aptitude_ratio'].to_dict()

# Crear una lista con todas las skills disponibles
all_skills = set()
for skills in df.skills:
    all_skills.update(skills.split(", "))

# Crear un diccionario que relaciona cada skill con su índice en el vector
skill_indices = {}
for i, skill in enumerate(all_skills):
    skill_indices[skill] = i

# Crear una matriz de características con la frecuencia de cada skill en cada fila
vectorizer = CountVectorizer(vocabulary=skill_indices.keys(), lowercase=False)
X = vectorizer.fit_transform(df.skills)

# Entrenar el modelo de clasificación
clf = MultinomialNB()

# Crear la interfaz de usuario con Streamlit
st.title("¿Es apto para el trabajo?")
category_job = st.selectbox("Selecciona el cargo de trabajo:", df.category_job.unique())
skills = st.multiselect("Selecciona tus habilidades:", all_skills)

if len(skills) == 0:
    st.warning("Selecciona al menos una habilidad.")
else:
    # Crear una matriz de características con todas las habilidades
    X_all = X.toarray()

    # Seleccionar las columnas correspondientes a las habilidades seleccionadas
    selected_skills = [skill_indices[skill] for skill in skills]
    X_selected = X_all[:, selected_skills]

    # Calcular la aptitud del conjunto de habilidades seleccionadas en relación al cargo de trabajo correspondiente
    aptitude_ratio = aptitude_by_category_job.get((category_job, 1), 0)

    # Obtener todas las filas de X que correspondan al cargo de trabajo seleccionado
    X_category_job = X[df.category_job == category_job, :]

    # Obtener las etiquetas correspondientes a las filas seleccionadas en X
    y = df[df.category_job == category_job].Aptitude

    # Entrenar el modelo de clasificación con las habilidades seleccionadas y la aptitud correspondiente
    clf.fit(X_category_job[:, selected_skills], y)

    # Predecir la aptitud del usuario con el modelo de clasificación
    y_pred = clf.predict(X_selected)
    y_prob = clf.predict_proba(X_selected)

    # Obtener el porcentaje de aptitud para el cargo de trabajo seleccionado
    aptitude_percentage = round((sum(y_pred) / len(y_pred)) * 100, 2)

    # Mostrar los resultados
    st.write("Para el cargo de trabajo de", category_job, "y las habilidades seleccionadas, el porcentaje de aptitud es del", aptitude_percentage, "%.")

    if aptitude_percentage >= aptitude_ratio:
        st.success("¡Felicidades! Parece que eres apto para este trabajo.")
    else:
        st.error("Lo sentimos, no pareces ser apto para este trabajo.")
 


