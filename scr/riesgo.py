# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:47:49 2026

@author: Delfina
"""

def detectar_riesgo(df):
    '''
    Deteccion de perfiles con riesgo: 
    aplica las 5 condiciones sobre el dataset completo y devuelve 
    un DataFrame con los estudiantes que cumplen con al menos una condicion, 
    ademas imprime cuantos estudiantes tienen riesgo y que porcentaje son.

    Parameters
    ----------
    df : pandas.DataFrame
        El DataFrame original que contiene los datos de todos los estudiantes.

    Returns
    -------
    df_riesgo: panas.DataFrame
        Un nuevo DataFrame filtrado que contiene unicamente las filas de 
        los estudiantes que presentan al menos un factor de riesgo detectado.

    '''
    
    c1 = df['Exam_Score'] < 60
    c2 = df['Sleep_Hours'] < 6
    c3 = df['Hours_Studied'] < 10
    c4 = df['Attendance'] < 75
    c5 = df['Motivation_Level'] = "Low"
    
    en_riesgo_mask = c1 | c2 | c3 | c4 | c5 #La barra | significa 'or'. Compara el cumplimiento de las 5 conidciones. Si al menos 1 cumple con la condicion, el resultado final es Verdadero.
    df_riesgo = df[en_riesgo_mask] #Conserva unicamente las filas que tenian True. Contiene los perfiles que deben ser observados por el equipo pedagogico desde cerca
    total_estudiantes = len(df) #Total de estudiantes en el dataset original
    cant_riesgo = len(df_riesgo) #Total de estudiantes que tienen riesgo
    porcentaje = (cant_riesgo / total_estudiantes) * 100 #Porcentaje de estudiantes con riesgo
    
    print("\n" + "="*40)
    print("DETECCION DE PERFILES DE RIESGO GLOBAL")
    print("="*40)
    print(f"Total de estudiantes analizados: {total_estudiantes}")
    print(f"Estudiantes con al menos un factor de riesgo: {cant_riesgo}")
    print(f"Porcentaje spbre el total: {porcentaje: .2f}%")
    print("="*40)
    
    return df_riesgo #Devuelve la tabla linda y prolija de los que tienen riesgo


#%%
def evaluar_condicion(df, condicion):
    '''
    Filtra el dataset de estudiantes segun un unico criterio de riesgo especifico.
    Permite aislar y analizar independientemente las subpoblaciones de estudiantes
    que se encuentran en situaciones criticas en base a una variable seleccionada
    por el usuario o el sistema interactivo. Limpia el texto de entrada para prevenir
    fallos por mayusculas o espacios extra
    
    Parameters
    ----------
    df : pandas: DataFrame
        El DataFrame original cargado desde el archivo CSV que contiene los datos
        de todos los estudiantes.
    condicion : str
        El nombre del factor de riesgo a evaluar. Opciones validas: 'rendimiento', 
        'sueño', 'estudio', 'asistencia', 'motivacion'.
        

    Returns
    -------
    df_filtrado: pandas: DataFrame
        Un DataFrame filtrado que contiene unicamente a los estudiantes que cumplen
        con la condicion elegida. Devuelve None si el texto ingresado en 'condicion'
        no coincide con ninguna opcion valida.

    '''
    condicion = condicion.lower().strip()
    
    #Aca la funcion va a usar condiciones para sabr que criterios aplicar:
    if condicion == "rendimiento":
        df_filtrado = df[df['Exam_Score'] < 60]
        mensaje = "Estudiantes con puntaje menor a 60 puntos"
    elif condicion == "sueño":
        df_filtrado = df[df['Sleep_Hours'] < 6]
        mensaje = "Estudiantes que duermes menos de 6 horas por noche"
    elif condicion == "estudio":
        df_filtrado = df[df['Hours_studied'] < 10]
        mensaje = "Estudiantes con menos de 10 horas semanales de estudio"
    elif condicion == "asistencia":
        df_filtrado = df[df['Attendance'] < 75]
        mensaje = "Estudiantes con asistencia menor al 75%"
    elif condicion == "motivacion" or condicion == "motivación":
        df_filtrado = df[df['Motivational_Level'] == "Low"]
    else:
        print("Condicion no valida")
        return None
    
    #Si la condicion fue valida y el filtro se aplico exitosamente, la funcion imprime los resultados
    print(f"\n Filtro Aplicado: {condicion.upper()}")
    print(f"{mensaje}")
    print(f"Cantidad encontrada: {len(df_filtrado)} estudiantes")
    
    return df_filtrado #DataFrame con los alumnos que sufren esa problematica en particular
    

#%%
def mostrar_reporte_riesgo(df):
    '''
    Genera y muestra en consola un reporte detallado del riesgo individual por variable.
    Calcula la cantidad exacta de estudiantes que se ven afectados por cada uno de los 5
    factores de riesgo de forma independiente. Ademas de imprimir los conteos, identifica
    de manera automatizada cual es la problematica mas critica en toda la poblacion y 
    concluye con una breve sugerencia o interpretacion pedagogica. 

    Parameters
    ----------
    df : pandas: DataFrame
        El DataFrame general de los estudiantes sobre el cual se contabilizaran las alertas individuales.

    Returns
    -------
    None.

    '''
    cant_rendimiento = len(df[df['Exam_Score'] < 60])
    cant_sueno = len(df[df['Sleep_Hours'] < 6])
    cant_estudio = len(df[df['Hours_Studied'] < 10])
    cant_asistencia = len(df[df['Attendance'] < 75])
    cant_motivacion = len(df[df['Motivational_Level'] == "Low"])
    
    print("\n" + " REPORTES DE RIESGO INDIVIDUAL POR VARIABLE ")
    print("-"*55)
    print(f"Bajo rendimiento (<60): {cant_rendimiento} alumnos.")
    print(f"Poco sueño (<6hs): {cant_sueno} alumnos.")
    print(f"Poco estudio (<10hs/sem): {cant_estudio} alumnos")
    print(f"Baja asistencia (<75%): {cant_asistencia} alumnos")
    print(f"Baja motivacion (Low): {cant_motivacion} alumnos")
    print("-"*55)
    
    print("\n CONTEXTO INTERPRETATIVO:")
    
    alertas = {
        "las notas insuficientes": cant_rendimiento,
        "La privacion del sueño": cant_sueno, 
        "Las pocas horas de estudio": cant_estudio,
        "El ausentismo a clase": cant_asistencia,
        "La desmotivacion general": cant_motivacion}
    
    peor_factor = max(alertas, key=alertas.get)
    
    print(f"El factor mas critico detectado en la poblacion estudiantil es {peor_factor}")
    print("Se sugiere al equipo de orientacion educativo priorizar intervenciones en este foco.")
    
    



































