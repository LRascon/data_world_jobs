import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

df = pd.read_csv('df_modelo_1_v2.csv')

df['Aptitude_Code'] = df['Aptitude'].apply(lambda x: 1 if x == 'Apto' else 0)

all_skills = list(set([skill for skills in df.skills for skill in skills.split(", ")]))

encoded_data = pd.get_dummies(df['skills'].apply(lambda x: pd.Series(x.split(", "))).stack()).sum(level=0)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(encoded_data, df['Aptitude_Code'], test_size=0.3, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)

st.title("¿Eres apto para el trabajo?")

job_categories = ['ml', 'engineer', 'data scientist', 'analyst']
job_category = st.selectbox('Selecciona el cargo de trabajo para el que deseas evaluar tus habilidades:', job_categories)

skills_options = st.multiselect('Selecciona tus habilidades:', all_skills)

if len(skills_options) == 0:
    st.warning('Debes seleccionar al menos una habilidad.')
else:
    user_skills = pd.DataFrame([[1 if skill.strip() in skills_options else 0 for skill in all_skills]], columns=all_skills)
    user_skills = user_skills.reindex(columns=X_train.columns, fill_value=0)

    aptitude_percentage = 0

    for skill in skills_options:
        if skill in encoded_data.columns and X_train[f'{job_category}_{skill}'].values[0] == 1:
            skill_prob = clf.predict_proba(user_skills)[0][1]
            aptitude_percentage += skill_prob

    if aptitude_percentage > 0:
        aptitude_percentage *= 100 / len(skills_options)
        if aptitude_percentage > 75:
            st.success(f"¡Felicidades! Parece que eres apto para este trabajo de {job_category} con un porcentaje de aptitud del {round(aptitude_percentage, 2)}%.")
        else:
            st.error(f"Lo sentimos, no pareces ser apto para este trabajo de {job_category} con un porcentaje de aptitud del {round(aptitude_percentage, 2)}%.")
    else:
        st.error(f"Lo sentimos, no pareces tener las habilidades necesarias para este trabajo de {job_category}.")