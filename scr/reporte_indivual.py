#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:51:49 2026

@author: catalinabellomo
"""


import matplotlib.pyplot as plt

def ingresar_datos_usuario():
    """
    Le pide al usuario que ingrese sus propios datos de bienestar
    uno por uno, validando cada valor antes de continuar.

    Retorna:
        dict con las 6 variables del usuario listas para comparar
    """
# separadores visuales para que la consola se vea ordenada
    print("\n" + "=" * 50)
    print("   INGRESÁ TUS DATOS PERSONALES")
    print("=" * 50)
 # diccionario vacío donde se van a guardar los datos del usuario
    usuario = {}

    # --- Horas de estudio semanales ---
    while True:  # repite hasta que el usuario ingrese un valor válido
        try:
            valor = float(input("\n¿Cuántas horas por semana dedicás al estudio?(1-44) "))
            if 1 <= valor <= 44:   # rango del  dataset sobre horas de estudio 
                usuario["Hours_Studied"] = valor
                break # sale del while si el valor es válido
            else:
                print("  El valor debe estar entre 1 y 44 horas.")
        except ValueError: # atrapa el error si el usuario escribe texto en lugar de número
            print("  Ingresá un número válido.")

    # --- Horas de sueño por noche ---
    while True:
        try:
            valor = float(input("¿Cuántas horas dormís por noche en promedio? (4-10) "))
            if 4 <= valor <= 10: # rango del  dataset de esta variable 
                usuario["Sleep_Hours"] = valor
                break
            else:
                print("  El valor debe estar entre 4 y 10 horas.")
        except ValueError:
            print("  Ingresá un número válido.")

    # --- Asistencia ---
    while True:
        try:
            valor = float(input("¿Cuál es tu porcentaje de asistencia a clases? (0-100) "))
            if 0 <= valor <= 100:  # es un porcentaje, máximo 100
                usuario["Attendance"] = valor
                break
            else:
                print("  El porcentaje debe estar entre 0 y 100.")
        except ValueError:
            print("  Ingresá un número válido.")

    # --- Nivel de motivación ---
    while True:
        # strip() saca espacios, capitalize() convierte a "Low"/"Medium"/"High" sin importar cómo lo escribió
        valor = input("¿Cuál es tu nivel de motivación? (Low / Medium / High) ").strip().capitalize()
        if valor in ["Low", "Medium", "High"]:
            usuario["Motivation_Level"] = valor
            break
        else:
            print("  Ingresá exactamente: Low, Medium o High.")
 

    # --- Sesiones de tutoría ---
    while True:
        try:
            valor = int(input("¿Cuántas sesiones de tutoría tuviste este mes? (0-8) "))
            if 0 <= valor <= 8:#Rango del dataset 
                usuario["Tutoring_Sessions"] = valor
                break
            else:
                print("  El valor debe estar entre 0 y 8.")
        except ValueError:   # int() falla si el usuario escribe texto

            print("  Ingresá un número entero y dentro del rango (0-8).")

    # --- Puntaje del último examen ---
    while True:
        try:
            valor = float(input("¿Cuál fue tu puntaje en el último examen? (55-100) "))
            if 55 <= valor <= 100: # Rango de esta variable en el dataset 
                usuario["Exam_Score"] = valor
                break
            else:
                print("  El puntaje debe estar entre 55 y 100.")
        except ValueError:
            print("  Ingresá un número válido.")

    print("\nDatos registrados correctamente.")
    # devuelve el diccionario con los 6 datos listos para usar
    return usuario

def comparar_con_dataset(usuario, df):
    """
    Compara cada valor del usuario contra el promedio del dataset.

    Parámetros:
        usuario (dict): datos ingresados por el usuario
        df (DataFrame): dataset cargado

    Retorna:
        dict con el resultado de cada variable:
        {"variable": {"valor_usuario": x, "promedio": y, "estado": "arriba"/"abajo"}}
    """

     # lista de variables numéricas que se pueden comparar con promedios
    variables_numericas = ["Hours_Studied", "Sleep_Hours", "Attendance",
                           "Tutoring_Sessions", "Exam_Score"]
    # diccionario vacío donde se van a guardar los resultados
    comparaciones = {}
# recorre cada variable numérica
    for variable in variables_numericas:
        # verifica que la variable exista tanto en el usuario como en el dataset
        if variable in usuario and variable in df.columns:
            # calcula el promedio de esa variable en todo el dataset--
            promedio = round(df[variable].mean(), 2)
            # guarda el valor que ingresó el usuario
            valor_usuario = usuario[variable]
 # compara y guarda si está por encima o por debajo
            if valor_usuario >= promedio:
                estado = "arriba"
            else:
                estado = "abajo"
 # guarda los tres datos en el diccionario
            comparaciones[variable] = {
                "valor_usuario": valor_usuario,
                "promedio": promedio,
                "estado": estado
            }

    # Motivation_Level se compara de forma categórica (no numérica)
    if "Motivation_Level" in usuario:
        # asigna un número a cada nivel para poder comparar
        orden = {"Low": 1, "Medium": 2, "High": 3}
        valor_usuario = usuario["Motivation_Level"]
        # busca el valor más frecuente de motivación en el dataset
        moda = df["Motivation_Level"].mode()[0]
        # convierte los textos a números para comparar
        nivel_usuario = orden.get(valor_usuario, 0)
        nivel_moda = orden.get(moda, 0)

        if nivel_usuario >= nivel_moda:
            estado = "arriba"
        else:
            estado = "abajo"

        comparaciones["Motivation_Level"] = {
            "valor_usuario": valor_usuario,
            "promedio": moda,
            "estado": estado
        }

    return comparaciones

def graficar_reporte_individual(usuario, df):
    """
    Genera un reporte visual del usuario comparado con el dataset.
    Muestra 3 subplots:
      1. Barras: valor del usuario vs promedio del dataset
      2. Scatter: Hours_Studied vs Exam_Score con el usuario destacado
      3. Scatter: Sleep_Hours vs Exam_Score con el usuario destacado

    Parámetros:
        usuario (dict): datos ingresados por el usuario
        df (DataFrame): dataset cargado
    """

# llama a la función que calcula si el usuario está por encima o debajo del promedio
    comparaciones = comparar_con_dataset(usuario, df)

 # crea una figura con 3 gráficos en una sola fila, de 14x5 pulgadas
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    # título general de toda la figura
    fig.suptitle("Tu perfil vs el dataset")

    # Subplot 1: Barras usuario vs promedio
    # variables que se van a mostrar en el gráfico de barras
    variables = ["Hours_Studied", "Sleep_Hours", "Attendance", "Exam_Score"]
    # etiquetas en español para el eje x
    etiquetas = ["Hs. estudio", "Hs. sueño", "Asistencia", "Puntaje"]
 # saca los valores del usuario del diccionario comparaciones
    valores_usuario = [comparaciones[v]["valor_usuario"] for v in variables]
    # saca los promedios del dataset del diccionario comparaciones
    valores_promedio = [comparaciones[v]["promedio"] for v in variables]
# posiciones numéricas para las barras (0, 1, 2, 3)
    x = range(len(variables))
  # dibuja las barras grises del promedio del dataset
    axes[0].bar(x, valores_promedio, color="gray", label="Promedio dataset", width=0.4)
    # dibuja las barras azules del usuario, desplazadas 0.4 para que no se pisen
    axes[0].bar([i + 0.4 for i in x], valores_usuario, color="steelblue", label="Tus valores", width=0.4)
   # pone las etiquetas del eje x en el centro entre las dos barras
    axes[0].set_xticks([i + 0.2 for i in x])
    axes[0].set_xticklabels(etiquetas)
    # título y leyenda del primer gráfico
    axes[0].set_title("Tus valores vs promedio")
    axes[0].legend()

    # Subplot 2: Scatter horas de estudio vs puntaje 
    # dibuja todos los estudiantes del dataset como puntos grises
    axes[1].scatter(df["Hours_Studied"], df["Exam_Score"], color="gray", label="Dataset")
   # dibuja el punto del usuario en rojo más grande (s=100) encima de los demás
    axes[1].scatter(usuario["Hours_Studied"], usuario["Exam_Score"], color="red", s=100, label="Vos")
    # etiquetas de los ejes y título del segundo gráfico
    axes[1].set_xlabel("Horas de estudio")
    axes[1].set_ylabel("Puntaje del examen")
    axes[1].set_title("Estudio vs Puntaje")
    axes[1].legend()

    # Subplot 3: Scatter horas de sueño vs puntaje 
    # mismo scatter pero con horas de sueño en el eje x
    axes[2].scatter(df["Sleep_Hours"], df["Exam_Score"], color="gray", label="Dataset")
    axes[2].scatter(usuario["Sleep_Hours"], usuario["Exam_Score"], color="red", s=100, label="Vos")
   # etiquetas de los ejes y título del tercer gráfico
    axes[2].set_xlabel("Horas de sueño")
    axes[2].set_ylabel("Puntaje del examen")
    axes[2].set_title("Sueño vs Puntaje")
    axes[2].legend()
# ajusta automáticamente los espacios para que no se pisen los títulos
    plt.tight_layout()
# guarda el gráfico en la carpeta outputs
    plt.savefig("outputs/reporte_individual.png")
# muestra la ventana con los tres gráficos
    plt.show()

def evaluar_riesgo_usuario(usuario):
    """
    Evalúa si el usuario presenta un perfil de riesgo académico
    basándose en los umbrales del percentil 25 del dataset.

    Un estudiante se considera en riesgo si cumple al menos 2
    de las siguientes condiciones:
        - Exam_Score     < 65
        - Sleep_Hours    < 6
        - Hours_Studied  < 16
        - Attendance     < 70
        - Motivation_Level == "Low"

    Parámetros:
        usuario (dict): datos ingresados por el usuario

    Retorna:
        bool: True si tiene perfil de riesgo, False si no
    """

    # lista para guardar qué condiciones se cumplen
    condiciones_en_riesgo = []

    # chequea cada condición y guarda las que se cumplen
    if usuario.get("Exam_Score", 100) < 65:
        condiciones_en_riesgo.append("Puntaje del examen bajo (menos de 65)")

    if usuario.get("Sleep_Hours", 10) < 6:
        condiciones_en_riesgo.append("Pocas horas de sueño (menos de 6)")

    if usuario.get("Hours_Studied", 20) < 16:
        condiciones_en_riesgo.append("Pocas horas de estudio semanales (menos de 16)")

    if usuario.get("Attendance", 100) < 70:
        condiciones_en_riesgo.append("Baja asistencia (menos de 70%)")

    if usuario.get("Motivation_Level", "High") == "Low":
        condiciones_en_riesgo.append("Motivación baja")

    # muestra el resultado
    print("\n" + "=" * 50)
    print("   EVALUACIÓN DE PERFIL DE RIESGO")
    print("=" * 50)

    if len(condiciones_en_riesgo) >= 2:
        # tiene perfil de riesgo
        print("\nATENCIÓN: presentás un perfil de riesgo académico.")
        print("Se detectaron las siguientes señales:")
        for condicion in condiciones_en_riesgo:
            print(f"  - {condicion}")
        return True
    else:
        # no tiene perfil de riesgo
        print("\nTu perfil no presenta riesgo académico.")
        if condiciones_en_riesgo:
            print("Igual te recomendamos prestar atención a:")
            for condicion in condiciones_en_riesgo:
                print(f"  - {condicion}")
        return False
