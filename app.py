import streamlit as pd
import streamlit as st
import pandas as pd
import numpy as np
import time

# =====================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# =====================================================================
st.set_page_config(page_title="Juego de Etapas: Estadística", layout="wide")

# Inicialización del estado del juego
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0

if 'tiempo_limite' not in st.session_state:
    st.session_state.tiempo_limite = None

# Mapeo de la solución del crucigrama
solucion_crucigrama = {
    (2, 4): "E", (2, 5): "S", (2, 6): "T", (2, 7): "A", (2, 8): "D", (2, 9): "I", (2, 10): "S", (2, 11): "T", (2, 12): "I", (2, 13): "C", (2, 14): "A",
    (1, 4): "P", (3, 4): "R", (4, 4): "C", (5, 4): "E", (6, 4): "N", (7, 4): "T", (8, 4): "I", (9, 4): "L",
    (3, 7): "S", (4, 7): "I", (5, 7): "M", (6, 7): "E", (7, 7): "T", (8, 7): "R", (9, 7): "I", (10, 7): "A",
    (1, 14): "V", (3, 14): "R", (4, 14): "I", (5, 14): "A", (6, 14): "N", (7, 14): "Z", (8, 14): "A",
    (4, 11): "M", (4, 12): "E", (4, 13): "D", (4, 15): "A", (4, 16): "N", (4, 17): "A",
    (9, 6): "R", (9, 8): "C"
}

# Inicializar y asegurar las llaves del crucigrama en session_state
if 'respuestas_crucigrama' not in st.session_state:
    st.session_state.respuestas_crucigrama = {}

for (r, c) in solucion_crucigrama.keys():
    clave_celda = f"{r}_{c}"
    if clave_celda not in st.session_state.respuestas_crucigrama:
        st.session_state.respuestas_crucigrama[clave_celda] = ""

# Estilos CSS (Incluye el contador flotante abajo a la derecha)
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1509228468518-180dd48219d1?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; 
        background-position: center center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(255, 255, 255, 0.85); 
        z-index: -1;
    }
    div[data-baseweb="input"] {
        background-color: #3b82f6 !important; 
        border: 2px solid #1e3a8a !important;
        border-radius: 4px !important;
    }
    input {
        color: #000000 !important; 
        -webkit-text-fill-color: #000000 !important; 
        text-align: center !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
    }
    .pistas-box {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 10px;
        border: 2px solid #1e3a8a;
        color: #1e3a8a;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .etapa-header {
        text-align: center; 
        color: #1e3a8a;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .autor-header {
        text-align: center; 
        color: #1e3a8a;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .contador-flotante {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #1e3a8a;
        color: white;
        padding: 10px 20px;
        border-radius: 30px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        z-index: 9999;
        border: 2px solid #ffffff;
    }
    .contador-alerta {
        background-color: #b91c1c !important;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.6; }
        100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)


# =====================================================================
# LÓGICA DEL CONTADOR DE TIEMPO (3 MINUTOS POR ETAPA)
# =====================================================================
if 0 < st.session_state.etapa < 6:
    if st.session_state.tiempo_limite is not None:
        tiempo_restante = int(st.session_state.tiempo_limite - time.time())
        
        if tiempo_restante <= 0:
            st.session_state.etapa = 0
            st.session_state.tiempo_limite = None
            st.session_state.respuestas_crucigrama = {f"{r}_{c}": "" for (r, c) in solucion_crucigrama.keys()}
            st.error("⏰ Te quedaste sin tiempo, debes volver a comenzar")
            time.sleep(3.5)
            st.rerun()
        
        minutos = tiempo_restante // 60
        segundos = tiempo_restante % 60
        
        clase_alerta = " contador-alerta" if tiempo_restante <= 30 else ""
        st.markdown(
            f'<div class="contador-flotante{clase_alerta}">'
            f'⏳ Etapa {st.session_state.etapa} — {minutos:02d}:{segundos:02d}'
            f'</div>', 
            unsafe_allow_html=True
        )


# =====================================================================
# ETAPA 0: PRESENTACIÓN DEL JUEGO
# =====================================================================
if st.session_state.etapa == 0:
    st.markdown("<p class='etapa-header'>📊 Desafío: Encrucijada de Estadística Descriptiva</p>", unsafe_allow_html=True)
    st.markdown("<p class='autor-header'>Elaborado por Natalia Salaberry</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        st.markdown("""
        <div class="pistas-box" style="font-size: 1.15rem; line-height: 1.6; text-align: justify;">
        Este desafío aborda los conceptos de estadística descriptiva relacionados a la construcción de 
        información analítica descriptiva sobre la cotización de un activo financiero. Los desafíos se presentan en 
        cinco etapas, que incluyen resolver actividades conceptuales y prácticas. <br><br>
        Para poder superar cada etapa y escapar con éxito de la encrucijada, deberás resolver en orden 
        consecutivo las mismas. Una vez que completes con éxito una etapa, selecciona en el botón 
        inferior para pasar a la siguiente. Cuentas con un tiempo máximo de 3 minutos en cada etapa.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("COMENZAR 🚀", type="primary", use_container_width=True):
            st.session_state.tiempo_limite = time.time() + (3 * 60)
            st.session_state.etapa = 1
            st.rerun()


# =====================================================================
# ETAPA 1: EL CRUCIGRAMA
# =====================================================================
elif st.session_state.etapa == 1:
    st.markdown("<p class='etapa-header'>📊 Etapa 1: Resolver el Crucigrama</p>", unsafe_allow_html=True)
    
    max_row, max_col = 11, 18
    _, center_col, _ = st.columns([1, 10, 1])

    with center_col:
        for r in range(max_row):
            cols = st.columns(max_col)
            for c in range(max_col):
                with cols[c]:
                    clave_celda = f"{r}_{c}"
                    if (r, c) in solucion_crucigrama:
                        st.session_state.respuestas_crucigrama[clave_celda] = st.text_input(
                            label=f"input_{r}_{c}",
                            value=st.session_state.respuestas_crucigrama[clave_celda],
                            max_chars=1,
                            key=f"celda_widget_{r}_{c}",
                            label_visibility="collapsed"
                        )
                    else:
                        st.write("")

    st.write("")
    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        btn_verificar = st.button("VERIFICAR CRUCIGRAMA", type="primary", use_container_width=True)

    if btn_verificar:
        aciertos = 0
        for (r, c), letra_correcta in solucion_crucigrama.items():
            letra_usuario = st.session_state.respuestas_crucigrama[f"{r}_{c}"]
            if letra_usuario.strip().upper() == letra_correcta:
                aciertos += 1
        
        if aciertos == len(solucion_crucigrama):
            st.session_state.tiempo_limite = time.time() + (3 * 60)
            st.session_state.etapa = 2
            st.rerun()
        else:
            st.error(f"Has completado {aciertos} letras correctamente de {len(solucion_crucigrama)}. ¡Sigue intentando!")

    st.markdown("<br>", unsafe_allow_html=True)
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("""
        <div class="pistas-box">
        <h3>HORIZONTALES</h3>
        <b>1. Disciplina que permite describir datos.</b><br>
        <b>2. Medida que brinda el 50% central de una distribución.</b><br>
        <b>3. Medida que indica la mitad de una distribución.</b>
        </div>
        """, unsafe_allow_html=True)

    with col_p2:
        st.markdown("""
        <div class="pistas-box">
        <h3>VERTICALES</h3>
        <b>1. Valor que acumula un porcentaje de datos en la distribución.</b><br>
        <b>2. Medida de la falta de simetría de una distribución.</b><br>
        <b>3. Medida de variabilidad.</b>
        </div>
        """, unsafe_allow_html=True)


# =====================================================================
# ETAPA 2: CÁLCULO DE DISPERSIÓN
# =====================================================================
elif st.session_state.etapa == 2:
    st.markdown("<p class='etapa-header'>🔢 Etapa 2: Calcular el desvío</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box">
        <h3>El reto de la dispersión</h3>
        Si calculamos la <b>Varianza</b> de una muestra de la cotización de un activo y el resultado es <b>25</b>, 
        ¿cuál es el valor de su <b>Desvío muestral</b>?
        </div>
        """, unsafe_allow_html=True)
        
        respuesta_2 = st.number_input("Ingresa tu respuesta numérica:", value=0, step=1, key="input_e2")
        
        if st.button("Validar Respuesta", type="primary", use_container_width=True):
            if respuesta_2 == 5:
                st.session_state.tiempo_limite = time.time() + (3 * 60)
                st.session_state.etapa = 3
                st.rerun()
            else:
                st.error("Respuesta incorrecta. Revisá la relación matemática entre ambas medidas.")


# =====================================================================
# ETAPA 3: INTERPRETACIÓN DE GRÁFICOS / ASIMETRÍA
# =====================================================================
elif st.session_state.etapa == 3:
    st.markdown("<p class='etapa-header'>📈 Etapa 3: Análisis de Asimetría</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box">
        <h3>Relación de Medidas</h3>
        En un análisis de una muestra de la cotización de un activo se observa el siguiente histograma: 
        ¿Qué tipo de asimetría presenta esta distribución?
        </div>
        """, unsafe_allow_html=True)
        
        st.write("**Representación gráfica de las cotizaciones analizadas:**")
        
        datos_histograma = pd.DataFrame({
            "Frecuencia (Días)": [45, 38, 25, 14, 8, 4, 2, 1]
        }, index=["$10-$20", "$20-$30", "$30-$40", "$40-$50", "$50-$60", "$60-$70", "$70-$80", "$80-$90"])
        
        st.bar_chart(datos_histograma, color="#1e3a8a")

        opcion_3 = st.radio(
            "Selecciona la opción correcta:",
            ["Asimetría Negativa (A la izquierda)", "Distribución Simétrica", "Asimetría Positiva (A la derecha)"],
            key="radio_e3"
        )
        
        if st.button("Validar Respuesta", type="primary", use_container_width=True):
            if opcion_3 == "Asimetría Positiva (A la derecha)":
                st.session_state.tiempo_limite = time.time() + (3 * 60)
                st.session_state.etapa = 4
                st.rerun()
            else:
                st.error("Incorrecto. Piensa hacia dónde se encuentra el sesgo, es decir, la cola de la distribución.")


# =====================================================================
# ETAPA 4: RANGO INTERCUARTÍLICO
# =====================================================================
elif st.session_state.etapa == 4:
    st.markdown("<p class='etapa-header'>📊 Etapa 4: Calcular el Rango Intercuartílico</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box">
        <h3>Calculando con Cuartiles</h3>
        Tienes las siguientes medidas calculadas sobre una muestra de la cotización de un activo:<br>
        • Primer Cuartil (Q1) = <b>12</b><br>
        • Mediana (Q2) = <b>18</b><br>
        • Tercer Cuartil (Q3) = <b>30</b><br><br>
        ¿Cuál es el valor del <b>Rango Intercuartílico (RIC)</b>?
        </div>
        """, unsafe_allow_html=True)
        
        st.write("**Boxplot de las cotizaciones con las medidas indicadas:**")
        
        datos_box = pd.DataFrame({
            "Precio ($)": [5, 12, 14, 18, 22, 30, 45]
        })
        
        st.vega_lite_chart(datos_box, {
            "width": "container",
            "height": 180,
            "config": {
                "view": {"stroke": "transparent"}
            },
            "layer": [
                {
                    "mark": {
                        "type": "boxplot", 
                        "extent": "min-max", 
                        "color": "#1e3a8a",
                        "median": {"color": "#b91c1c", "thickness": 3}
                    },
                    "encoding": {
                        "x": {
                            "field": "Precio ($)", 
                            "type": "quantitative", 
                            "scale": {"domain": [0, 50]},
                            "title": "Precio del Activo ($)"
                        }
                    }
                }
            ]
        })
        
        respuesta_4 = st.number_input("Ingresa tu respuesta numérica:", value=0, step=1, key="input_e4")
        
        if st.button("Validar Respuesta", type="primary", use_container_width=True):
            if respuesta_4 == 18:
                st.session_state.tiempo_limite = time.time() + (3 * 60)
                st.session_state.etapa = 5
                st.rerun()
            else:
                st.error("Incorrecto. Revisá la fórmula de cálculo del RIC.")


# =====================================================================
# ETAPA 5: CURTOSIS 
# =====================================================================
elif st.session_state.etapa == 5:
    st.markdown("<p class='etapa-header'>📉 Etapa 5: Análisis de Curtosis</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box">
        <h3>Grado de Concentración</h3>
        Dada la distribución de la cotización de un activo como la que se muestra a continuación, 
        ¿cómo es la <b>curtosis</b> de la distribución?
        </div>
        """, unsafe_allow_html=True)
        
        # Gráfico de una distribución platicúrtica 
        x = np.linspace(-4, 4, 100)
        y = np.where(np.abs(x) <= 3, 0.15 * (1 + np.cos(np.pi * x / 3)), 0) + 0.01
        
        df_curtosis = pd.DataFrame({
            "Precio del Activo": x,
            "Densidad de Frecuencia": y
        }).set_index("Precio del Activo")
        
        st.line_chart(df_curtosis, color="#1e3a8a")
        
        opcion_5 = st.radio(
            "Selecciona la opción correcta:",
            ["A - Leptocúrtica", "B - Platicúrtica", "C - Mesocúrtica"],
            key="radio_e5"
        )
        
        if st.button("Validar Respuesta", type="primary", use_container_width=True):
            if opcion_5 == "B - Platicúrtica":
                st.session_state.etapa = 6
                st.rerun()
            else:
                st.error("Incorrecto. Observa la altura de la curva en al parte central.")


# =====================================================================
# ETAPA 6: PANTALLA FINAL DE ÉXITO
# =====================================================================
elif st.session_state.etapa == 6:
    st.balloons()
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box" style="text-align: center; border-color: #10b981;">
        <h2 style="color: #10b981;">🏆 ¡Felicidades! 🏆</h2>
        <p style="font-size: 1.2rem;">Has superado con éxito todas las etapas.</p>
        <b>¡El desafío se encuentra resuelto!</b>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Volver a jugar", type="secondary", use_container_width=True):
            st.session_state.etapa = 0
            st.session_state.tiempo_limite = None
            st.session_state.respuestas_crucigrama = {f"{r}_{c}": "" for (r, c) in solucion_crucigrama.keys()}
            st.rerun()
