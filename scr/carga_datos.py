#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:28:31 2026

@author: catalinabellomo
"""

import pandas as pd

def cargar_dataset(ruta):
    """
    Carga el dataset desde un archivo CSV. 

    Parámetros:
        ruta (str): ubicacion del archivo.

    Retorna:
        DataFrame: dataset cargado en pandas
    """
    try:
        datos = pd.read_csv(ruta)
        return datos

    except FileNotFoundError:
        print("No se encontró el archivo.")
        return None

    except Exception as error:
        print("Error:", error)
        return None
    
    