
#1 Trabajo_aplicado- Sistema de AnÃ¡lisis de Rendimiento Estudiantil

## 2. Integrantes — Grupo 14

Ana Piuma, Catalina Bellomo, Matilda Ivancich, Delfina Ferrero, Allegra Gegenschatz

---

## 3. Objetivo

Muchos estudiantes no tienen forma de ver, de manera concreta, cómo sus hábitos del día a día afectan su rendimiento académico. Variables como las horas de sueño, la cantidad de horas dedicadas al estudio, el nivel de motivación o la asistencia a clases claramente influyen en los resultados, pero pocas herramientas lo muestran de forma accesible y personalizada.

Este sistema interactivo permite explorar datos reales de rendimiento estudiantil, visualizar patrones entre variables de hábitos y desempeño académico, detectar automáticamente perfiles de riesgo académico y generar reportes individualizados.

### División de tareas

Cada una se encargó de hacer el diagrama de la parte que le tocaba.

**Matilda** — Carga & Menú — scr/carga_datos.py + main.py

**Allegra** — Estadísticas — scr/estadisticas.py

**Anita** — Visualizaciones — scr/graficos_variables.py

**Delfi** — Riesgo Académico — scr/riesgo.py

**Cata** — Reporte Individual — scr/reporte_indivual.py + README.md + Streamlit

---

## 4. Descripción de fuente de datos

- **Dataset:** StudentPerformanceFactors.csv
- **Fuente:** Lainguyn123. (2024). Student Performance Factors. Kaggle.
- **Link:** https://www.kaggle.com/datasets/lainguyn123/student-performance-factors
- **Registros:** 6607 estudiantes

---

## 5. Instrucciones para ejecutar el programa

### Modo consola (main.py)

1. Clonar el repositorio
```
git clone https://github.com/tu-usuario/Trabajo_aplicado.git
```

2. Instalar las dependencias
```
pip install -r requirements.txt
```

3. Verificar que el dataset esté en la carpeta correcta.
   El archivo StudentPerformanceFactors.csv debe estar dentro de la carpeta datos/

4. Ejecutar el programa desde el main.py.
   Antes de correr el programa verificar que la ruta del dataset sea correcta para tu computadora.
```
python main.py
```

5. Usar el menú interactivo.
   Seguir las opciones que aparecen en consola e ingresar la información solicitada:

   - Opción 1 — Explorar el dataset → submenú con estadísticas, gráficos y reporte de riesgo
   - Opción 2 — Generar mi reporte individual → ingresás tus datos y recibís un reporte personalizado
   - Opción 3 — Salir

---

### Modo web (Streamlit)

1. Clonar el repositorio
```
git clone https://github.com/tu-usuario/Trabajo_aplicado.git
```

2. Entrar a la carpeta
```
cd Trabajo_aplicado
```

3. Instalar las dependencias
```
pip install -r requirements.txt
```

4. Correr la interfaz web
```
streamlit run app.py
```

5. Se abrirá automáticamente el navegador comenzá a explorar.

---

## 6. Librerías utilizadas

- **Pandas** — carga del dataset, validación, correlaciones, filtros de riesgo y cálculo de estadísticas
- **Matplotlib** — dashboard y gráficos del reporte individual
- **Os** — verificación de existencia de archivos y manejo de rutas
- **Sys** — control de rutas del sistema para importar módulos
- **Streamlit** — interfaz web interactiva (app.py)

---

## 7. Estructura del repositorio

```plaintext
Trabajo_aplicado/
├── datos/
│   └── StudentPerformanceFactors.csv
├── docs/
│   ├── Diagramas de graficos/
│   ├── Diagramas de reporte_individual/
│   ├── Diagramas de riesgo/
│   ├── Diagramas de carga_datos/
│   ├── Diagramas de estadisticas/
│   ├── Diagrama del programa.png
│   └── Diagrama del main.png
├── outputs/
├── scr/
│   ├── __init__.py
│   ├── carga_datos.py
│   ├── estadisticas.py
│   ├── graficos_variables.py
│   ├── riesgo.py
│   └── reporte_indivual.py
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 8. Explicación breve de las clases implementadas

No se implementan clases. El programa tiene un diseño de módulos, basado en una división de funciones donde cada archivo tiene las funciones necesarias para la realización de cada tarea. El archivo main.py actúa como orquestador: importa y llama a las funciones de cada módulo según la opción que elija el usuario en el menú.

---

## 9. Funciones principales

### Módulo carga_datos.py
- **cargar_dataset(ruta)** — lee el CSV y lo devuelve como DataFrame. Si no existe o falla, retorna None.
- **validar_archivo(df)** — verifica que el DataFrame tenga las columnas requeridas. Lanza ValueError si falta alguna.
- **mostrar_menu()** — muestra el menú principal con 3 opciones y retorna la opción elegida.
- **mostrar_submenu()** — muestra el submenú de exploración con 4 opciones y retorna la opción elegida.

### Módulo estadisticas.py
- **mostrar_estadisticas(df)** — calcula y muestra el promedio, máximo y mínimo de las variables numéricas.
- **calcular_correlaciones(df)** — calcula la correlación de Pearson entre hábitos y Exam_Score con interpretación.
- **formatear_tabla(datos)** — muestra un diccionario como tabla alineada en consola.

### Módulo graficos_variables.py
- **grafico_dispersion(df, variable)** — genera un scatter entre una variable y Exam_Score.
- **grafico_exam_score(df)** — genera un gráfico de barras con la distribución de Exam_Score.

### Módulo riesgo.py
- **evaluar_condicion(df, condicion)** — filtra el dataset por una condición individual de riesgo y retorna los estudiantes afectados.
- **detectar_riesgo(df)** — aplica las 5 condiciones fila por fila y agrega la columna perfil_riesgo al DataFrame.
- **mostrar_reporte_riesgo(df)** — muestra cantidad, porcentaje y detalle de estudiantes en riesgo.

### Módulo reporte_indivual.py
- **ingresar_datos_usuario()** — pide y valida 6 variables del usuario. Retorna un diccionario.
- **comparar_con_dataset(usuario, df)** — compara cada variable del usuario contra el promedio del dataset.
- **graficar_reporte_individual(usuario, df)** — genera 3 subplots comparativos del usuario vs el dataset.
- **evaluar_riesgo_usuario(usuario)** — evalúa 5 condiciones y retorna True si el usuario cumple al menos 2.

### main.py
- **main()** — punto de entrada del programa. Carga y valida el dataset, luego entra en un loop con el menú principal. Según la opción elegida ejecuta el módulo correspondiente.

---

## 10. Resultados y salidas generadas

### Salidas en consola
- Menú principal con 3 opciones: explorar el dataset, generar reporte individual y salir
- Submenú de exploración con 4 opciones: estadísticas, gráficos, reporte de riesgo y volver
- Submenú de gráficos con 5 opciones para elegir qué gráfico visualizar
- Estadísticas descriptivas: promedio, máximo y mínimo de cada variable numérica
- Correlaciones de Pearson entre hábitos académicos y Exam_Score con interpretación
- Reporte de riesgo: cantidad y porcentaje de estudiantes en riesgo y detalle por condición
- Reporte individual: comparación del usuario contra los promedios del dataset y clasificación de riesgo

### Gráficos generados
- Distribución de Exam_Score — histograma de barras con la frecuencia de cada puntaje
- Hours_Studied vs Exam_Score — dispersión entre horas de estudio y puntaje
- Sleep_Hours vs Exam_Score — dispersión entre horas de sueño y puntaje
- Attendance vs Exam_Score — dispersión entre asistencia y puntaje
- Reporte individual — 3 subplots: barras comparativas usuario vs dataset, scatter de estudio vs puntaje y scatter de sueño vs puntaje con el usuario destacado en rojo

### Métricas de riesgo académico

Los umbrales se calcularon usando el percentil 25 del dataset real (6607 registros):

- Exam_Score < 65
- Sleep_Hours < 6
- Hours_Studied < 16 horas semanales
- Attendance < 70%
- Motivation_Level == Low

Un estudiante se clasifica en perfil de riesgo si cumple al menos 2 de estas condiciones.

---

## 11. Diagramas de diseño

Los diagramas de flujo del programa y de cada módulo se encuentran en la carpeta docs/

---

## 12. Declaración de uso de IA

Este proyecto utilizó Inteligencia Artificial (Gemini y Claude) como herramienta de asistencia durante el desarrollo. El uso incluyó:

- Generación de código inicial para cada módulo a partir del documento de diseño
- Ayuda para resolver errores: cuando algo fallaba le preguntábamos cómo resolverlo
- Organización y división de tareas entre las integrantes
- Consultas sobre librerías y funciones que no conocíamos, por ejemplo cómo generar múltiples gráficos en un mismo subplot o cómo formatear tablas en consola
- Generación del dashboard en Streamlit (app.py)

En todos los casos el código generado fue revisado, probado y ajustado por las integrantes del grupo. La IA ayudó como asistente del código, pero las decisiones sobre cómo organizar el sistema, qué funciones hacer y cómo probarlo las tomamos nosotras.

Seguimos la estructura de documento de diseño → prompt → código. Antes de pedirle código a la IA, cada integrante preparó un documento de 
diseño con los siguientes componentes:

1. Objetivo del programa
2. Inputs
3. Outputs
4. Procesos principales
5. Estructuras de datos
6. Módulos / funciones
7. Errores posibles
8. Criterios de calidad
El documento de diseño se encuentra en la carpeta `/docs`.  
Los prompts utilizados por cada integrante están documentados en `/docs'

## 13. Notas adicionales

- El archivo CSV debe estar en la carpeta datos/ con el nombre exacto StudentPerformanceFactors.csv, sin cambiarle el nombre.

- La carpeta scr/ debe contener el archivo __init__.py (puede estar vacío) para que los imports entre módulos funcionen correctamente.

- Si usás Spyder, antes de correr main.py ejecutá esto en la consola para que encuentre los módulos:

```python
import os
os.chdir("/ruta/a/Trabajo_aplicado")
```

- Para el modo Streamlit, el programa debe correrse siempre desde la carpeta raíz Trabajo_aplicado/ y no desde dentro de scr/.

- Los gráficos generados se guardan automáticamente en la carpeta outputs/.
