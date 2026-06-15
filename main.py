#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:25:44 2026

@author: catalinabellomo
"""

from scr.carga_datos import cargar_dataset, validar_archivo, mostrar_menu, mostrar_submenu
from scr.estadisticas import mostrar_estadisticas, calcular_correlaciones
from scr.graficos_variables import grafico_dispersion, grafico_exam_score
from scr.riesgo import mostrar_reporte_riesgo
from scr.reporte_indivual import ingresar_datos_usuario, graficar_reporte_individual, evaluar_riesgo_usuario

RUTA_DATASET = "datos/StudentPerformanceFactors.csv"


def main():
    """
    Punto de entrada del programa.
    Carga el dataset, lo valida y ejecuta el menú principal en loop.
    """
    # 1. Cargar el dataset
    df = cargar_dataset(RUTA_DATASET)
    if df is None:
        print("No se pudo cargar el dataset. Cerrando el programa.")
        return

    # 2. Validar el archivo
    try:
        validar_archivo(df)
    except ValueError as e:
        print(f"Error de validación: {e}")
        print("Cerrando el programa.")
        return

    # 3. Loop del menú
    while True:
     opcion = mostrar_menu()

     if opcion == 1:
          # Submenú: explorar el dataset
          while True:
              subopcion = mostrar_submenu()

              if subopcion == 1:
                  mostrar_estadisticas(df)
                  calcular_correlaciones(df)

              elif subopcion == 2:
                  print("\n=============================================")
                  print("        VISUALIZACIÓN DE GRÁFICOS")
                  print("=============================================")
                  print("  1. Hours Studied vs Exam Score")
                  print("  2. Sleep Hours vs Exam Score")
                  print("  3. Attendance vs Exam Score")
                  print("  4. Distribución de Exam Score")
                  print("  5. Volver al menú principal")
                  print("=============================================")
                  grafico_a_ver = int(input("Elegi una opcion (1-5): "))
                  
                  if grafico_a_ver == 1:
                      grafico_dispersion(df, "Hours_Studied")
                      print("\n=============================================")
                      print("Grafico de comparacion de las horas estudiadas vs el puntaje obtenido en el examen.")
                      print("=============================================")
                  elif grafico_a_ver == 2:
                      grafico_dispersion(df, "Sleep_Hours")
                      print("\n=============================================")
                      print("Grafico comparacion de las horas de sueno vs puntaje obtenido en el examen.")
                      print("=============================================")
                  elif grafico_a_ver == 3:
                      grafico_dispersion(df, "Attendance")
                      print("\n=============================================")
                      print("Grafico comparacion de las asistencias vs puntaje obtenido en el examen.")
                      print("=============================================")
                  elif grafico_a_ver == 4:
                      grafico_exam_score(df)
                      print("\n=============================================")
                      print("Grafico de barras que muestra la distribucion de los puntajes obtenidos en el examen")
                      print("=============================================")
                  elif grafico_a_ver == 5:
                      break

              elif subopcion == 3:
                  mostrar_reporte_riesgo(df)

              elif subopcion == 4:
                  break  # vuelve al menú principal

     elif opcion == 2:
          usuario = ingresar_datos_usuario()
          graficar_reporte_individual(usuario, df)
          evaluar_riesgo_usuario(usuario)

     elif opcion == 3:
          print("\nHasta luego!")
          break


if __name__ == "__main__":
    main()