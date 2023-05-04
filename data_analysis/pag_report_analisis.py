import streamlit as st

def main():
    st.title("Propuesta de Proyecto")
    st.write("""
    Es por todo esto que Latam Brain, una empresa líder en ciencia de datos, ha diseñado un 
    proyecto revolucionario que aborda este desafío de frente. Este proyecto se basa en 
    cuatro objetivos fundamentales:
    • Recopilar datos de todas las ofertas de empleo relacionadas con la ciencia de datos 
    y crear un data warehouse, un recurso invaluable para almacenar y analizar 
    información de manera eficiente.
    • Obtener un panorama general de la situación actual del mercado laboral en el 
    ámbito de la ciencia de datos tanto a nivel mundial como en América Latina.
    • Identificar las características clave que definen a los profesionales en este campo, 
    como habilidades, herramientas y funciones, y su relación con el nivel de salario.
    • Crear un modelo predictivo utilizando Machine Learning para identificar patrones y 
    tendencias en los datos generados por las distintas fuentes de información.
    """)

    st.header("Nuestro proyecto, con su amplio alcance y enfoque en el análisis exhaustivo de las ofertas laborales,busca revolucionar la forma en que las empresas de reclutamiento identifican y contratan a profesionales especializados en ciencia de datos y análisis.")
    st.write("""
    Lo que te ofrecemos:
    • Base de Datos en la nube (aws) que nos ayude a descubrir las habilidades y 
    herramientas más demandadas en el mercado. Con esta información, pueden 
    afinar su búsqueda y encontrar a los candidatos ideales para sus clientes. A su vez, 
    los candidatos pueden mejorar sus habilidades y aumentar sus posibilidades de 
    conseguir empleo en empresas que se ajusten a sus metas profesionales.
    • Dashboards de Analítica que nos permita visualizar las tendencias y características 
    que nos permitan tomar mejores decisiones en el mercado laboral dedicado en 
    este caso a Data.
    • El modelo predictivo de Machine Learning, como el cerebro detrás de todo el 
    proyecto, permitirá anticipar tendencias y patrones en la demanda de talento, lo 
    que permitirá a las empresas de reclutamiento estar siempre un paso adelante y 
    adaptarse a las necesidades cambiantes del mercado.
    """)

    st.header("Con este proyecto, Latam Brain no solo está cambiando el juego en la industria del reclutamiento, sino que también está creando un puente entre el talento y las empresas en la era del Big Data. Juntos, estamos construyendo un futuro donde las empresas y los profesionales pueden alcanzar su máximo potencial, gracias a la unión perfecta entre la ciencia de datos y el reclutamiento en la era de la Transformación Digital")


    st.title("Análisis de mercado y recomendaciones")   

    st.header("Dashboard Vistazo General el Mercado Laboral Empleos Data")  

    # Cargar y mostrar la imagen
    imagen_1 = "data_viz\Dashboard_Vistazo_al_Mercado_Actual.png"
    st.image(imagen_1, caption="Dashboard Vistazo el Mercado Actual.", use_column_width=True)

    st.write("""
    En el siguiente enlace puede acceder al Dashboard dinámico -> [link](https://public.tableau.com/views/latam_brain_context/DashboardVistazoelMercadoActual?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)   

    Basándonos en los hallazgos del dashboard de visión general relacionado a los empleos de data, podemos hacer el siguiente análisis y recomendaciones:
    """)    

    st.header("Análisis")   

    st.write("""
    1. El salario promedio anual en empleos de data ha experimentado un crecimiento significativo (30%) entre 2019 y 2020, lo que indica una alta demanda y valoración de los profesionales en este campo.
    2. El número de empleos relacionados con data ha aumentado en un sorprendente 450%, lo que demuestra un interés creciente por parte de las empresas en contratar profesionales con habilidades en ciencia de datos y análisis.
    3. La mayoría de los empleados en este campo se encuentran en compañías medianas (más del 50%), lo que sugiere que estas empresas podrían estar invirtiendo más en ciencia de datos y análisis que las pequeñas o grandes empresas.
    4. En cuanto a la antigüedad, hay una mayor cantidad de empleados en puestos senior, seguido de semisenior, junior y, por último, expert. Esto indica que las empresas están buscando profesionales con experiencia en el campo, aunque también hay oportunidades para aquellos con menos experiencia.
    5. La mayoría de los empleos en este campo se ofrecen en modalidad remota, lo que puede atraer a una amplia gama de candidatos y permitir una mayor flexibilidad en la contratación y el trabajo.
    """)

    st.header("Recomendaciones")

    st.write("""
    • Como empresa de reclutamiento, enfóquense en buscar candidatos con experiencia en ciencia de datos y análisis, ya que estos perfiles son altamente demandados. Además, consideren ofrecer capacitación y desarrollo profesional para ayudar a los candidatos a avanzar en sus carreras y mejorar sus habilidades.
    • Atraigan a los profesionales de la ciencia de datos ofreciendo salarios competitivos y oportunidades de crecimiento, ya que el salario promedio anual en este campo está en aumento.
    • Las pequeñas y grandes empresas podrían considerar aumentar su inversión en ciencia de datos y análisis, ya que las compañías medianas parecen estar liderando en este aspecto.
    • Las empresas deben adaptarse a las tendencias actuales de contratación y ofrecer puestos de trabajo en modalidad remota cuando sea posible. Esto no solo ampliará el grupo de candidatos, sino que también puede aumentar la satisfacción y la retención de los empleados.
    • Y para loos profesionales que buscan empleo en el campo de la ciencia de datos deben enfocarse en adquirir habilidades y experiencia relevantes, especialmente en áreas de alta demanda. Además, pueden considerar buscar oportunidades de trabajo remoto, ya que estas parecen ser predominantes en la industria.
    """)



    st.title("Dashboards especializados como herramientas de Análisis")

    st.header("Dashboard General Data Jobs")

    # Cargar y mostrar la imagen
    imagen_2 = "data_viz\Dashboard_General_Data_Jobs.png"
    st.image(imagen_2, caption="Dashboard General Data Jobs.", use_column_width=True)

    st.write("""
    En el siguiente enlace puede acceder al Dashboard dinámico -> [link](https://public.tableau.com/views/latam_brain_mvp_la/DashboardGeneralDataJobs?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

    "El futuro del empleo en Ciencia de Datos: Un vistazo a nuestros revolucionarios Dashboards de Análisis" -Latam Brain
    """)

    st.write("""
    Nuestro Dashboard General Data Jobs cuenta con una serie de gráficos esclarecedores que abarcan diferentes aspectos del mercado laboral en el campo de la Ciencia de Datos. El dashboard que atraves de cada uno de los gráficos nos muestra información pertinente para la toma de decisiones informadas y estratégicas.
    """)

    st.header("Gráficos y lo que nos permiten visualizar")

    st.write("""
    1. Participación de empleos por rol: Este gráfico muestra la distribución de empleos en el ámbito de la Ciencia de Datos entre diferentes roles, como científicos, analistas, ingenieros y especialistas en Machine Learning. Con esta información, podrán identificar las áreas de mayor demanda y adaptar sus estrategias de reclutamiento o formación en consecuencia.
    2. Participación de empleos por tipo: Aquí, visualizamos la proporción de empleos según su tipo: tiempo completo, freelance, pasantías y contratos. Esto les permitirá evaluar la naturaleza del mercado laboral y considerar qué tipo de contratación es más adecuado para sus necesidades empresariales.
    3. Participación de mercado en empleos por modalidad: Este gráfico compara la cantidad de empleos que son presenciales y remotos, lo que les ayudará a comprender la prevalencia de cada modalidad y adaptar sus ofertas de trabajo para satisfacer las expectativas de los profesionales en la actualidad.
    4. Salario promedio anual por antigüedad: Aquí, observamos la relación entre el salario promedio anual y la antigüedad del empleado, desde ejecutivos hasta empleados de nivel inicial. Este conocimiento les permitirá establecer salarios competitivos y atractivos para atraer y retener talento en cada nivel de experiencia.
    5. Salario promedio anual por rol: Este gráfico muestra el salario promedio anual en función del rol, ya sea científico, analista, ingeniero o especialista en Machine Learning. Con esta información, podrán comparar los salarios entre roles y asegurarse de que sus ofertas salariales sean competitivas dentro del mercado.
    6. Participación de mercado por país: Aquí, analizamos la distribución geográfica de los empleos en Ciencia de Datos, lo que les permitirá identificar las áreas geográficas con mayor demanda de profesionales y ajustar sus estrategias de contratación o expansión en consecuencia.
    7. Top 10 países por salario promedio anual: Por último, este gráfico presenta los 10 países con los salarios promedio anuales más altos en el ámbito de la Ciencia de Datos. Este conocimiento les permitirá evaluar la competitividad de sus salarios a nivel internacional y tomar decisiones informadas sobre dónde enfocar sus esfuerzos de contratación.
    """)



    st.header("Dashboard Latino América Data Jobs")

    # Cargar y mostrar la imagen
    imagen_3 = "data_viz\Dashboard_Latinoamerica_Data_Jobs.png"
    st.image(imagen_3, caption="Dashboard Latinoamerica Data Jobs.", use_column_width=True)

    st.write("""
    En el siguiente enlace puede acceder al Dashboard dinámico -> [link](https://public.tableau.com/views/latam_brain_mvp_la/DashboardLatinoamericaDataJobs?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)
    """)

    st.write("""
    Nuestro Dashboard Latinoamérica Data Jobs es una solución integral diseñada para proporcionar información valiosa sobre el panorama del empleo en el ámbito de la ciencia de datos en América Latina. Esta herramienta fácil de usar presenta una serie de gráficos que abarcan diversos aspectos del mercado laboral en la región, permitiéndoles tomar decisiones informadas y estratégicas en sus esfuerzos de contratación y expansión. A continuación, les presento una descripción de los gráficos incluidos en nuestro dashboard:
    """)

    st.header("Gráficos y lo que nos permiten visualizar")

    st.write("""
    1. Participación de Mercado Latinoamericano por país: Este gráfico muestra el porcentaje de participación de cada país en cuanto a la cantidad de empleos de data en América Latina. Con esta información, podrán identificar los países con mayor demanda de profesionales en ciencia de datos y enfocar sus esfuerzos de contratación y expansión en consecuencia.
    2. Salario Promedio Anual por Región: Aquí, comparamos el salario promedio anual en el mundo y en América Latina en el ámbito de la ciencia de datos. Esta comparación les permitirá evaluar la competitividad de los salarios en la región y tomar decisiones informadas sobre cómo atraer y retener talento.
    3. Participación del mercado en Empleos Data en América Latina: Este gráfico presenta la participación de cada país en el mercado de empleos de data en América Latina, así como el porcentaje de modalidad (presencial y remota) en cada país. Con esta información, podrán evaluar las tendencias de contratación en la región y adaptar sus ofertas de trabajo para satisfacer las expectativas de los profesionales en el ámbito de la ciencia de datos.
    4. Participación de mercado en empleos Data por Rol en porcentaje: Este gráfico muestra la distribución de empleos en el ámbito de la ciencia de datos en América Latina entre diferentes roles, como científicos, analistas, ingenieros y especialistas en Machine Learning. Con esta información, podrán identificar las áreas de mayor demanda y adaptar sus estrategias de reclutamiento o formación en consecuencia.
    5. Salario Promedio Anual en USD por país: Por último, este gráfico presenta el salario promedio anual en dólares estadounidenses para cada país en América Latina. Este conocimiento les permitirá evaluar la competitividad de sus salarios a nivel regional y tomar decisiones informadas sobre dónde enfocar sus esfuerzos de contratación.
    """)

    st.write("""
    En resumen, nuestros revolucionarios Dashboards de Análisis son unas herramientas poderosas que les proporcionan información valiosa sobre el mercado laboral en el ámbito de la Ciencia de Datos. Al aprovechar esta información, podrán tomar decisiones informadas y estratégicas que les permitirán atraer y retener a los mejores talentos en el campo, mantenerse competitivos en el mercado y, en última instancia, impulsar el crecimiento y éxito de su empresa.
    """)

    st.write("""
    Nuestro equipo de expertos en ciencia de datos y análisis ha trabajado incansablemente para diseñar y desarrollar este dashboard, asegurando que sea fácil de usar, visualmente atractivo y, lo más importante, útil en la toma de decisiones empresariales.
    """)

    st.write("""
    Les invitamos a explorar nuestro Dashboard de Análisis y experimentar por sí mismos cómo esta herramienta puede transformar la forma en que abordan el empleo en el ámbito de la Ciencia de Datos. Estamos seguros de que, al integrar esta información en sus estrategias de contratación, formación y desarrollo, podrán mantenerse a la vanguardia en este campo en constante evolución y crecimiento.
    """)

    st.write("""
    Si tienen alguna pregunta o necesitan más información sobre cómo nuestros Dashboards de Análisis puede ayudarles a alcanzar sus objetivos empresariales, no duden en ponerse en contacto con nosotros. Estamos aquí para apoyarles en cada paso del camino hacia el éxito en el emocionante mundo de la Ciencia de Datos.
    """)



if __name__ == "__main__":
    main()
