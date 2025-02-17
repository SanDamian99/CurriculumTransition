# App de Transición Curricular

Esta aplicación en Streamlit permite verificar la elegibilidad de estudiantes para la transición de un currículo antiguo a uno nuevo. Evalúa los cursos cursados, calcula créditos acumulados y genera recomendaciones de cursos pendientes para el próximo semestre, siguiendo criterios definidos (nivel de inglés, créditos acumulados, semestre actual, etc.).

## Características

- **Entrada de Datos del Estudiante:**  
  - Nivel de inglés (numérico y/o homologación).
  - Semestre actual.
  - Selección de materias cursadas del currículo antiguo.

- **Lógica de Cálculo:**  
  - Suma de créditos acumulados y verificación contra el límite (48 o 64 créditos según nivel de inglés).
  - Detección de materias cursadas en semestres avanzados.
  - Convalidación de cursos del currículo antiguo al nuevo.
  - Generación de reporte con créditos pendientes, lista de cursos a cursar y recomendaciones para el próximo semestre.

- **Asesoría Personalizada:**  
  - Mensaje de notificación para buscar asesoría en el proceso de transición curricular.

## Requisitos

- **Python 3.x**
- **Librerías:**  
  - `streamlit`
  - `pyngrok` (opcional, para exponer la app en Google Colab)

Consulta el archivo [requirements.txt](requirements.txt) para las versiones recomendadas.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
