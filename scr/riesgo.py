# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:47:49 2026

@author: Delfina
"""

import pandas as pd

def evaluar_condicion(df, condicion):
    """
    Filtra el dataset y devuelve solo los estudiantes que cumplen una condición 
    específica de riesgo (individualmente).
    
    Parámetros:
    - df (DataFrame): El dataset cargado con Pandas.
    - condicion (str): Nombre de la condición a evaluar.
    
    Retorna:
    - DataFrame: Subconjunto filtrado con los estudiantes en riesgo por esa variable.
    """
    # Diccionario interno que mapea cada condición con su respectivo filtro (Umbrales del percentil 25)
    filtros = {
        'Exam_Score': df['Exam_Score'] < 65,
        'Sleep_Hours': df['Sleep_Hours'] < 6,
        'Hours_Studied': df['Hours_Studied'] < 16,
        'Attendance': df['Attendance'] < 70,
        'Motivation_Level': df['Motivation_Level'].str.strip() == 'Low'
    }
    
    if condicion in filtros:
        return df[filtros[condicion]]
    else:
        print(f"Error: La condición '{condicion}' no es reconocida.")
        return pd.DataFrame() # Devuelve un DataFrame vacío si no es válida


def detectar_riesgo(df):
    """
    Recorre todos los registros del dataset y clasifica a cada estudiante.
    Agrega una nueva columna al DataFrame llamada 'perfil_riesgo'.
    
    Parámetros:
    - df (DataFrame): El dataset original cargado con Pandas.
    
    Retorna:
    - DataFrame: El mismo DataFrame con la columna 'perfil_riesgo' (True/False).
    """
    # Creamos una copia para evitar advertencias de asignación (SettingWithCopyWarning)
    df_resultado = df.copy()
    
    # Calculamos series booleanas para cada una de las 5 condiciones de riesgo
    c1 = df_resultado['Exam_Score'] < 65
    c2 = df_resultado['Sleep_Hours'] < 6
    c3 = df_resultado['Hours_Studied'] < 16
    c4 = df_resultado['Attendance'] < 70
    c5 = df_resultado['Motivation_Level'].str.strip() == 'Low'
    
    # Sumamos las condiciones (True se cuenta como 1, False como 0) fila por fila de manera eficiente
    cantidad_condiciones = c1.astype(int) + c2.astype(int) + c3.astype(int) + c4.astype(int) + c5.astype(int)
    
    # Un estudiante entra en riesgo si cumple al menos 2 de estas condiciones
    df_resultado['perfil_riesgo'] = cantidad_condiciones >= 2
    
    return df_resultado


def mostrar_reporte_riesgo(df):
    """
    Muestra en consola un resumen estadístico completo de la situación de riesgo
    en todo el dataset e interpreta cada condición individual.
    
    Parámetros:
    - df (DataFrame): El dataset cargado con Pandas.
    """
    print("=" * 60)
    print("       REPORTE GENERAL DE DETECCIÓN DE RIESGO ACADÉMICO       ")
    print("=" * 60)
    
    # 1. Ejecutar la detección general
    df_con_riesgo = detectar_riesgo(df)
    
    total_estudiantes = len(df_con_riesgo)
    estudiantes_en_riesgo = df_con_riesgo['perfil_riesgo'].sum()
    porcentaje_riesgo = (estudiantes_en_riesgo / total_estudiantes) * 100
    
    print(f"Total de estudiantes analizados: {total_estudiantes}")
    print(f"Estudiantes en perfil de riesgo: {estudiantes_en_riesgo}")
    print(f"Porcentaje en riesgo académico:  {porcentaje_riesgo:.2f}%")
    print("-" * 60)
    print("Análisis detallado por indicador de riesgo individual:")
    print("-" * 60)
    
    # 2. Evaluar y contar cada condición de forma individual usando evaluar_condicion()
    indicadores = [
        ('Exam_Score', "Puntaje de examen bajo (< 65 pts)"),
        ('Sleep_Hours', "Horas de sueño insuficientes (< 6 hs)"),
        ('Hours_Studied', "Pocas horas de estudio semanales (< 16 hs)"),
        ('Attendance', "Asistencia escolar insuficiente (< 70%)"),
        ('Motivation_Level', "Nivel de motivación bajo (== 'Low')")
    ]
    
    for cond, descripcion in indicadores:
        df_filtrado = evaluar_condicion(df, cond)
        cantidad_afectados = len(df_filtrado)
        porcentaje_afectados = (cantidad_afectados / total_estudiantes) * 100
        print(f"• {descripcion}:")
        print(f"  Cantidad: {cantidad_afectados} estudiantes | Proporción: {porcentaje_afectados:.2f}%")
    
    print("=" * 60)
    print("Nota: Los estudiantes en perfil de riesgo acumulan al menos 2")
    print("de los indicadores detallados arriba simultáneamente.")
    print("=" * 60)
    


    
    



































