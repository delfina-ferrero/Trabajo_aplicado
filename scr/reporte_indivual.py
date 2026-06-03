#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:51:49 2026

@author: catalinabellomo
"""

def ingresar_datos_usuario():
    """
    Le pide al usuario que ingrese sus propios datos de bienestar
    uno por uno, validando cada valor antes de continuar.
 
    Retorna:
        dict con las 6 variables del usuario listas para comparar
    """
    
    usuario = {}
    
    while True:
        try:
            #Horas de estudio semanales
            valor = float(input("\n¿Cuántas horas por semana dedicás al estudio? "))
            if 0 <= valor <= 168:
                usuario["Hours_Studied"] = valor
                break
            else:
                print("  El valor debe estar entre 0 y 168 horas.")
        except ValueError:
            print("  Ingresá un número válido.")
            
            
            #Horas de sueño por noche           
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
            
        
   # Asistencia 
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
 
   #Nivel de motivacion 
    while True:
        valor = input("¿Cuál es tu nivel de motivación? (Low / Medium / High) ").strip().capitalize()
        if valor in ["Low", "Medium", "High"]:
            usuario["Motivation_Level"] = valor
            break
        else:
            print("  Ingresá exactamente: Low, Medium o High.")
 
    #Sesiones de tutoria 
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
 
    # Puntaje en el ultimo examen 
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