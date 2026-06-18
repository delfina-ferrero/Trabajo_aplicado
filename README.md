
# Trabajo_aplicado- Sistema de Análisis de Rendimiento Estudiantil
# 2. Integrantes, grupo 14
 Ana Piuma, Catalina Bellomo, Matilda Ivancich, Delfina Ferrero, Allegra Gegenschatz
# 3. Objetivo:
 Muchos estudiantes no tienen forma de ver, de manera concreta,cómo sus hábitos del día a día afectan su rendimiento académico. Variables como las horas de sueño, la cantidad de horas dedicadas al estudio, 
 el nivel de motivación o la asistencia a clases claramente influyen en los resultados, pero pocas herramientas lo muestran de forma accesible y personalizada.
 Este sistema interactivo permite explorar datos reales de rendimiento estudiantil, visualizar patrones entre variables de hábitos y desempeño académico, detectar automáticamente perfiles de riesgo académico y generar reportes individualizados.

#    Division de tareas 
**Matilda** — Carga & Menú — scr/carga_datos.py + main.py

**Allegra** — Estadísticas — scr/estadisticas.py

**Anita** — Visualizaciones — scr/graficos_variables.py

**Delfi** — Riesgo Académico — scr/riesgo.py

**Cata** — Reporte Individual + Docs — scr/reporte_indivual.py + README.md

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


3.Verificar que el dataset esté en la carpeta correcta
El archivo StudentPerformanceFactors.csv debe estar dentro de la carpeta datos/

4.Ejecutar el programa desde el main.py

5.Usar el menú interactivo
Seguir las opciones que aparecen en consola e ingresar la información solicitada:

Opción 1 — Explorar el dataset → submenú con estadísticas, gráficos y reporte de riesgo
Opción 2 — Generar mi reporte individual → ingresás tus datos y recibís un reporte personalizado
Opción 3 — Salir

##Modo web (Streamlit)
1.Clonar el repositorio
git clone https://github.com/tu-usuario/Trabajo_aplicado.git


2.Entrar a la carpeta
cd Trabajo_aplicado

3.Instalar las dependencias
pip install -r requirements.txt

4.Correr la interfaz web
streamlit run app.py

5.Se abrirá automáticamente el navegador 
Arrastrá el archivo StudentPerformanceFactors.csv desde la carpeta datos/ al uploader de la interfaz y comenzá a explorar.

# 6. Librerías utilizadas:
- **Pandas** — carga del dataset, validación, correlaciones, 
  filtros de riesgo y cálculo de estadísticas
- **Matplotlib** — dashboard y gráficos del reporte individual
- **Os** — verificación de existencia de archivos y manejo de rutas
- **Sys** — control de rutas del sistema para importar módulos
- **Streamlit** — interfaz web interactiva (app.py)

# 7. Estructura del repositorio: 

```
Trabajo_aplicado/
├── datos/
│   └── StudentPerformanceFactors.csv
├── scr/
│   ├── __init__.py
│   ├── carga_datos.py
│   ├── estadisticas.py
│   ├── graficos_variables.py
│   ├── riesgo.py
│   └── reporte_indivual.py
├── docs/
│   └── diseño.md
├── outputs/
├── app.py
├── main.py
├── requirements.txt
├── prompts_dashboard.txt
└── README.md
```

# 8. Explicación breve de las clases implementadas: 
no se implementan clases, nuestro programa tiene un diseno de "modulos", basado en una division de funciones y cada archivo tiene las funciones necesarias para la realizacion de cada tarea.
# 9. Explicación breve de las funciones principales:
```
carga_datos.py 
    - cargar_dataset(ruta):recibe la ruta del CSV, verifica que el archivo exista y que tenga extensión `.csv`. Lo carga y maneja los errores posibles Retorna un `pd.DataFrame` o `None` si algo falla.
    - validar_archivo (df): verifica que el dataframe tenga la estructura esperada, que no esté vacio y  que estén todas las columnas necesarias, que no haya valoresnulos críticos, que `Exam_Score` esté en el rango [0, 100] y que las columnas numéricas tengan el tipo correcto. Retorna `True` o `False`.
main.py
    - mostrar_menu(): imprime el menú principal con las 6 opciones (0 a 5).
    - _modulo_no_disponible(nombre): función auxiliar que avisa en consola si un módulo de alguna compañera todavía no fue integrado.
    - _pedir_opcion(): pide al usuario un número del menú y valida que sea un entero, manejando el error con try / except. 
    - main() :punto de entrada del programa. Pide la ruta del dataset, lo carga y valida, y ejecuta el loop del menú que despacha a cada módulo según la opción elegida.
reporte_individual.py
    - graficar_reporte_individual(usuario, df): usa los datos ingresados por el usuario, Genera un reporte visual del usuario comparado con el dataset. Muestra 3 subplots: Barras: valor del usuario vs promedio del dataset ; Scatter: Hours_Studied vs Exam_Score con el usuario destacado y Scatter: Sleep_Hours vs Exam_Score con el usuario destacado
    - comparar_con_dataset(usuario, df): Compara cada valor del usuario contra el promedio del dataset.
    - ingresar_datos_usuario(): Le pide al usuario que ingrese sus propios datos de bienestar uno por uno, validando cada valor antes de continuar.
riesgo.py
    - detectar_riesgo(df): aplica las 5 condiciones sobre el dataset completo y devuelve un DataFrame con los estudiantes que cumplen con al menos una condicion, ademas imprime cuantos estudiantes tienen riesgo y que porcentaje son.
    - evaluar_condicion(df, condicion):recibe el dataset y un texto con una condición de riesgo . Filtra el dataset según esa condición, imprime un mensaje descriptivo y la cantidad de estudiantes encontrados, y retorna el DataFrame filtrado o None si la condición no es válida.
    - mostrar_reporte_riesgo(df): cuenta cuántos estudiantes cumplen cada una de las 5 condiciones de riesgo por separado (rendimiento, sueño, estudio, asistencia y motivación), muestra esos resultados en consola y determina cuál es el factor más crítico (el que afecta a más estudiantes), sugiriendo priorizarlo en futuras intervenciones.

GRAFICO Y RIESGOS?!?!?!?!

```
# 10. - Resultados
#       - Salidas : Estadísticas descriptivas por variable numérica ; Tabla de correlaciones de Pearson con interpretación ; Reporte de riesgo académico grupal: cantidad y porcentaje de estudiantes en riesgo, detalle por condición y mensaje interpretativo. ; Reporte individual: comparación del usuario contra los promedios del dataset y resultado de su evaluación de riesgo personal.
FALTAAAA
#       - Métricas 
#       - Gráficos o funcionalidades generadas




CORROBORAR QUE ESTEN ESTOS DIAGRAMAS SEPARADOS ASI 

# 11. Diagramas de diseño. Los diagramas de flujo de cada función principal se encuentran en la carpeta `Diagramas/`, organizados por módulo: en los siguientes archivos:
#     -cargar_datos.py: `cargar_dataset(ruta)`, `validar_archivo(df)` #poner el formato del archivo, .png...
#     -main.py : 'mostrar_menu()' , '_modulo_no_disponible(nombre)', '_pedir_opcion()', 'main()'
#     -reporte_individual.py : 'graficar_reporte_individual(usuario, df)', 'comparar_con_dataset(usuario, df)', 'ingresar_datos_usuario()'
#     -riesgo.py :'detectar_riesgo(df)', 'evaluar_condicion(df, condicion)', 'mostrar_reporte_riesgo(df)'
#     -pruebs_funciones.py : ACA QUEEEEEEE?????????????????????!!!!!!!!!


12. Declaración de uso de IA.
13. Notas o explicaciones adicionales para correr correctamente el programa.

