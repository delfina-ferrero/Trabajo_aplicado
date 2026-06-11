#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:15:19 2026

@author: catalinabellomo
"""

from  reporte_indivual import ingresar_datos_usuario

usuario = ingresar_datos_usuario()
print(usuario)

from reporte_indivual import comparar_con_dataset
import pandas as pd

df = pd.read_csv("/Users/catalinabellomo/Documents/GitHub/Trabajo_aplicado/datos/StudentPerformanceFactors.csv")

comparaciones = comparar_con_dataset(usuario, df)

for variable, resultado in comparaciones.items():
    print(f"{variable}: vos = {resultado['valor_usuario']} | promedio = {resultado['promedio']} | {resultado['estado']}")
    
    
from reporte_indivual import graficar_reporte_individual

graficar_reporte_individual(usuario, df)


from  reporte_indivual import evaluar_riesgo_usuario

evaluar_riesgo_usuario(usuario)

