import streamlit as st

# ===============================
# Datos de entrada (Fase 1)
# ===============================

# Currículo Antiguo
curriculum_antiguo = [
    {"nombre": "Ingles nivel 2", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Competencias idiomáticas básicas", "semestre": 1, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Introducción a la investigación en psicología", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Percepción, Atención y Memoria", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Psicobiología", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Historia y fundamentos de la psicología", "semestre": 1, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Core, Curriculum persona y cultura I", "semestre": 2, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Ingles nivel 3", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Competencias básicas digitales", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Pensamiento y Lenguaje", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Investigación cuantitativa", "semestre": 2, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Neurociencias", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Core, Curriculum persona y cultura II", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Inglés nivel 4", "semestre": 3, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Escuela Psicológica I", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Psicología del desarrollo", "semestre": 3, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Escuela psicológica II", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Métodos y análisis cuantitativos", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Electiva general I", "semestre": 3, "creditos": 2, "prerrequisitos": []}
]

# Currículo Nuevo
curriculum_nuevo = [
    {"nombre": "Ingles nivel 2", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Competencias idiomáticas básicas", "semestre": 1, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Introducción a la investigación en psicología", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Percepción y Atención", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Memoria y Aprendizaje", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Historia y fundamentos de la psicología", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Electivas", "semestre": 1, "creditos": 1, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Core, Curriculum persona y cultura I", "semestre": 2, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Ingles nivel 3", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Competencias básicas digitales", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Pensamiento y Lenguaje", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Investigación cuantitativa", "semestre": 2, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Funciones Ejecutivas y Cognición Social", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Modelos de Aprendizaje", "semestre": 2, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Core, Curriculum persona y cultura II", "semestre": 3, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Inglés nivel 4", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Problemas sociales contemporáneos", "semestre": 3, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Psicología del desarrollo", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Micropractica 1", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Métodos y análisis cuantitativos", "semestre": 3, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Electivas", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 3}
]

# Convalidaciones y mapeo de electivas
convalidaciones = {
    "Ingles nivel 2": "Ingles nivel 2",
    "Competencias idiomáticas básicas": "Competencias idiomáticas básicas",
    "Introducción a la investigación en psicología": "Introducción a la investigación en psicología",
    "Percepción, Atención y Memoria": "Percepción y Atención",  # Convalidación parcial
    "Psicobiología": "Memoria y Aprendizaje",  # Convalidación parcial
    "Historia y fundamentos de la psicología": "Historia y fundamentos de la psicología",
    "Core, Curriculum persona y cultura I": "Core, Curriculum persona y cultura I",
    "Ingles nivel 3": "Ingles nivel 3",
    "Competencias básicas digitales": "Competencias básicas digitales",
    "Pensamiento y Lenguaje": "Pensamiento y Lenguaje",
    "Investigación cuantitativa": "Investigación cuantitativa",
    "Neurociencias": "Funciones Ejecutivas y Cognición Social",
    "Core, Curriculum persona y cultura II": "Core, Curriculum persona y cultura II",
    "Inglés nivel 4": "Inglés nivel 4",
    "Psicología del desarrollo": "Psicología del desarrollo",
    "Métodos y análisis cuantitativos": "Métodos y análisis cuantitativos",
    "Escuela Psicológica I": "Electivas",  # Mapeo a Electivas
    "Escuela psicológica II": "Electivas",  # Mapeo a Electivas
    "Electiva general I": "Electivas"
}

# ===============================
# Interfaz de Usuario (Fase 2)
# ===============================

st.title("App de Transición Curricular")

st.header("Datos del Estudiante")
english_level = st.number_input("Nivel de Inglés (1-7)", min_value=1, max_value=7, value=1, step=1)
english_homologado = st.checkbox("¿Ha sido homologado el inglés?")
semestre_actual = st.number_input("Semestre Actual", min_value=1, value=1, step=1)

st.header("Materias cursadas (Currículo Antiguo)")
st.write("Seleccione las materias que ya ha cursado:")
# Generamos un checkbox para cada materia del currículo antiguo
selected_courses = []
for course in curriculum_antiguo:
    if st.checkbox(course["nombre"], key=course["nombre"]):
        selected_courses.append(course)

# ===============================
# Lógica de Cálculo y Reporte (Backend)
# ===============================

if st.button("Verificar Elegibilidad"):
    # Determinar límite de créditos según nivel de inglés/homologación
    credit_limit = 64 if english_homologado or english_level >= 5 else 48

    # Sumar créditos cursados en el currículo antiguo
    total_credits = sum(course["creditos"] for course in selected_courses)

    # Verificar si se han cursado materias de semestres avanzados (4 o superior)
    advanced_courses = [course for course in selected_courses if course["semestre"] >= 4]

    # Inicializamos variables de elegibilidad y mensajes de error
    elegible = True
    razones_no_elegible = []

    if total_credits > credit_limit:
        elegible = False
        razones_no_elegible.append(
            f"Ha superado el límite de créditos permitidos para la transición ({total_credits} créditos cursados, límite {credit_limit})."
        )
    if advanced_courses:
        elegible = False
        nombres_advanced = ", ".join(course["nombre"] for course in advanced_courses)
        razones_no_elegible.append(
            f"Ha cursado materias de semestres avanzados del currículo antiguo: {nombres_advanced}."
        )
    # Criterio adicional: Si el estudiante se encuentra en un semestre avanzado (4 o superior)
    if semestre_actual >= 4:
        elegible = False
        razones_no_elegible.append("El estudiante se encuentra en un semestre avanzado (4 o superior), lo cual impide la transición.")

    # Mostrar resultados según elegibilidad
    if elegible:
        st.success("Elegible para Cambio de Currículo: Sí")

        # -------------------------------
        # Convalidaciones: identificar cursos aprobados
        # -------------------------------
        convalidados = []
        for course in selected_courses:
            nombre = course["nombre"]
            if nombre in convalidaciones:
                mapped = convalidaciones[nombre]
                if mapped not in convalidados:
                    convalidados.append(mapped)
        st.subheader("Cursos convalidados en el currículo nuevo:")
        if convalidados:
            for c in convalidados:
                st.write(f"- {c}")
        else:
            st.write("No se han identificado convalidaciones directas.")

        # -------------------------------
        # Cálculo de materias pendientes
        # -------------------------------
        pending_courses = [course for course in curriculum_nuevo if course["nombre"] not in convalidados]
        st.subheader("Cursos pendientes por cursar en el currículo nuevo:")
        if pending_courses:
            for course in pending_courses:
                st.write(f"- {course['nombre']} (Semestre {course['semestre']}, {course['creditos']} créditos)")
        else:
            st.write("No hay cursos pendientes. ¡Felicidades!")

        # Calcular créditos totales del currículo nuevo y créditos ya convalidados
        total_new_credits = sum(course["creditos"] for course in curriculum_nuevo)
        convalidados_credits = sum(course["creditos"] for course in curriculum_nuevo if course["nombre"] in convalidados)
        creditos_pendientes = total_new_credits - convalidados_credits

        st.write(f"**Créditos pendientes por completar:** {creditos_pendientes}")

        # -------------------------------
        # Recomendaciones para el próximo semestre
        # -------------------------------
        if pending_courses:
            # Se priorizan las materias del semestre más bajo entre las pendientes
            min_semestre = min(course["semestre"] for course in pending_courses)
            recommended = [course for course in pending_courses if course["semestre"] == min_semestre]
            st.subheader("Recomendaciones para el próximo semestre:")
            for course in recommended:
                st.write(f"- {course['nombre']} (Semestre {course['semestre']})")
    else:
        st.error("Elegible para Cambio de Currículo: No")
        st.subheader("Razones:")
        for razon in razones_no_elegible:
            st.write(f"- {razon}")

    st.info("NOTA: Necesitamos que tengas asesoría personalizada para finalizar el proceso de transición curricular.")
