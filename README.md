
# Trabajo_aplicado- Sistema de AnÃ¡lisis de Rendimiento Estudiantil
# 2. Integrantes, grupo 14
 Ana Piuma, Catalina Bellomo, Matilda Ivancich, Delfina Ferrero, Allegra Gegenschatz
# 3. Objetivo:
 Muchos estudiantes no tienen forma de ver, de manera concreta,cÃ³mo sus hÃ¡bitos del dÃ­a a dÃ­a afectan su rendimiento acadÃ©mico. Variables como las horas de sueÃ±o, la cantidad de horas dedicadas al estudio, 
 el nivel de motivaciÃ³n o la asistencia a clases claramente influyen en los resultados, pero pocas herramientas lo muestran de forma accesible y personalizada.
 Este sistema interactivo permite explorar datos reales de rendimiento estudiantil, visualizar patrones entre variables de hÃ¡bitos y desempeÃ±o acadÃ©mico, detectar automÃ¡ticamente perfiles de riesgo acadÃ©mico y generar reportes individualizados.

#    Division de tareas 
Cada una se encargo de hacer el diagrama de la parte que le tocaba 
**Matilda** â Carga & MenÃº â scr/carga_datos.py + main.py

**Allegra** â EstadÃ­sticas â scr/estadisticas.py

**Anita** â Visualizaciones â scr/graficos_variables.py

**Delfi** â Riesgo AcadÃ©mico â scr/riesgo.py

**Cata** â Reporte Individual +s cr/reporte_indivual.py + README.md +streamlit

# 4. Descricpion de fuente de datos: 
Dataset: StudentPerformanceFactors.csv
Fuente: Lainguyn123. (2024). Student Performance Factors. Kaggle.
Link: https://www.kaggle.com/datasets/lainguyn123/student-performance-factors
Registros: 6607 estudiantes

# 5. Instrucciones para ejecutar el programa: 
#Modo consola (main.py)

1.Clonar el repositorio
git clone https://github.com/tu-usuario/Trabajo_aplicado.git


2.Instalar las dependencias
pip install -r requirements.txt


3.Verificar que el dataset estÃ© en la carpeta correcta
El archivo StudentPerformanceFactors.csv debe estar dentro de la carpeta datos/

4.Ejecutar el programa desde el main.py
Antes de correr el programa verificar que la ruta del dataset sea correcta para tu computadora:

5.Usar el menÃº interactivo
Seguir las opciones que aparecen en consola e ingresar la informaciÃ³n solicitada:

OpciÃ³n 1 â Explorar el dataset â submenÃº con estadÃ­sticas, grÃ¡ficos y reporte de riesgo
OpciÃ³n 2 â Generar mi reporte individual â ingresÃ¡s tus datos y recibÃ­s un reporte personalizado
OpciÃ³n 3 â Salir

##Modo web (Streamlit)
1.Clonar el repositorio
git clone https://github.com/tu-usuario/Trabajo_aplicado.git


2.Entrar a la carpeta
cd Trabajo_aplicado

3.Instalar las dependencias
pip install -r requirements.txt

4.Correr la interfaz web
streamlit run app.py

5.Se abrirÃ¡ automÃ¡ticamente el navegador 
ArrastrÃ¡ el archivo StudentPerformanceFactors.csv desde la carpeta datos/ al uploader de la interfaz y comenzÃ¡ a explorar.

# 6. LibrerÃ­as utilizadas:
- **Pandas** â carga del dataset, validaciÃ³n, correlaciones, 
  filtros de riesgo y cÃ¡lculo de estadÃ­sticas
- **Matplotlib** â dashboard y grÃ¡ficos del reporte individual
- **Os** â verificaciÃ³n de existencia de archivos y manejo de rutas
- **Sys** â control de rutas del sistema para importar mÃ³dulos
- **Streamlit** â interfaz web interactiva (app.py)

# 7. Estructura del repositorio: 

```
Trabajo_aplicado/
âââ datos/
â   âââ StudentPerformanceFactors.csv
âââ scr/
â   âââ __init__.py
â   âââ carga_datos.py
â   âââ estadisticas.py
â   âââ graficos_variables.py
â   âââ riesgo.py
â   âââ reporte_indivual.py
âââ docs/
â   âââ diseÃ±o.md
âââ outputs/
âââ app.py
âââ main.py
âââ requirements.txt
âââ prompts_dashboard.txt
âââ README.md
```

# 8. ExplicaciÃ³n breve de las clases implementadas: 
no se implementan clases, nuestro programa tiene un diseno de "modulos", basado en una division de funciones y cada archivo tiene las funciones necesarias para la realizacion de cada tarea.

# 9. Funciones principales
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
- **main()** — punto de entrada del programa. Carga y valida el dataset, 
  luego entra en un loop con el menú principal


# 10. - Resultados
### Salidas en consola
- Estadísticas descriptivas: promedio, máximo y mínimo de cada variable numérica
- Correlaciones de Pearson entre hábitos académicos y Exam_Score con interpretación
- Reporte de riesgo: cantidad y porcentaje de estudiantes en riesgo y detalle por condición
- Reporte individual: comparación del usuario contra los promedios del dataset y clasificación de riesgo

### Gráficos generados
- Distribución de Exam_Score — histograma de barras con la frecuencia de cada puntaje
- Hours_Studied vs Exam_Score — dispersión entre horas de estudio y puntaje
- Sleep_Hours vs Exam_Score — dispersión entre horas de sueño y puntaje
- Attendance vs Exam_Score — dispersión entre asistencia y puntaje
- Reporte individual — 3 subplots: barras comparativas usuario vs dataset, 
  scatter de estudio vs puntaje y scatter de sueño vs puntaje con el usuario destacado en rojo

### Métricas de riesgo académico
Los umbrales se calcularon usando el percentil 25 del dataset real (6607 registros):

- Exam_Score < 65
- Sleep_Hours < 6
- Hours_Studied < 16 horas semanales
- Attendance < 70%
- Motivation_Level == Low

Un estudiante se clasifica en perfil de riesgo si cumple al menos 2 de estas condiciones.

### Salidas en consola
- Menú principal con 3 opciones: explorar el dataset, generar reporte 
  individual y salir


# 11. Diagramas de diseÃ±o
Los diagramas de flujo del programa y de cada módulo se encuentran en la carpeta docs


##12. DeclaraciÃ³n de uso de IA.
Este proyecto utilizó Inteligencia Artificial Gemini y Chat como herramienta de asistencia durante el desarrollo,
 Generación de código inicial para cada módulo a partir del documento de diseño
- Si salia un error le pediamos que nos ayude o le preguntabamos como podemos resolverlo 
- Lo utilizamos para que nos divida la tarea y nos podemos organizar mejor 
-  Consultas sobre librerías y funciones que no conocíamos, por ejemplo 
  cómo generar múltiples gráficos en un mismo subplot, cómo formatear  tablas en consola
- Generación del dashboard en Streamlit (app.py) el codigo sobre el diseño de la interfaz
En todos los casos el código generado fue revisado, probado y ajustado 
por los integrantes del grupo. La IA ayudó como un asistente del ódigo, pero 
las decisiones sobre cómo organizar el sistema, qué funciones hacer y  cómo probarlo las tomamos nosotras.

## 13. Notas adicionales

- El archivo CSV debe estar en la carpeta datos/ con el nombre exacto 
  StudentPerformanceFactors.csv, sin cambiarle el nombre.

- La carpeta scr/ debe contener el archivo __init__.py (puede estar vacío) 
  para que los imports entre módulos funcionen correctamente.

- Si usás Spyder, antes de correr main.py ejecutá esto en la consola 
  para que encuentre los módulos:

  import os
  os.chdir("/ruta/a/Trabajo_aplicado")

- Para el modo Streamlit, el programa debe correrse siempre desde la 
  carpeta raíz Trabajo_aplicado/ y no desde dentro de scr/.

- Los gráficos generados se guardan automáticamente en la carpeta outputs/.

