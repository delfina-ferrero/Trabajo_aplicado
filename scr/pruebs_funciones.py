#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:15:19 2026

@author: catalinabellomo
"""

from carga_datos import cargar_dataset
from reporte_usuario import ingresar_datos_usuario, comparar_con_dataset, graficar_reporte_individual

# 1. Cargar el dataset
df = cargar_dataset("datos/StudentPerformanceFactors.csv")

# 2. Simular un usuario con datos fijos (sin tener que escribirlos cada vez)
usuario_prueba = {
    "Hours_Studied": 10,
    "Sleep_Hours": 5,
    "Attendance": 70,
    "Motivation_Level": "Low",
    "Tutoring_Sessions": 1,
    "Exam_Score": 55
}

# 3. Probar comparar_con_dataset
comparaciones = comparar_con_dataset(usuario_prueba, df)
print(comparaciones)

# 4. Probar el gráfico
graficar_reporte_individual(usuario_prueba, df)