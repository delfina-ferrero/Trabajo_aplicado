# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:27:10 2026

@author: Delfina
"""

import os
import pandas as pd

# 1. Importamos las funciones de tu módulo 'riesgo.py'
try:
    from scr import riesgo
    print("¡Módulo 'riesgo.py' importado correctamente!")
except ImportError:
    print("Error: No se encontró el archivo 'riesgo.py' en el mismo directorio.")

# 2. Definimos la ruta del dataset (respetando la estructura de carpetas acordada)
ruta_dataset = os.path.join("datos", "StudentPerformanceFactors.csv")

# 3. Lógica de carga y validación básica
if not os.path.exists(ruta_dataset):
    print(f"Error: No se encontró el archivo en la ruta especificada: '{ruta_dataset}'")
    print("Por favor, verifica que la carpeta 'datos' exista y contenga el archivo CSV.")
else:
    print(f"Cargando el dataset desde: '{ruta_dataset}'...")
    
    # Cargamos el DataFrame con Pandas
    df = pd.read_csv(ruta_dataset)
    print(f"Dataset cargado con éxito. Cantidad de registros: {len(df)}")
    
    print("\n" + "="*60)
    print(" EJECUTANDO INVOCACIÓN DE TUS FUNCIONES DEL MÓDULO RIESGO")
    print("="*60 + "\n")
    
    # --- PRUEBA 1: mostrar_reporte_riesgo(df) ---
    # Esta función ya llama internamente a detectar_riesgo() y evaluar_condicion()
    # mostrando todo el procesamiento por consola de forma limpia.
    riesgo.mostrar_reporte_riesgo(df)
    
    
    # --- PRUEBA 2: Uso manual de detectar_riesgo(df) ---
    # Si quisieras capturar el DataFrame modificado para usarlo en otro módulo:
    df_procesado = riesgo.detectar_riesgo(df)
    
    # Mostramos una vista previa de estudiantes clasificados en riesgo para verificar
    print("\nVista previa de estudiantes en situación de riesgo detectados:")
    estudiantes_riesgo_ejemplo = df_procesado[df_procesado['perfil_riesgo'] == True].head(3)
    
    # Seleccionamos las columnas clave para que la previsualización en la consola sea legible
    columnas_clave = ['Hours_Studied', 'Sleep_Hours', 'Attendance', 'Motivation_Level', 'Exam_Score', 'perfil_riesgo']
    print(estudiantes_riesgo_ejemplo[columnas_clave])
    
    print("\nPrueba finalizada con éxito. ¡Todo listo para integrar en el main.py!")
    
