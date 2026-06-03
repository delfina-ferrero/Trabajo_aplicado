#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:51:49 2026

@author: catalinabellomo
"""
#Tenemos 4 fucniones:
 #ingresar_datos_usuario() ---> Le pregunta al usuario sus 6 datos uno por uno y los valida. Devuelve un diccionario con esos valores.
 #comparar_con_dataset(usuario, df) —->  recibe ese diccionario y el dataset. Calcula los promedios del dataset y compara cada valor del usuario contra esos promedios. Devuelve otro diccionario diciendo si cada variable está "arriba" o "abajo" del promedio.

import matplotlib.pyplot as plt




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

    comparaciones = comparar_con_dataset(usuario, df)

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.suptitle("Tu perfil vs el dataset")

    # --- Subplot 1: Barras usuario vs promedio ---
    variables = ["Hours_Studied", "Sleep_Hours", "Attendance", "Exam_Score"]
    etiquetas = ["Hs. estudio", "Hs. sueño", "Asistencia", "Puntaje"]

    valores_usuario = [comparaciones[v]["valor_usuario"] for v in variables]
    valores_promedio = [comparaciones[v]["promedio"] for v in variables]

    x = range(len(variables))
    axes[0].bar(x, valores_promedio, color="gray", label="Promedio dataset", width=0.4)
    axes[0].bar([i + 0.4 for i in x], valores_usuario, color="steelblue", label="Tus valores", width=0.4)
    axes[0].set_xticks([i + 0.2 for i in x])
    axes[0].set_xticklabels(etiquetas)
    axes[0].set_title("Tus valores vs promedio")
    axes[0].legend()

    # --- Subplot 2: Scatter horas de estudio vs puntaje ---
    axes[1].scatter(df["Hours_Studied"], df["Exam_Score"], color="gray", label="Dataset")
    axes[1].scatter(usuario["Hours_Studied"], usuario["Exam_Score"], color="red", s=100, label="Vos")
    axes[1].set_xlabel("Horas de estudio")
    axes[1].set_ylabel("Puntaje del examen")
    axes[1].set_title("Estudio vs Puntaje")
    axes[1].legend()

    # --- Subplot 3: Scatter horas de sueño vs puntaje ---
    axes[2].scatter(df["Sleep_Hours"], df["Exam_Score"], color="gray", label="Dataset")
    axes[2].scatter(usuario["Sleep_Hours"], usuario["Exam_Score"], color="red", s=100, label="Vos")
    axes[2].set_xlabel("Horas de sueño")
    axes[2].set_ylabel("Puntaje del examen")
    axes[2].set_title("Sueño vs Puntaje")
    axes[2].legend()

    plt.tight_layout()
    plt.show()


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

    # Variables numéricas que se pueden comparar
    variables_numericas = ["Hours_Studied", "Sleep_Hours", "Attendance",
                           "Tutoring_Sessions", "Exam_Score"]

    comparaciones = {}

    for variable in variables_numericas:
        if variable in usuario and variable in df.columns:
            promedio = round(df[variable].mean(), 2)
            valor_usuario = usuario[variable]

            if valor_usuario >= promedio:
                estado = "arriba"
            else:
                estado = "abajo"

            comparaciones[variable] = {
                "valor_usuario": valor_usuario,
                "promedio": promedio,
                "estado": estado
            }

    # Motivation_Level se compara de forma categórica (no numérica)
    if "Motivation_Level" in usuario:
        orden = {"Low": 1, "Medium": 2, "High": 3}
        valor_usuario = usuario["Motivation_Level"]
        moda = df["Motivation_Level"].mode()[0]
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


def ingresar_datos_usuario():
    """
    Le pide al usuario que ingrese sus propios datos de bienestar
    uno por uno, validando cada valor antes de continuar.

    Retorna:
        dict con las 6 variables del usuario listas para comparar
    """

    print("\n" + "=" * 50)
    print("   INGRESÁ TUS DATOS PERSONALES")
    print("=" * 50)

    usuario = {}

    # --- Horas de estudio semanales ---
    while True:
        try:
            valor = float(input("\n¿Cuántas horas por semana dedicás al estudio? "))
            if 0 <= valor <= 168:
                usuario["Hours_Studied"] = valor
                break
            else:
                print("  El valor debe estar entre 0 y 168 horas.")
        except ValueError:
            print("  Ingresá un número válido.")

    # --- Horas de sueño por noche ---
    while True:
        try:
            valor = float(input("¿Cuántas horas dormís por noche en promedio? "))
            if 0 <= valor <= 24:
                usuario["Sleep_Hours"] = valor
                break
            else:
                print("  El valor debe estar entre 0 y 24 horas.")
        except ValueError:
            print("  Ingresá un número válido.")

    # --- Asistencia ---
    while True:
        try:
            valor = float(input("¿Cuál es tu porcentaje de asistencia a clases? (0-100) "))
            if 0 <= valor <= 100:
                usuario["Attendance"] = valor
                break
            else:
                print("  El porcentaje debe estar entre 0 y 100.")
        except ValueError:
            print("  Ingresá un número válido.")

    # --- Nivel de motivación ---
    while True:
        valor = input("¿Cuál es tu nivel de motivación? (Low / Medium / High) ").strip().capitalize()
        if valor in ["Low", "Medium", "High"]:
            usuario["Motivation_Level"] = valor
            break
        else:
            print("  Ingresá exactamente: Low, Medium o High.")

    # --- Sesiones de tutoría ---
    while True:
        try:
            valor = int(input("¿Cuántas sesiones de tutoría tuviste este mes? (0-10) "))
            if 0 <= valor <= 10:
                usuario["Tutoring_Sessions"] = valor
                break
            else:
                print("  El valor debe estar entre 0 y 10.")
        except ValueError:
            print("  Ingresá un número entero.")

    # --- Puntaje del último examen ---
    while True:
        try:
            valor = float(input("¿Cuál fue tu puntaje en el último examen? (0-100) "))
            if 0 <= valor <= 100:
                usuario["Exam_Score"] = valor
                break
            else:
                print("  El puntaje debe estar entre 0 y 100.")
        except ValueError:
            print("  Ingresá un número válido.")

    print("\nDatos registrados correctamente.")
    return usuario


