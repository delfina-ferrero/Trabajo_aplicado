#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:58:45 2026

@author: Ana
"""

import matplotlib.pyplot as plt


def grafico_dispersion(df, variable):
    """
    Genera un gráfico de dispersión entre una variable
    y Exam_Score.

    Parámetros:
        df (DataFrame)
        variable (str)

    Retorna:
        None
    """

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df[variable],
        df["Exam_Score"]
    )

    plt.xlabel(variable)
    plt.ylabel("Exam_Score")
    plt.title(f"{variable} vs Exam_Score")

    plt.grid(True)
    plt.savefig(f"../outputs/dispersion_{variable}.png")
    plt.show()
    
def grafico_exam_score(df):
    """
    Genera un gráfico de barras con la frecuencia
    de los puntajes de examen.

    Parámetros:
        df (DataFrame)

    Retorna:
        None
    """

    frecuencias = (
        df["Exam_Score"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))

    plt.bar(
        frecuencias.index,
        frecuencias.values
    )

    plt.xlabel("Exam_Score")
    plt.ylabel("Cantidad de estudiantes")
    plt.title("Distribución de Exam_Score")

    plt.grid(axis="y")
    plt.savefig("../outputs/distribucion_exam_score.png")
    plt.show()
    
