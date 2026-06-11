#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:25:44 2026

@author: catalinabellomo
"""

from carga_datos import cargar_dataset, validar_archivo, mostrar_menu
from graficos_variables import mostrar_dashboard
from riesgo import mostrar_reporte_riesgo
from reporte_usuario import ingresar_datos_usuario, graficar_reporte_individual

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

       # if opcion == 1:
         #   mostrar_estadisticas(df)

        if opcion == 2:
            mostrar_dashboard(df)

        elif opcion == 3:
            mostrar_reporte_riesgo(df)

        elif opcion == 4:
            usuario = ingresar_datos_usuario()
            graficar_reporte_individual(usuario, df)

        elif opcion == 5:
            print("\nHasta luego!")
            break


if __name__ == "__main__":
    main()