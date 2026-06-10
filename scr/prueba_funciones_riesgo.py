# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:27:10 2026

@author: Delfina
"""

import pandas as pd
from riesgo import evaluar_condicion, detectar_riesgo, mostrar_reporte_riesgo

if __name__ == "__main__":
    # Definimos la ruta relativa exacta:
    # '..' sale de 'src' a 'trabajo_aplicado' y luego ingresa a 'datos'
    ruta_dataset = "../datos/StudentPerformanceFactors.csv"
    
    print("Iniciando el módulo de riesgo académico...")
    print(f"Buscando el dataset en la ruta relativa: '{ruta_dataset}'...\n")
    
    try:
        # Cargar el dataset utilizando la ruta relativa correcta para GitHub
        df_original = pd.read_csv(ruta_dataset)
        print("¡Dataset cargado con éxito desde la carpeta 'datos'!\n")
        
        # ---------------------------------------------------------------------
        # PRUEBA 1: Invocación de 'mostrar_reporte_riesgo(df)'
        # ---------------------------------------------------------------------
        print(" Ejecutando Función: mostrar_reporte_riesgo")
        mostrar_reporte_riesgo(df_original)
        print("\n" + "="*60 + "\n")
        
        # ---------------------------------------------------------------------
        # PRUEBA 2: Invocación de 'evaluar_condicion(df, condicion)'
        # ---------------------------------------------------------------------
        print(" Ejecutando Función: evaluar_condicion")
        condicion_a_probar = 'Attendance'
        df_solo_asistencia = evaluar_condicion(df_original, condicion_a_probar)
        
        print(f"Filtrando dataset por la condición: '{condicion_a_probar}'")
        print(f"Cantidad de estudiantes afectados de forma individual: {len(df_solo_asistencia)}")
        print("Mostrando los primeros 3 casos encontrados:")
        print(df_solo_asistencia[['Attendance', 'Hours_Studied', 'Exam_Score']].head(3))
        print("\n" + "="*60 + "\n")
        
        # ---------------------------------------------------------------------
        # PRUEBA 3: Invocación de 'detectar_riesgo(df)'
        # ---------------------------------------------------------------------
        print(" Ejecutando Función: detectar_riesgo")
        df_con_alertas = detectar_riesgo(df_original)
        
        print("¡Columna 'perfil_riesgo' agregada correctamente!")
        print("Verificación de la nueva columna en los primeros 5 registros del DataFrame:")
        columnas_verificacion = ['Exam_Score', 'Attendance', 'Sleep_Hours', 'perfil_riesgo']
        print(df_con_alertas[columnas_verificacion].head(5))
        
    except FileNotFoundError:
        print(f"❌ ERROR: No se pudo encontrar el archivo en '{ruta_dataset}'.")
        print("\nConsejo para que funcione en Spyder:")
        print("Asegurate de que el 'Working Directory' (Directorio de trabajo) en la esquina")
        print("superior derecha de Spyder sea la carpeta 'src' donde está tu archivo de código.")