import streamlit as st
import sqlite3
import datetime
import os
from supabase import create_client, Client

# ===============================
# Función para inicializar la base de datos
# ===============================
supabase: Client = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

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

# Mostrar logo de la universidad (asegúrate de tener "logo.png" en la carpeta)
st.image("logo.png", caption="Facultad de Psicología y Ciencias del Comportamiento", width=200)

st.title("App de Transición Curricular")
st.markdown(
    """
    **Bienvenido/a a la aplicación de apoyo para la transición curricular del programa de Psicología.**

    Esta herramienta te ayudará a determinar si eres elegible para realizar el cambio curricular, que implica pasar de un programa de 5 años (16 créditos por semestre) a uno de 4 años (18 créditos por semestre). Si has avanzado demasiado, puede que no cuentes con los créditos suficientes para hacer el cambio.

    Ten presente que en el nuevo plan se incorpora la **Micropráctica 1** en el tercer semestre, un componente fundamental que no existía anteriormente. Ingresa tus datos y materias cursadas para conocer tu situación y, de ser elegible, proceder con el cambio.
    """
)

st.header("Datos del Estudiante")
english_level = st.number_input("Nivel de Inglés (1-7)", min_value=1, max_value=7, value=1, step=1)
english_homologado = st.checkbox("¿Has homologado el inglés?")
semestre_actual = st.number_input("Semestre Actual (según tu avance)", min_value=1, value=1, step=1)
doble_programa = st.checkbox("¿Eres estudiante de doble programa?")

st.header("Materias cursadas (Currículo Antiguo)")
st.write("Selecciona las materias que has cursado, agrupadas por semestre:")

# Agrupar materias por semestre
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

# Opción para agregar un curso adicional "Otro"
st.subheader("Agregar curso adicional 'Otro'")
if st.checkbox("¿Desea agregar un curso adicional 'Otro'?"):
    otro_creditos = st.number_input("Indica la cantidad de créditos para el curso 'Otro'", min_value=1, value=1, step=1, key="otro_creditos")
    selected_courses.append({"nombre": "Otro", "semestre": 0, "creditos": otro_creditos, "prerrequisitos": []})

# ===============================
# Lógica de Cálculo y Reporte (Backend)
# ===============================
if st.button("Verificar Elegibilidad"):

    # Calcular créditos totales y determinar límite
    total_credits = sum(course["creditos"] for course in selected_courses)
    credit_limit = 64 if english_homologado or english_level >= 5 else 48

    # Verificar materias de semestres avanzados
    advanced_courses = [course for course in selected_courses if course["semestre"] >= 4]
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

    # Cálculo del avance (currículo antiguo: 16 créditos, nuevo: 18 créditos)
    old_semesters_completados = total_credits // 16
    old_semestre_actual = old_semesters_completados + (1 if total_credits % 16 != 0 else 0)
    new_semesters_completados = total_credits // 18
    new_semestre_actual = new_semesters_completados + (1 if total_credits % 18 != 0 else 0)
    missing_credits = ((new_semesters_completados + 1) * 18) - total_credits if total_credits < ((new_semesters_completados + 1) * 18) else 0

    if total_credits >= 48:
        st.warning("Recuerda: la 'Micropráctica 1' debe cursarse en el intersemestral, ya que has finalizado el tercer semestre.")
    if any(course["nombre"] == "Métodos y análisis cuantitativos" for course in selected_courses) and not any(course["nombre"] == "Investigación cuantitativa" for course in selected_courses):
        st.warning("Recuerda: 'Investigación cuantitativa' es prerrequisito para 'Métodos y análisis cuantitativos'.")

    st.markdown("### Avance Académico")
    st.write(f"**Créditos totales cursados:** {total_credits}")
    st.write(f"**Según el currículo antiguo:** Has completado {old_semestre_actual} semestre(s) (16 créditos por semestre).")
    st.write(f"**Según el currículo nuevo:** Estarías en el semestre {new_semestre_actual} (18 créditos por semestre).")
    if missing_credits > 0:
        st.write(f"Te faltan **{missing_credits}** crédito(s) para completar el semestre actual según el nuevo plan.")
        electiva_convalidada = any(conv == "Electivas" for conv in [
            convalidaciones.get(course["nombre"]) for course in selected_courses if course["nombre"] in convalidaciones
        ])
        if new_semestre_actual == 1 and not electiva_convalidada:
            st.write("**Nota:** Falta convalidar la electiva correspondiente al primer semestre.")

    if elegible:
        st.success("Elegible para el cambio curricular: Sí")
    else:
        st.error("Elegible para el cambio curricular: No")
        st.markdown("#### Razones:")
        for razon in razones_no_elegible:
            st.write(f"- {razon}")

    # Convalidaciones y cursos pendientes (lógica similar a tu versión original)
    convalidados = []
    for course in selected_courses:
        nombre = course["nombre"]
        if nombre in convalidaciones:
            mapped = convalidaciones[nombre]
            if mapped not in convalidados:
                convalidados.append(mapped)
    st.markdown("### Cursos convalidados en el currículo nuevo:")
    if convalidados:
        conv_by_sem = {}
        for curso in curriculum_nuevo:
            if curso["nombre"] in convalidados:
                conv_by_sem.setdefault(curso["semestre"], []).append(curso["nombre"])
        for sem, cursos in sorted(conv_by_sem.items()):
            st.write(f"**Semestre {sem}:** {', '.join(cursos)}")
    else:
        st.write("No se han identificado convalidaciones directas.")

    pending_courses = [course for course in curriculum_nuevo if course["nombre"] not in convalidados]
    st.markdown("### Cursos pendientes por cursar en el currículo nuevo:")
    if pending_courses:
        pending_by_sem = {}
        for course in pending_courses:
            pending_by_sem.setdefault(course["semestre"], []).append(course)
        for sem in sorted(pending_by_sem.keys()):
            st.write(f"**Semestre {sem}:**")
            for course in pending_by_sem[sem]:
                st.write(f"- {course['nombre']} ({course['creditos']} créditos)")
    else:
        st.write("No hay cursos pendientes. ¡Felicidades!")
        
    total_new_credits = sum(course["creditos"] for course in curriculum_nuevo)
    convalidados_credits = sum(course["creditos"] for course in curriculum_nuevo if course["nombre"] in convalidados)
    creditos_pendientes = total_new_credits - convalidados_credits
    st.write(f"**Créditos pendientes por completar en el currículo nuevo:** {creditos_pendientes}")

    st.markdown("### Recomendaciones para el próximo semestre")
    if pending_courses:
        pending_sorted = sorted(pending_courses, key=lambda x: x["semestre"])
        recommended = []
        total_rec = 0
        for course in pending_sorted:
            if total_rec + course["creditos"] <= 18:
                recommended.append(course)
                total_rec += course["creditos"]
        st.write("Se recomienda inscribir las siguientes materias, priorizando las de menor semestre, para alcanzar hasta 18 créditos:")
        for course in recommended:
            st.write(f"- {course['nombre']} (Semestre {course['semestre']}, {course['creditos']} créditos)")
        st.write(f"**Total de créditos recomendados:** {total_rec}")
    else:
        st.write("No hay recomendaciones; ya estás al día con el currículo nuevo.")

    nota = ("Si la información proporcionada no se ajusta a tu situación o consideras que falta algún dato, "
            "te recomendamos buscar asesoría personalizada.")
    if doble_programa:
        nota += " Además, al ser estudiante de doble programa, es importante que recibas asesoría especializada."
    st.info(nota)

    # --- Guardar la consulta en Supabase ---
    data = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "english_level": english_level,
        "english_homologado": english_homologado,
        "semestre_actual": semestre_actual,
        "doble_programa": doble_programa,
        "selected_courses": ", ".join(course["nombre"] for course in selected_courses),
        "total_credits": total_credits,
        "elegibilidad": "Elegible" if elegible else "No elegible"
    }
    response = supabase.table("queries").insert(data).execute()
    st.write("Consulta guardada en la base de datos:", response)

