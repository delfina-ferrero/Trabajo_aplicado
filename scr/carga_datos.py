#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:28:31 2026

@author: catalinabellomo
"""
import os
import pandas as pd
 
 
def cargar_dataset(ruta):
    """
    Lee el archivo CSV del dataset y lo devuelve como DataFrame.
 
    Parámetros:
        ruta (str): ruta al archivo CSV
 
    Retorna:
        DataFrame con los datos, o None si hubo un error.
    """
    if not os.path.exists(ruta):
        print(f"Error: no se encontró el archivo '{ruta}'.")
        return None
 
    try:
        df = pd.read_csv(ruta)
        print(f"Dataset cargado correctamente ({len(df)} registros).")
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
 
 
def validar_archivo(df):
    """
    Verifica que el DataFrame tenga las columnas necesarias.
 
    Parámetros:
        df (DataFrame): dataset cargado con pandas
 
    Retorna:
        True si es válido. Lanza ValueError si falta alguna columna.
    """
    columnas_requeridas = [
        "Hours_Studied",
        "Sleep_Hours",
        "Attendance",
        "Motivation_Level",
        "Tutoring_Sessions",
        "Exam_Score"
    ]
 
    faltantes = []
    for col in columnas_requeridas:
        if col not in df.columns:
            faltantes.append(col)

    if faltantes:
        raise ValueError(f"El archivo no tiene las columnas requeridas: {faltantes}")

    print("Archivo validado correctamente.")
    return True
 
 
def mostrar_menu():
    """
    Muestra el menú principal y pide al usuario que elija una opción.
    Valida que la opción sea un número entre 1 y 3.
 
    Retorna:
        int entre 1 y 3 con la opción elegida.
    """
    print("\n" + "=" * 45)
    print("   SISTEMA DE ANÁLISIS DE RENDIMIENTO")
    print("=" * 45)
    print("  1. Explorar el dataset")
    print("  2. Generar mi reporte individual")
    print("  3. Salir")
    print("=" * 45)
 
    while True:
        try:
            opcion = int(input("Elegí una opción (1-3): "))
            if 1 <= opcion <= 3:
                return opcion
            else:
                print("Error: ingresá un número entre 1 y 3.")
        except ValueError:
            print("Error: eso no es un número válido.")
 
 
def mostrar_submenu():
    """
    Muestra el submenú de exploración del dataset.
    Valida que la opción sea un número entre 1 y 4.
 
    Retorna:
        int entre 1 y 4 con la opción elegida.
    """
    print("\n" + "-" * 45)
    print("   EXPLORAR EL DATASET")
    print("-" * 45)
    print("  1. Ver estadísticas descriptivas")
    print("  2. Ver dashboard de gráficos")
    print("  3. Ver reporte de riesgo académico")
    print("  4. Volver al menú principal")
    print("-" * 45)
 
    while True:
        try:
            opcion = int(input("Elegí una opción (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Error: ingresá un número entre 1 y 4.")
        except ValueError:
            print("Error: eso no es un número válido.")