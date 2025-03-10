import streamlit as st
import sqlite3
import datetime
import os
from supabase import create_client, Client

# ===============================
# Inicialización de Supabase
# ===============================
supabase: Client = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
FORMS_LINK = "https://forms.gle/ejemploAsesoria"

# ===============================
# Currículo Antiguo (de 1° a 10° semestre)
# ===============================
curriculum_antiguo = [
    # 1° semestre
    {"nombre": "Competencias Idiomáticas Básicas", "semestre": 1, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Inglés Nivel 2", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Introducción a la Investigación en Psicología", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Percepción, Atención y Memoria", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Psicobiología", "semestre": 1, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Historia y Fundamentos de la Psicología", "semestre": 1, "creditos": 2, "prerrequisitos": []},
    # 2° semestre
    {"nombre": "Core Curriculum Persona y Cultura I", "semestre": 2, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Inglés Nivel 3", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Competencias Básicas Digitales", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Pensamiento y Lenguaje", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Investigación Cuantitativa", "semestre": 2, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Neurociencias", "semestre": 2, "creditos": 3, "prerrequisitos": []},
    # 3° semestre
    {"nombre": "Core Curriculum Persona y Cultura II", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Inglés Nivel 4", "semestre": 3, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Electiva General I", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Psicología del Desarrollo", "semestre": 3, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Escuela Psicológica I", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Métodos y Análisis Cuantitativos", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Escuela Psicológica II", "semestre": 3, "creditos": 2, "prerrequisitos": []},
    # 4° semestre
    {"nombre": "Core Curriculum Persona y Cultura III", "semestre": 4, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Inglés Nivel 5", "semestre": 4, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Escuela Psicológica III", "semestre": 4, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Modelos de Aprendizaje", "semestre": 4, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Investigación Cualitativa", "semestre": 4, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Pensamiento Social Contemporáneo", "semestre": 4, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Electiva General II", "semestre": 4, "creditos": 2, "prerrequisitos": []},
    # 5° semestre
    {"nombre": "Core Curriculum Persona y Cultura IV", "semestre": 5, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Inglés Nivel 6", "semestre": 5, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Psicología Social (Laboratorio x1)", "semestre": 5, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Métodos y Análisis Cualitativos", "semestre": 5, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Electiva de Apoyo Disciplinar I", "semestre": 5, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Electiva de Apoyo Disciplinar II", "semestre": 5, "creditos": 3, "prerrequisitos": []},
    # 6° semestre
    {"nombre": "Core Curriculum Persona y Cultura V", "semestre": 6, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Inglés Nivel 7", "semestre": 6, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Psicometría (Laboratorio x1)", "semestre": 6, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Psicología Organizacional (Laboratorio x1)", "semestre": 6, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Psicopatología", "semestre": 6, "creditos": 4, "prerrequisitos": []},
    # 7° semestre
    {"nombre": "Proyecto en Psicología I", "semestre": 7, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Psicología Educativa", "semestre": 7, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Psicología Clínica", "semestre": 7, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Electiva de Apoyo Profesional I", "semestre": 7, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Evaluación e Intervención Optativa I", "semestre": 7, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Salud Pública", "semestre": 7, "creditos": 3, "prerrequisitos": []},
    # 8° semestre
    {"nombre": "Proyecto en Psicología II", "semestre": 8, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Práctica Formativa en Psicología Clínica y de la Salud", "semestre": 8, "creditos": 4, "prerrequisitos": []},
    {"nombre": "Ética Profesional", "semestre": 8, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Evaluación e Intervención Optativa II", "semestre": 8, "creditos": 3, "prerrequisitos": []},
    {"nombre": "Electiva de Apoyo Profesional II", "semestre": 8, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Campo Profesional Electivo", "semestre": 8, "creditos": 2, "prerrequisitos": []},
    {"nombre": "Competencias Profesionales", "semestre": 8, "creditos": 1, "prerrequisitos": []},
    # 9° semestre
    {"nombre": "Práctica en Psicología I", "semestre": 9, "creditos": 16, "prerrequisitos": []},
    # 10° semestre
    {"nombre": "Práctica en Psicología II", "semestre": 10, "creditos": 16, "prerrequisitos": []},
]

# ===============================
# Currículo Nuevo (Modificación a 4 años)
# ===============================
curriculum_nuevo = [
    # 1° semestre
    {"nombre": "Competencias idiomáticas básicas", "semestre": 1, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Ingles 2", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Introducción a la investigación", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Percepción y Atención", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Memoría y Aprendizaje", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Historia y fundamentos de la psicología", "semestre": 1, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Electivas", "semestre": 1, "creditos": 1, "prerrequisitos": [], "importancia": 3},
    # 2° semestre
    {"nombre": "Core, Curriculum persona y cultura 1", "semestre": 2, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Ingles 3", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Competencias básicas digitales", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Pensamiento y Lenguaje", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Investigación cuantitativa", "semestre": 2, "creditos": 2, "prerrequisitos": [], "importancia": 4},
    {"nombre": "Funciones Ejecutivas y Cognición Social", "semestre": 2, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Modelos de Aprendizaje", "semestre": 2, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    # 3° semestre
    {"nombre": "Core, Curriculum persona y cultura 2", "semestre": 3, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Inglés nivel 4", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Problemas sociales contemporáneos", "semestre": 3, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Psicología del desarrollo", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Micropractica 1", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 5},
    {"nombre": "Métodos y análisis cuantitativos", "semestre": 3, "creditos": 2, "prerrequisitos": ["Investigación cuantitativa", "Ingles nivel 4", "Core, Curriculum persona y cultura 2"], "importancia": 4},
    {"nombre": "Electivas", "semestre": 3, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    # 4° semestre
    {"nombre": "Ingles nivel 5", "semestre": 4, "creditos": 3, "prerrequisitos": ["Inglés nivel 4"], "importancia": 3},
    {"nombre": "Core, Curriculum persona y cultura 3", "semestre": 4, "creditos": 2, "prerrequisitos": ["Core, Curriculum persona y cultura 2"], "importancia": 4},
    {"nombre": "Ética profesional", "semestre": 4, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Investigación cualitativa", "semestre": 4, "creditos": 2, "prerrequisitos": [], "importancia": 4},
    {"nombre": "Psicopatología", "semestre": 4, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Medición y evaluación del comportamiento", "semestre": 4, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Electivas", "semestre": 4, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    # 5° semestre
    {"nombre": "Ingles nivel 6", "semestre": 5, "creditos": 3, "prerrequisitos": ["Ingles nivel 5"], "importancia": 3},
    {"nombre": "Core, Curriculum persona y cultura 4", "semestre": 5, "creditos": 2, "prerrequisitos": ["Core, Curriculum persona y cultura 3"], "importancia": 3},
    {"nombre": "Psicología social", "semestre": 5, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Métodos y análisis cualitativos", "semestre": 5, "creditos": 2, "prerrequisitos": ["Investigación cualitativa"], "importancia": 3},
    {"nombre": "Psicología clínica", "semestre": 5, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Micro práctica 2", "semestre": 5, "creditos": 3, "prerrequisitos": [], "importancia": 5},
    {"nombre": "Electivas", "semestre": 5, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    # 6° semestre
    {"nombre": "Ingles nivel 7", "semestre": 6, "creditos": 3, "prerrequisitos": ["Ingles nivel 6"], "importancia": 3},
    {"nombre": "Core, Curriculum persona y cultura 5", "semestre": 6, "creditos": 3, "prerrequisitos": ["Core, Curriculum persona y cultura 4"], "importancia": 3},
    {"nombre": "Psicología organizacional", "semestre": 6, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Psicología educativa", "semestre": 6, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Electivas", "semestre": 6, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Micro práctica 3", "semestre": 6, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    # 7° semestre
    {"nombre": "Competencias profesionales", "semestre": 7, "creditos": 1, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Psicología, Politica y Ciudadanía", "semestre": 7, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Campo profesional (optativo) 1", "semestre": 7, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Campo profesional (optativo) 2", "semestre": 7, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Práctica formativa en Psicología clínica y de la Salud", "semestre": 7, "creditos": 4, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Electivas", "semestre": 7, "creditos": 3, "prerrequisitos": [], "importancia": 3},
    {"nombre": "Proyecto en psicología", "semestre": 7, "creditos": 2, "prerrequisitos": [], "importancia": 3},
    # 8° semestre
    {"nombre": "Práctica en psicología", "semestre": 8, "creditos": 16, "prerrequisitos": [], "importancia": 3},
]

# ===============================
# Convalidaciones y mapeo
# ===============================
# Mapeo de materias con convalidación parcial o especial
convalidaciones = {
    # Convalidaciones particulares o con ajustes parciales:
    "Percepción, Atención y Memoria": "Percepción y Atención",  # Convalidación parcial
    "Psicobiología": "Memoria y Aprendizaje",  # Convalidación parcial
    "Historia y fundamentos de la psicología": "Historia y fundamentos de la psicología",  # (Ajuste de créditos: 2 → 3)
    
    # Convalidaciones directas (nombres idénticos o casi, ajustando mayúsculas/acento según el plan nuevo):
    "Ingles nivel 2": "Ingles nivel 2",
    "Ingles 2": "Inglés Nivel 2",
    "Competencias idiomáticas básicas": "Competencias idiomáticas básicas",
    "Introducción a la investigación": "Introducción a la investigación en psicología",
    "Introducción a la investigación en psicología": "Introducción a la investigación en psicología",
    "Core, Curriculum persona y cultura 1": "Core, Curriculum persona y cultura I",
    "Ingles nivel 3": "Ingles nivel 3",
    "Competencias básicas digitales": "Competencias básicas digitales",
    "Pensamiento y Lenguaje": "Pensamiento y Lenguaje",
    "Investigación cuantitativa": "Investigación cuantitativa",
    "Funciones Ejecutivas y Cognición Social": "Neurociencias",  # Según mapeo particular
    "Neurociencias": "Funciones Ejecutivas y Cognición Social",  # Mapeo recíproco según se requiera
    "Core, Curriculum persona y cultura II": "Core, Curriculum persona y cultura II",
    "Inglés nivel 4": "Inglés nivel 4",
    "Psicología del desarrollo": "Psicología del desarrollo",
    "Métodos y análisis cuantitativos": "Métodos y análisis cuantitativos",
    "Ingles nivel 5": "Inglés Nivel 5",
    "Core, Curriculum persona y cultura 3": "Core, Curriculum persona y cultura III",
    "Investigación cualitativa": "Investigación cualitativa",
    "Psicopatología": "Psicopatología",
    "Medición y evaluación del comportamiento": "Medición y evaluación del comportamiento",
    "Ingles nivel 6": "Inglés Nivel 6",
    "Core, Curriculum persona y cultura 4": "Core, Curriculum persona y cultura IV",
    "Métodos y análisis cualitativos": "Métodos y análisis cualitativos",
    "Psicología clínica": "Psicología Clínica",
    "Micro práctica 2": "Micro práctica 2",
    "Ingles nivel 7": "Inglés Nivel 7",
    "Core, Curriculum persona y cultura 5": "Core, Curriculum persona y cultura V",
    "Psicología organizacional": "Psicología Organizacional (laboratorio x1)",
    "Psicología educativa": "Psicología Educativa",
    "Micro práctica 3": "Micro práctica 3",
    "Competencias profesionales": "Competencias profesionales",
    "Práctica formativa en Psicología clínica y de la Salud": "Práctica formativa en Psicología Clínica y de la Salud",
    "Proyecto en psicología": "Proyecto en Psicología I",
    "Práctica en psicología": "Práctica en Psicología I",
    
    # Mapeos a Electivas:
    "Escuela Psicológica I": "Electivas",
    "Escuela Psicológica II": "Electivas",
    "Escuela Psicológica III": "Electivas",
    "Electiva de Apoyo Disciplinar I": "Electivas",
    "Electiva de Apoyo Disciplinar II": "Electivas",
    "Electiva de Apoyo Disciplinar III": "Electivas",
    "Electiva de Apoyo Profesional I": "Electivas",
    "Electiva de Apoyo Profesional II": "Electivas",
    "Electiva de Apoyo Profesional III": "Electivas",
    "Electiva General I": "Electivas",
    "Electiva General II": "Electivas",
    
    # Otras convalidaciones especiales:
    "Problemas sociales contemporaneos": "Pensamiento social contemporaneo",
    "Psicometría (Laboratorio x1)": "Medición y evaluación del comportamiento"
}


# ===============================
# Explicación inicial
# ===============================
st.image("logo.png", caption="Facultad de Psicología y Ciencias del Comportamiento", width=200)
st.title("App de Transición Curricular")
st.markdown(
    """
    ### Instrucciones y Consideraciones Importantes

    - **Microprácticas:**  
      Se deben cursar de forma individual; **no se pueden ver dos microprácticas en un mismo semestre**.  
      A mayor avance en el plan, la incorporación de microprácticas se vuelve más problemática para realizar el cambio curricular.
      Por ello, esta aplicación prioriza la asignatura de Micropractica en las recomendaciones, e incluso sugiere realizarla en intersemestral cuando corresponda.

    - La aplicación te ayudará a determinar si eres elegible para el cambio curricular, considerando que en el nuevo plan se requieren ciertos créditos mínimos y una correcta convalidación de asignaturas.
    
    - **Importante sobre el nivel de inglés:**  
      Se supone que debes tener como mínimo nivel 2 de inglés. Si indicas que tienes nivel 1, se te informará que adeudas 3 créditos de inglés.

    - Si necesitas asesoría personalizada, por favor solicita una cita [aquí]({forms_link}).

    """.replace("{forms_link}", FORMS_LINK)
)

# ===============================
# Entrada de datos del estudiante
# ===============================
# Solicitar el ID universitario para identificar al estudiante
university_id = st.text_input("Ingrese su ID universitario", "")

english_level = st.number_input("Nivel de Inglés (1-7)", min_value=1, max_value=7, value=1, step=1)
english_homologado = st.checkbox("He homologado inglés")
doble_programa = st.checkbox("¿Eres estudiante de doble programa?")

# Verificación del nivel de inglés mínimo
if english_level < 2:
    st.error("El nivel mínimo de inglés requerido es 2. Actualmente indicas nivel 1, por lo que debes cursar 3 créditos de inglés adicionales.")
    
# ===============================
# Selección de materias aprobadas/cursadas
# ===============================
st.header("Materias cursadas (Currículo Antiguo)")
st.markdown("**Seleccione las materias que ha APROBADO o está CURSANDO actualmente:**")

selected_courses = []
courses_by_semester = {}
for course in curriculum_antiguo:
    courses_by_semester.setdefault(course["semestre"], []).append(course)

for sem in sorted(courses_by_semester.keys()):
    st.subheader(f"Semestre {sem}")
    for course in courses_by_semester[sem]:
        key_course = f"{course['nombre']}_old"
        # Si es una asignatura de inglés y se homologó, se marca automáticamente y se deshabilita
        if english_homologado and "Inglés" in course["nombre"]:
            checked = st.checkbox(course["nombre"], key=key_course, value=True, disabled=True)
        else:
            checked = st.checkbox(course["nombre"], key=key_course)
        if checked and course not in selected_courses:
            selected_courses.append(course)

# Opción para agregar curso adicional "Otro"
st.subheader("Agregar curso adicional 'Otro'")
if st.checkbox("¿Desea agregar un curso adicional 'Otro'?"):
    otro_creditos = st.number_input("Indica la cantidad de créditos para el curso 'Otro'", min_value=1, value=1, step=1, key="otro_creditos")
    selected_courses.append({"nombre": "Otro", "semestre": 0, "creditos": otro_creditos, "prerrequisitos": []})

# ===============================
# Lógica de Cálculo, Convalidaciones y Recomendaciones
# ===============================
if st.button("Verificar Elegibilidad"):
    # Calcular créditos totales (garantizando que los créditos de inglés se cuenten una sola vez)
    total_credits = 0
    for course in selected_courses:
        # Ajuste especial: "Historia y Fundamentos de la Psicología" se cuentan como 3 créditos en lugar de 2
        if course["nombre"] == "Historia y Fundamentos de la Psicología":
            total_credits += 3
        else:
            total_credits += course["creditos"]

    # Determinar límite de créditos permitidos (48 o 64 según homologación o nivel de inglés)
    credit_limit = 64 if english_homologado or english_level >= 5 else 48

    # Verificar materias de semestres avanzados (más allá del 3° semestre del currículo antiguo)
    advanced_courses = [course for course in selected_courses if course["semestre"] >= 4]
    elegible = True
    razones_no_elegible = []

    if total_credits > credit_limit:
        elegible = False
        razones_no_elegible.append(
            f"Has superado el límite de créditos permitidos para la transición ({total_credits} créditos, límite {credit_limit})."
        )
    if advanced_courses:
        elegible = False
        nombres_advanced = ", ".join(course["nombre"] for course in advanced_courses)
        razones_no_elegible.append(
            f"Has cursado materias de semestres avanzados (4° o superior) del currículo antiguo: {nombres_advanced}."
        )

    # Cálculo del semestre en el plan nuevo (cada semestre equivale a 18 créditos)
    nuevo_semestre = 1 if total_credits < 15 else total_credits // 18 + (1 if total_credits % 18 != 0 else 0)
    
    # Recomendaciones:
    # Se prioriza la inscripción de la Micropractica. Si es pertinente (según el total de créditos),
    # se sugiere realizarla en intersemestral.
    recomendacion = ""
    if total_credits % 18 in range(15, 18):
        recomendacion += "Tienes créditos entre 15 y 17; se sugiere un intersemestral para completar los 18 créditos.\n"
    if total_credits in range(31, 36):
        recomendacion += "En segundo semestre, si tienes entre 31 y 35 créditos, se recomienda realizar un intersemestral para alcanzar 36 créditos.\n"
    if total_credits in range(48, 54):
        if english_level == 4:
            recomendacion += "Con nivel 4 de inglés y entre 48 y 53 créditos, ya cuentas con 6 créditos de inglés; INSCRIBE Micropractica 1.\n"
        else:
            recomendacion += "En tercer semestre, si tienes entre 48 y 53 créditos, se recomienda realizar intersemestral para alcanzar 54 créditos y pasar a cuarto semestre, e INSCRIBIR Micropractica 1.\n"
    if total_credits in range(37, 48):
        recomendacion += f"Tienes entre 37 y 47 créditos; te recomendamos buscar asesoría personalizada ya que aún tienes oportunidad, [solicita cita aquí]({FORMS_LINK}).\n"
    if total_credits in range(64, 72):
        recomendacion += f"Con 64 a 71 créditos, te recomendamos asesoría personalizada para definir la inscripción de Micropractica y continuar el plan nuevo, [solicita cita aquí]({FORMS_LINK}).\n"
    if total_credits >= 73:
        recomendacion += "Con más de 73 créditos, no es posible el cambio curricular, ya que correspondería al sexto semestre del plan nuevo (se requerirían dos Micropracticas).\n"
    
    # Priorizar la Micropractica: se revisa si entre las asignaturas pendientes del nuevo plan existe alguna Micropractica.
    # Si no se encuentra y el total de créditos sugiere avanzar, se añade esta recomendación al inicio.
    pending_micro = [course for course in curriculum_nuevo if "micropractica" in course["nombre"].lower() or "micro práctica" in course["nombre"].lower()]
    # Se supone que la lista de "convalidados" se genera posteriormente; aquí se verifica si en el nuevo plan ya se incluyó Micropractica.
    micro_in_convalidados = False  # Se actualizará más adelante según convalidaciones
    if not micro_in_convalidados and pending_micro:
        recomendacion = "Prioridad: INSCRIBE la asignatura de Micropractica. " + recomendacion

    if any(course["nombre"] == "Métodos y Análisis Cuantitativos" for course in selected_courses) and not any(course["nombre"] == "Investigación Cuantitativa" for course in selected_courses):
        st.warning("Recuerda: 'Investigación Cuantitativa' es prerrequisito para 'Métodos y Análisis Cuantitativos'.")

    st.markdown("### Avance Académico")
    st.write(f"**Créditos totales cursados (con ajuste en Historia y Fundamentos):** {total_credits}")
    st.write(f"**Según el plan nuevo:** Estarías en el semestre {nuevo_semestre} (18 créditos por semestre).")
    if total_credits % 18 > 0 and total_credits % 18 < 18:
        st.write(f"Te faltan **{18 - (total_credits % 18)}** crédito(s) para completar el semestre actual. {recomendacion}")
    else:
        st.write(recomendacion)

    if elegible:
        st.success("Elegible para el cambio curricular: Sí")
    else:
        st.error("Elegible para el cambio curricular: No")
        st.markdown("#### Razones:")
        for razon in razones_no_elegible:
            st.write(f"- {razon}")

    # Proceso de convalidación de asignaturas (se asume que "convalidaciones" y "curriculum_nuevo" están definidos externamente)
    convalidados = []
    for course in selected_courses:
        nombre = course["nombre"]
        if nombre in convalidaciones:
            mapped = convalidaciones[nombre]
            if mapped not in convalidados:
                convalidados.append(mapped)
        for nuevo in curriculum_nuevo:
            if nuevo["nombre"].lower() == nombre.lower() and nuevo["nombre"] not in convalidados:
                convalidados.append(nuevo["nombre"])

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

    # Recomendaciones para el próximo semestre: se priorizan las asignaturas de menor semestre y la Micropractica.
    st.markdown("### Recomendaciones para el próximo semestre")
    pending_micropracticas = [course for course in pending_courses if "micropractica" in course["nombre"].lower() or "micro práctica" in course["nombre"].lower()]
    pending_otros = [course for course in pending_courses if course not in pending_micropracticas]
    pending_sorted = sorted(pending_micropracticas, key=lambda x: x["semestre"]) + sorted(pending_otros, key=lambda x: x["semestre"])
    
    recommended = []
    total_rec = 0
    for course in pending_sorted:
        if total_rec + course["creditos"] <= 18:
            recommended.append(course)
            total_rec += course["creditos"]
    st.write("Se recomienda inscribir las siguientes materias para alcanzar hasta 18 créditos, **priorizando la Micropractica**:")
    for course in recommended:
        st.write(f"- {course['nombre']} (Semestre {course['semestre']}, {course['creditos']} créditos)")
    st.write(f"**Total de créditos recomendados:** {total_rec}")

    nota = (
        "Si la información proporcionada no se ajusta a tu situación o consideras que falta algún dato, "
        "te recomendamos buscar asesoría personalizada [solicitando cita aquí]({forms_link})."
    ).replace("{forms_link}", FORMS_LINK)
    if doble_programa:
        nota += " Además, al ser estudiante de doble programa, es importante que recibas asesoría especializada."
    st.info(nota)

    # --- Guardar la consulta en Supabase (se agrega un ID único) ---
    data = {
        "id": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        "university_id": university_id,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "english_level": english_level,
        "english_homologado": english_homologado,
        "doble_programa": doble_programa,
        "selected_courses": ", ".join(course["nombre"] for course in selected_courses),
        "total_credits": total_credits,
        "nuevo_semestre": nuevo_semestre,
        "elegibilidad": "Elegible" if elegible else "No elegible"
    }
    response = supabase.table("queries").insert(data).execute()
    st.write("Consulta guardada en la base de datos:", response)
