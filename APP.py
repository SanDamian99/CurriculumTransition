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
    {"nombre": "Métodos y análisis cuantitativos", "semestre": 3, "creditos": 2, "prerrequisitos": ["Investigación cuantitativa"], "importancia": 4},
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
semestre_actual = st.number_input("Semestre Actual (por tiempo)", min_value=1, value=1, step=1)
doble_programa = st.checkbox("¿Eres estudiante de doble programa?")

st.header("Materias cursadas (Currículo Antiguo)")
st.write("Selecciona las materias cursadas, agrupadas por semestre:")

# Agrupamos las materias por semestre para facilitar la selección
selected_courses = []
courses_by_semester = {}
for course in curriculum_antiguo:
    sem = course["semestre"]
    courses_by_semester.setdefault(sem, []).append(course)

for sem in sorted(courses_by_semester.keys()):
    st.subheader(f"Semestre {sem}")
    for course in courses_by_semester[sem]:
        if st.checkbox(course["nombre"], key=f"{course['nombre']}_old"):
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
            f"Has superado el límite de créditos permitidos para la transición ({total_credits} créditos cursados, límite {credit_limit})."
        )
    if advanced_courses:
        elegible = False
        nombres_advanced = ", ".join(course["nombre"] for course in advanced_courses)
        razones_no_elegible.append(
            f"Has cursado materias de semestres avanzados del currículo antiguo: {nombres_advanced}."
        )
    if semestre_actual >= 4:
        elegible = False
        razones_no_elegible.append("Te encuentras en un semestre avanzado (4 o superior), lo cual impide la transición.")

    # Cálculo del avance según créditos
    # En el currículo antiguo cada semestre equivale a 16 créditos y en el nuevo a 18 créditos.
    old_semesters_completados = total_credits // 16
    old_semestre_actual = old_semesters_completados + (1 if total_credits % 16 != 0 else 0)

    new_semesters_completados = total_credits // 18
    new_semestre_actual = new_semesters_completados + (1 if total_credits % 18 != 0 else 0)
    missing_credits = ((new_semesters_completados + 1) * 18) - total_credits if total_credits < ((new_semesters_completados + 1) * 18) else 0

    # Alertas adicionales:
    # 1. Micropráctica: Si ya terminó tercer semestre (48 créditos o más) se debe hacer en intersemestral.
    if total_credits >= 48:
        st.warning("Recuerda: la 'Micropractica 1' debe cursarse en el intersemestral, ya que has finalizado el tercer semestre.")

    # 2. Prerrequisito: 'Investigación cuantitativa' es prerrequisito de 'Métodos y análisis cuantitativos'
    if any(course["nombre"] == "Métodos y análisis cuantitativos" for course in selected_courses) and not any(course["nombre"] == "Investigación cuantitativa" for course in selected_courses):
        st.warning("Recuerda: 'Investigación cuantitativa' es prerrequisito para 'Métodos y análisis cuantitativos'.")

    # Mostrar reporte general de avance
    st.markdown("### Avance Académico")
    st.write(f"**Créditos totales cursados:** {total_credits}")
    st.write(f"**Según el currículo antiguo:** Has completado {old_semestre_actual} semestre(s) (cada semestre equivale a 16 créditos).")
    st.write(f"**Según el currículo nuevo:** Estarías en el semestre {new_semestre_actual} (se requieren 18 créditos por semestre).")
    if missing_credits > 0:
        st.write(f"Te faltan **{missing_credits}** crédito(s) para completar el semestre actual según el currículo nuevo.")
        # Verificamos si falta la electiva en el primer semestre (en el nuevo, la electiva de semestre 1 es de 1 crédito)
        electiva_convalidada = any(conv == "Electivas" for conv in [
            convalidaciones.get(course["nombre"]) for course in selected_courses if course["nombre"] in convalidaciones
        ])
        if new_semestre_actual == 1 and not electiva_convalidada:
            st.write("**Nota:** Te falta convalidar la electiva correspondiente al primer semestre.")

    # Verificar elegibilidad general
    if elegible:
        st.success("Elegible para Cambio de Currículo: Sí")
    else:
        st.error("Elegible para Cambio de Currículo: No")
        st.markdown("#### Razones:")
        for razon in razones_no_elegible:
            st.write(f"- {razon}")

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
    st.markdown("### Cursos convalidados en el currículo nuevo:")
    if convalidados:
        # Se agrupan los cursos convalidados por semestre en el currículo nuevo para facilitar la visualización.
        conv_by_sem = {}
        for curso in curriculum_nuevo:
            if curso["nombre"] in convalidados:
                conv_by_sem.setdefault(curso["semestre"], []).append(curso["nombre"])
        for sem, cursos in sorted(conv_by_sem.items()):
            st.write(f"**Semestre {sem}:** {', '.join(cursos)}")
    else:
        st.write("No se han identificado convalidaciones directas.")

    # -------------------------------
    # Cálculo de materias pendientes
    # -------------------------------
    pending_courses = [course for course in curriculum_nuevo if course["nombre"] not in convalidados]
    st.markdown("### Cursos pendientes por cursar en el currículo nuevo:")
    if pending_courses:
        # Agrupar por semestre para mostrar de forma clara
        pending_by_sem = {}
        for course in pending_courses:
            pending_by_sem.setdefault(course["semestre"], []).append(course)
        for sem in sorted(pending_by_sem.keys()):
            st.write(f"**Semestre {sem}:**")
            for course in pending_by_sem[sem]:
                st.write(f"- {course['nombre']} ({course['creditos']} créditos)")
    else:
        st.write("No hay cursos pendientes. ¡Felicidades!")

    # Créditos totales del currículo nuevo y créditos convalidados
    total_new_credits = sum(course["creditos"] for course in curriculum_nuevo)
    convalidados_credits = sum(course["creditos"] for course in curriculum_nuevo if course["nombre"] in convalidados)
    creditos_pendientes = total_new_credits - convalidados_credits

    st.write(f"**Créditos pendientes por completar en el currículo nuevo:** {creditos_pendientes}")

    # -------------------------------
    # Recomendaciones para el próximo semestre
    # -------------------------------
    st.markdown("### Recomendaciones para el próximo semestre")
    # Se priorizan las materias del semestre más bajo entre las pendientes
    if pending_courses:
        pending_sorted = sorted(pending_courses, key=lambda x: x["semestre"])
        recommended = []
        total_rec = 0
        for course in pending_sorted:
            if total_rec + course["creditos"] <= 18:
                recommended.append(course)
                total_rec += course["creditos"]
        st.write("Se recomienda inscribir las siguientes materias, priorizando las de menor semestre, para completar hasta 18 créditos:")
        for course in recommended:
            st.write(f"- {course['nombre']} (Semestre {course['semestre']}, {course['creditos']} créditos)")
        st.write(f"**Total de créditos recomendados:** {total_rec}")
    else:
        st.write("No hay recomendaciones; ya estás al día con el currículo nuevo.")

    # -------------------------------
    # Nota final y recomendaciones de asesoría
    # -------------------------------
    nota = "Si la información proporcionada no concuerda con tu situación o si consideras que hay datos que no puedes incluir en la app, busca asesoría personalizada."
    if doble_programa:
        nota += " Además, al ser estudiante de doble programa, asegúrate de recibir asesoría especializada, ya que aplican condiciones especiales."
    st.info(nota)
