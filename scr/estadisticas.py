#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:30:43 2026

@author: allegra
"""

def mostrar_estadisticas(df):
    """
    Calcula y muestra el promedio, máximo y mínimo de las
    variables numéricas del dataset en consola.

    Parámetros:
        df (DataFrame): el dataset cargado con Pandas.

    Retorna:
        No retorna ningún valor. Muestra los resultados
        directamente en consola.
    """
    if df is None or df.empty:
        print("\n[ERROR] No hay datos cargados. Por favor reiniciá el programa.")
        return

    columnas = ["Hours_Studied", "Sleep_Hours", "Attendance", "Tutoring_Sessions", "Exam_Score"]

    print("\n" + "=" * 55)
    print("     ESTADÍSTICAS DESCRIPTIVAS DEL DATASET")
    print("=" * 55)

    for col in columnas:
        promedio = df[col].mean()
        maximo   = df[col].max()
        minimo   = df[col].min()
        print(f"  {col:<22} prom: {promedio:>6.2f}   máx: {maximo:>3.0f}   mín: {minimo:>3.0f}")

    print("=" * 55)
    input("\nPresioná Enter para volver al menú principal...")

    
def calcular_correlaciones(df):
    """
    Calcula la correlación de Pearson entre Hours_Studied,
    Sleep_Hours y Attendance con Exam_Score. Muestra el
    coeficiente y una interpretación en texto por variable.

    Parámetros:
        df (DataFrame): el dataset cargado con Pandas.

    Retorna:
        No retorna ningún valor. Muestra los resultados
        directamente en consola.
    """
    if df is None or df.empty:
        print("\n[ERROR] No hay datos cargados. Por favor reiniciá el programa.")
        return

    variables = ["Hours_Studied", "Sleep_Hours", "Attendance"]

    print("\n" + "=" * 55)
    print("       CORRELACIONES CON EXAM_SCORE (Pearson)")
    print("=" * 55)

    for variable in variables:
        r = df[variable].corr(df["Exam_Score"])

        abs_r = abs(r)
        if abs_r >= 0.5:
            interpretacion = "alta positiva" if r > 0 else "alta negativa"
        elif abs_r >= 0.3:
            interpretacion = "media positiva" if r > 0 else "media negativa"
        else:
            interpretacion = "baja"

        print(f"  {variable:<22} r = {r:>5.2f}  →  {interpretacion}")

    print("=" * 55)
    input("\nPresioná Enter para volver al menú principal...")
    
def formatear_tabla(datos):
    """
    Muestra un diccionario en consola en formato de tabla
    ordenada con columnas alineadas y separadores visuales.

    Parámetros:
        datos (dict): diccionario con los valores a mostrar.
                      La clave es el nombre de la variable y
                      el valor es el texto con sus estadísticas.

    Retorna:
        No retorna ningún valor. Imprime directamente en consola.
    """
    print("-" * 55)
    for clave, valor in datos.items():
        print(f"  {clave:<22} {valor}")
    print("-" * 55)
    
    