#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:45:23 2026

@author: catalinabellomo
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scr"))

from carga_datos import validar_archivo
from estadisticas import calcular_correlaciones
from graficos_variables import grafico_dispersion, grafico_exam_score
from riesgo import detectar_riesgo, evaluar_condicion
from reporte_indivual import comparar_con_dataset, graficar_reporte_individual, evaluar_riesgo_usuario

# ── Configuración de la página ──────────────────────────────────────────────
st.set_page_config(
    page_title="Análisis de Rendimiento Estudiantil",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Sistema de Análisis de Rendimiento Estudiantil")
st.markdown("Grupo 14 — Matilda Ivancich · Allegra Gegenschatz · Ana Piuma · Delfina Ferrero · Catalina Bellomo")
st.divider()

# ── 1. CARGA DEL ARCHIVO ─────────────────────────────────────────────────────
# ── 1. CARGA DEL ARCHIVO ─────────────────────────────────────────────────────
RUTA_DATASET = "datos/StudentPerformanceFactors.csv"  # ← ajustá la ruta a donde está tu CSV

try:
    df = pd.read_csv(RUTA_DATASET)
    validar_archivo(df)
    st.success(f"Dataset cargado correctamente — {len(df)} registros.")
except ValueError as e:
    st.error(f"Error de validación: {e}")
    st.stop()
except FileNotFoundError:
    st.error(f"No se encontró el archivo en: {RUTA_DATASET}")
    st.stop()
except Exception as e:
    st.error(f"No se pudo leer el archivo: {e}")
    st.stop()

# ── 2. VALIDACIÓN DEFENSIVA ──────────────────────────────────────────────────
try:
    df = pd.read_csv(RUTA_DATASET)
    validar_archivo(df)
    st.success(f"Archivo cargado y validado correctamente — {len(df)} registros.")
except ValueError as e:
    st.error(f"Error de validación: {e}")
    st.stop()
except FileNotFoundError:
    st.error(f"No se encontró el archivo en: {RUTA_DATASET}")
    st.stop()
except Exception as e:
    st.error(f"No se pudo leer el archivo: {e}")
    st.stop()

st.divider()
# ── 3. KPIs ──────────────────────────────────────────────────────────────────
st.header("2. Indicadores clave")

df_riesgo = detectar_riesgo(df)
total = len(df)
promedio_score = round(df["Exam_Score"].mean(), 2)
promedio_estudio = round(df["Hours_Studied"].mean(), 2)
promedio_sueno = round(df["Sleep_Hours"].mean(), 2)
en_riesgo = int(df_riesgo["perfil_riesgo"].sum())
porcentaje_riesgo = round((en_riesgo / total) * 100, 1)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total estudiantes", f"{total:,}")
col2.metric("Promedio Exam Score", promedio_score)
col3.metric("Promedio hs. estudio", f"{promedio_estudio} hs")
col4.metric("Promedio hs. sueño", f"{promedio_sueno} hs")
col5.metric("Estudiantes en riesgo", f"{porcentaje_riesgo}%", f"{en_riesgo} estudiantes")

st.divider()

# ── 4. TABS PRINCIPALES ──────────────────────────────────────────────────────
st.header("3. Explorar el dataset")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Estadísticas",
    "📈 Gráficos",
    "⚠️ Riesgo académico",
    "👤 Mi reporte individual"
])

# ── TAB 1: ESTADÍSTICAS ──────────────────────────────────────────────────────
with tab1:
    st.subheader("Estadísticas descriptivas")

    columnas = ["Hours_Studied", "Sleep_Hours", "Attendance", "Tutoring_Sessions", "Exam_Score"]
    etiquetas = {
        "Hours_Studied": "Horas de estudio",
        "Sleep_Hours": "Horas de sueño",
        "Attendance": "Asistencia (%)",
        "Tutoring_Sessions": "Sesiones de tutoría",
        "Exam_Score": "Puntaje del examen"
    }

    filas = []
    for col in columnas:
        filas.append({
            "Variable": etiquetas[col],
            "Promedio": round(df[col].mean(), 2),
            "Máximo": int(df[col].max()),
            "Mínimo": int(df[col].min()),
            "Desvío estándar": round(df[col].std(), 2)
        })

    st.dataframe(pd.DataFrame(filas), use_container_width=True, hide_index=True)

    st.subheader("Correlaciones con Exam Score (Pearson)")

    variables_corr = ["Hours_Studied", "Sleep_Hours", "Attendance"]
    filas_corr = []
    for variable in variables_corr:
        r = round(df[variable].corr(df["Exam_Score"]), 4)
        abs_r = abs(r)
        if abs_r >= 0.5:
            interpretacion = "Alta positiva" if r > 0 else "Alta negativa"
        elif abs_r >= 0.3:
            interpretacion = "Media positiva" if r > 0 else "Media negativa"
        else:
            interpretacion = "Baja"
        filas_corr.append({
            "Variable": etiquetas[variable],
            "Coeficiente r": r,
            "Interpretación": interpretacion
        })

    st.dataframe(pd.DataFrame(filas_corr), use_container_width=True, hide_index=True)

# ── TAB 2: GRÁFICOS ──────────────────────────────────────────────────────────
with tab2:
    st.subheader("Dashboard de visualizaciones")

    col_a, col_b = st.columns(2)

    with col_a:
        fig1, ax1 = plt.subplots(figsize=(7, 4))
        frecuencias = df["Exam_Score"].value_counts().sort_index()
        ax1.bar(frecuencias.index, frecuencias.values, color="steelblue")
        ax1.set_xlabel("Exam Score")
        ax1.set_ylabel("Cantidad de estudiantes")
        ax1.set_title("Distribución de Exam Score")
        ax1.grid(axis="y")
        st.pyplot(fig1)
        plt.close(fig1)

    with col_b:
        fig2, ax2 = plt.subplots(figsize=(7, 4))
        ax2.scatter(df["Hours_Studied"], df["Exam_Score"], alpha=0.4, color="steelblue", s=10)
        ax2.set_xlabel("Horas de estudio")
        ax2.set_ylabel("Puntaje del examen")
        ax2.set_title("Horas de estudio vs Puntaje")
        ax2.grid(True)
        st.pyplot(fig2)
        plt.close(fig2)

    col_c, col_d = st.columns(2)

    with col_c:
        fig3, ax3 = plt.subplots(figsize=(7, 4))
        ax3.scatter(df["Sleep_Hours"], df["Exam_Score"], alpha=0.4, color="mediumpurple", s=10)
        ax3.set_xlabel("Horas de sueño")
        ax3.set_ylabel("Puntaje del examen")
        ax3.set_title("Horas de sueño vs Puntaje")
        ax3.grid(True)
        st.pyplot(fig3)
        plt.close(fig3)

    with col_d:
        fig4, ax4 = plt.subplots(figsize=(7, 4))
        ax4.scatter(df["Attendance"], df["Exam_Score"], alpha=0.4, color="seagreen", s=10)
        ax4.set_xlabel("Asistencia (%)")
        ax4.set_ylabel("Puntaje del examen")
        ax4.set_title("Asistencia vs Puntaje")
        ax4.grid(True)
        st.pyplot(fig4)
        plt.close(fig4)

# ── TAB 3: RIESGO ────────────────────────────────────────────────────────────
with tab3:
    st.subheader("Reporte de riesgo académico")

    st.metric("Estudiantes en perfil de riesgo", f"{en_riesgo} de {total}", f"{porcentaje_riesgo}%")

    st.markdown("#### Análisis por indicador individual")

    indicadores = [
        ("Exam_Score",       "Puntaje de examen bajo (< 65)"),
        ("Sleep_Hours",      "Horas de sueño insuficientes (< 6)"),
        ("Hours_Studied",    "Pocas horas de estudio (< 16 semanales)"),
        ("Attendance",       "Asistencia insuficiente (< 70%)"),
        ("Motivation_Level", "Motivación baja (Low)"),
    ]

    filas_riesgo = []
    for cond, descripcion in indicadores:
        afectados = len(evaluar_condicion(df, cond))
        porcentaje = round((afectados / total) * 100, 1)
        filas_riesgo.append({
            "Indicador": descripcion,
            "Estudiantes afectados": afectados,
            "Porcentaje": f"{porcentaje}%"
        })

    st.dataframe(pd.DataFrame(filas_riesgo), use_container_width=True, hide_index=True)

    st.info("Un estudiante se clasifica en riesgo si cumple al menos 2 de estas condiciones. Los umbrales se calcularon usando el percentil 25 del dataset.")

# ── TAB 4: REPORTE INDIVIDUAL ─────────────────────────────────────────────────
with tab4:
    st.subheader("Ingresá tus datos para ver tu reporte")

    with st.form("formulario_usuario"):
        col1, col2 = st.columns(2)

        with col1:
            hours_studied = st.slider("Horas de estudio semanales", 1, 44, 20)
            sleep_hours = st.slider("Horas de sueño por noche", 4, 10, 7)
            attendance = st.slider("Porcentaje de asistencia", 0, 100, 80)

        with col2:
            motivation = st.selectbox("Nivel de motivación", ["Low", "Medium", "High"], index=1)
            tutoring = st.slider("Sesiones de tutoría por mes", 0, 8, 1)
            exam_score = st.slider("Puntaje de tu último examen", 55, 100, 70)

        enviado = st.form_submit_button("Generar mi reporte", use_container_width=True)

    if enviado:
        usuario = {
            "Hours_Studied": hours_studied,
            "Sleep_Hours": sleep_hours,
            "Attendance": attendance,
            "Motivation_Level": motivation,
            "Tutoring_Sessions": tutoring,
            "Exam_Score": exam_score
        }

        comparaciones = comparar_con_dataset(usuario, df)

        st.markdown("#### Tu perfil vs el dataset")

        variables_mostrar = ["Hours_Studied", "Sleep_Hours", "Attendance", "Tutoring_Sessions", "Exam_Score"]
        etiquetas_ind = {
            "Hours_Studied": "Horas de estudio",
            "Sleep_Hours": "Horas de sueño",
            "Attendance": "Asistencia (%)",
            "Tutoring_Sessions": "Sesiones de tutoría",
            "Exam_Score": "Puntaje del examen"
        }

        cols = st.columns(len(variables_mostrar))
        for i, var in enumerate(variables_mostrar):
            comp = comparaciones[var]
            delta = round(comp["valor_usuario"] - comp["promedio"], 2)
            cols[i].metric(
                etiquetas_ind[var],
                comp["valor_usuario"],
                f"{'+' if delta >= 0 else ''}{delta} vs promedio"
            )

        st.markdown("#### Gráficos comparativos")

        fig_rep, axes = plt.subplots(1, 3, figsize=(14, 5))
        fig_rep.suptitle("Tu perfil vs el dataset")

        variables_barras = ["Hours_Studied", "Sleep_Hours", "Attendance", "Exam_Score"]
        etiquetas_barras = ["Hs. estudio", "Hs. sueño", "Asistencia", "Puntaje"]
        valores_usuario = [comparaciones[v]["valor_usuario"] for v in variables_barras]
        valores_promedio = [comparaciones[v]["promedio"] for v in variables_barras]
        x = range(len(variables_barras))

        axes[0].bar(x, valores_promedio, color="gray", label="Promedio dataset", width=0.4)
        axes[0].bar([i + 0.4 for i in x], valores_usuario, color="steelblue", label="Tus valores", width=0.4)
        axes[0].set_xticks([i + 0.2 for i in x])
        axes[0].set_xticklabels(etiquetas_barras)
        axes[0].set_title("Tus valores vs promedio")
        axes[0].legend()

        axes[1].scatter(df["Hours_Studied"], df["Exam_Score"], color="gray", label="Dataset", alpha=0.3, s=10)
        axes[1].scatter(usuario["Hours_Studied"], usuario["Exam_Score"], color="red", s=150, label="Vos", zorder=5)
        axes[1].set_xlabel("Horas de estudio")
        axes[1].set_ylabel("Puntaje")
        axes[1].set_title("Estudio vs Puntaje")
        axes[1].legend()

        axes[2].scatter(df["Sleep_Hours"], df["Exam_Score"], color="gray", label="Dataset", alpha=0.3, s=10)
        axes[2].scatter(usuario["Sleep_Hours"], usuario["Exam_Score"], color="red", s=150, label="Vos", zorder=5)
        axes[2].set_xlabel("Horas de sueño")
        axes[2].set_ylabel("Puntaje")
        axes[2].set_title("Sueño vs Puntaje")
        axes[2].legend()

        plt.tight_layout()
        st.pyplot(fig_rep)
        plt.close(fig_rep)

        st.markdown("#### Evaluación de riesgo académico")

        en_riesgo_usuario = evaluar_riesgo_usuario(usuario)

        if en_riesgo_usuario:
            st.error("⚠️ Presentás un perfil de riesgo académico. Revisá las señales detectadas.")
        else:
            st.success("✅ Tu perfil no presenta riesgo académico.")