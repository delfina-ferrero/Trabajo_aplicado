
# Trabajo_aplicado
# 1. Titulo: Student Performance Factors
# 2. Integrantes: Ana Piuma, Catalina Bellomo, Matilda Ivancich, Delfina Ferrero, Allegra Gegenschatz
# 3. Objetivo:
 Muchos estudiantes no tienen forma de ver, de manera concreta,cómo sus hábitos del día a día afectan su rendimiento académico. Variables como las horas de sueño, la cantidad de horas dedicadas al estudio, 
 el nivel de motivación o la asistencia a clases claramente influyen en los resultados, pero pocas herramientas lo muestran de forma accesible y personalizada.
 Este sistema interactivo permite explorar datos reales de rendimiento estudiantil, visualizar patrones entre variables de hábitos y desempeño académico, detectar automáticamente perfiles de riesgo académico y generar reportes individualizados.

#    Division de tareas => 
#    Allegra: Estadísticas & Análisis (estadisticas.py) Estadísticas descriptivas :Calcular y mostrar promedios, máximos y mínimos de todas las variables numéricas del dataset ; Correlaciones : Calcular correlaciones entre Hours_Studied, Sleep_Hours, Motivation y Exam_Score. Mostrar tabla interpretada con texto ; Formato de salida en consola:Que los resultados se muestren de forma clara, con separadores visuales y etiquetas legibles.
#    Ana : Visualizaciones (graficos.py) Dashboard con 8 gráficos: Armar el dashboard con Matplotlib subplots: scatter plots y barras ; Estética y coherencia visual: Que todos los gráficos tengan títulos, ejes etiquetados, colores consistentes y se vean bien juntos en el dashboard ; Histograma de Exam_Score : Distribución general del puntaje del examen como primer gráfico del dashboard.
#    Matilda: Coordinadora & Datos (carga_datos.py · main.py) Carga y validación del dataset: Leer el CSV con Pandas, verificar que el archivo existe y es válido, manejar el error si no se encuentra ; main.py y menú principal: Armar el main.py que llama a todos los módulos, el loop del menú principal y la lógica de navegación entre opciones ; Validación de entradas del usuario : Que el programa no se rompa con inputs inválidos.
#    Catalina:Reporte Individual & Docs (reporte_usuario.py | README) Reporte personal del usuario:Pedir los datos del usuario, comparar cada uno con el promedio del dataset y mostrar mensaje personalizado ; Diagnóstico de riesgo individual: Aplicar la lógica de riesgo al perfil del usuario y generar un mensaje por cada variable en zona crítica ; README y documentación: Redactar el README completo según la consigna.
#    Delfina: Riesgo Académico (riesgo.py) Detección de perfiles de riesgo : Aplicar las 5 condiciones de riesgo sobre el dataset completo y mostrar cuántos y qué porcentaje de estudiantes tiene perfil de riesgo; Filtro por condición: Permitir al usuario ver qué estudiantes fallan en cada condición específica; Reporte de riesgo en consola: Mostrar un resumen claro con cantidad de estudiantes en riesgo por cada variable, con mensaje interpretativo.
# 4. Descricpion de fuente de datos: La fuente de datos provee una descripcion general de diversos factores que afectan el rendimiento de estudiantes ante instancias de evaluacion. Incluye informacion de habitos de estudio, asistencias a clase, partiicpacion parental y otros aspectos que influencian el exito academico. 
# 5. Instrucciones para ejecutar el programa: Primero, clonar el repositorio ; Segundo: instalar las dependencias (requirements.txt) ; Tercero: verificar que el dataset este en la carpeta correcta (chequear que ese archivo CSV esté guardado donde el código espera encontrarlo); Cuarto : Ejecutar el programa (main.py) ; Quinto: Usar el menu interactivo al completar en consola la info solicitada.
# 6. Librerías utilizadas: Pandas (Carga del dataset, validacion, correlaciones, filtros de riesgo y calculo de estadisticas) ; Matplotlib (dashboard y graficos del reporte individual) ; Os (verificar que estistan los archivos) ; Sys (controla la salida del programa)










# 7. Estructura del repositorio: 
```
EDUTRACK/
--main.py --> menu principal
--carga_datos.py --> carga y validacion del csv
--estadisticas.py --> estadisticas descriptivas y correlaciones
--graficos.py --> graficos Matplotlib
--riesgo.py --> detecta perfiles con riesgo academico
--reporte_usuario.py --> reporte indicidual de cada usuario
--Datos:
    --StudentPerformanceFactors.CSV --> # [COMPLETAR: confirmar ruta/carpeta real del dataset]
--Diagramas:
    ---##DIAGRAMAS DE CADA FUNCION!!!!!!##
--requirements.txt --> librerias necesarias para que corra el codigo
--README.md --> este archivo

```
# 8. Explicación breve de las clases implementadas: no se implementan clases, nuestro programa tiene un diseno de "modulos", basado en una division de funciones y cada archivo tiene las funciones necesarias para la realizacion de cada tarea.
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

# 11. Diagramas de diseño. Los diagramas de flujo de cada función principal se encuentran en la carpeta `Diagramas/`, organizados por módulo:
#     -cargar_datos2.py: `cargar_dataset(ruta)`, `validar_archivo(df)`
#     -main.py : 'mostrar_menu()' , '_modulo_no_disponible(nombre)', '_pedir_opcion()', 'main()'
#     -reporte_individual.py : 'graficar_reporte_individual(usuario, df)', 'comparar_con_dataset(usuario, df)', 'ingresar_datos_usuario()'
#     -riesgo.py :'detectar_riesgo(df)', 'evaluar_condicion(df, condicion)', 'mostrar_reporte_riesgo(df)'
#     -pruebs_funciones.py : ACA QUEEEEEEE?????????????????????!!!!!!!!!


12. Declaración de uso de IA.
13. Notas o explicaciones adicionales para correr correctamente el programa.

