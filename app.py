import streamlit as st

# =====================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# =====================================================================
st.set_page_config(page_title="Juego de Etapas: Estadística", layout="wide")

# Inicialización del estado del juego (Etapa 0: Presentación)
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0

# Estilos CSS originales
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
    </style>
    """, unsafe_allow_html=True)


# =====================================================================
# ETAPA 0: PRESENTACIÓN DEL JUEGO
# =====================================================================
if st.session_state.etapa == 0:
    st.markdown("<p class='etapa-header'>📊 Desafío de una Encrucijada de Estadística Descriptiva</p>", unsafe_allow_html=True)
    st.markdown("<p class='autor-header'>Elaborado por Natalia Salaberry</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        st.markdown("""
        <div class="pistas-box" style="font-size: 1.15rem; line-height: 1.6; text-align: justify;">
        Este desafío aborda los conceptos de estadística descriptiva relacionados a la construcción de 
        información analítica sobre la cotización de un activo financiero. Los desafíos se presentan en 
        cinco etapas, que incluyen juegos conceptuales y prácticos. <br><br>
        Para poder superar cada etapa y escapar con éxito de la encrucijada, deberás resolver en orden 
        consecutivo las mismas. Una vez que completes con éxito la primera etapa, selecciona en el botón 
        inferior para pasar a la siguiente, y así sucesivamente.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("COMENZAR 🚀", type="primary", use_container_width=True):
            st.session_state.etapa = 1
            st.rerun()


# =====================================================================
# ETAPA 1: EL CRUCIGRAMA
# =====================================================================
elif st.session_state.etapa == 1:
    st.markdown("<p class='etapa-header'>📊 Etapa 1: Crucigrama de Estadística Descriptiva</p>", unsafe_allow_html=True)
    st.markdown("<p class='autor-header'>Elaborado por Natalia Salaberry</p>", unsafe_allow_html=True)
    
    solucion = {}
    p1 = "ESTADISTICA"
    for i, l in enumerate(p1): solucion[(2, 4 + i)] = l
    p2 = "PERCENTIL"
    for i, l in enumerate(p2): solucion[(1 + i, 4)] = l
    p3 = "ASIMETRIA"
    for i, l in enumerate(p3): solucion[(2 + i, 7)] = l
    p5 = "VARIANZA"
    for i, l in enumerate(p5): solucion[(1 + i, 14)] = l
    p6 = "MEDIANA"
    for i, l in enumerate(p6): solucion[(4, 11 + i)] = l
    p4 = "RIC"
    for i, l in enumerate(p4): solucion[(9, 6 + i)] = l

    max_row, max_col = 11, 18
    user_inputs = {}

    _, center_col, _ = st.columns([1, 10, 1])

    with center_col:
        for r in range(max_row):
            cols = st.columns(max_col)
            for c in range(max_col):
                with cols[c]:
                    if (r, c) in solucion:
                        user_inputs[(r, c)] = st.text_input(
                            label=f"c{r}{c}",
                            value="",
                            max_chars=1,
                            key=f"cr_e1_{r}_{c}",
                            label_visibility="collapsed"
                        )
                    else:
                        st.write("")

    st.write("")
    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        btn_verificar = st.button("VERIFICAR CRUCIGRAMA", type="primary", use_container_width=True)

    if btn_verificar:
        aciertos = sum(1 for (r, c), letra in user_inputs.items() if letra.strip().upper() == solucion[(r, c)])
        
        if aciertos == len(solucion):
            st.session_state.etapa = 2
            st.rerun()
        else:
            st.error(f"Has completado {aciertos} letras correctamente de {len(solucion)}. ¡Sigue intentando!")

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
    st.markdown("<p class='etapa-header'>🔢 Etapa 2: Varianza y Desviación</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box">
        <h3>El reto de la dispersión</h3>
        Si calculamos la <b>Varianza</b> de una muestra de tiempos de carga y el resultado es <b>25</b>, 
        ¿cuál es el valor de su <b>Desviación Estándar</b>?
        </div>
        """, unsafe_allow_html=True)
        
        respuesta_2 = st.number_input("Ingresa tu respuesta numérica:", value=0, step=1, key="input_e2")
        
        if st.button("Validar Respuesta", type="primary", use_container_width=True):
            if respuesta_2 == 5:
                st.session_state.etapa = 3
                st.rerun()
            else:
                st.error("Respuesta incorrecta. Recuerda la relación matemática entre ambas medidas.")


# =====================================================================
# ETAPA 3: INTERPRETACIÓN DE GRÁFICOS / ASIMETRÍA
# =====================================================================
elif st.session_state.etapa == 3:
    st.markdown("<p class='etapa-header'>📈 Etapa 3: Análisis de Formas</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box">
        <h3>Relación de Medidas</h3>
        En un análisis de salarios se observa que la <b>Media</b> es notablemente <b>mayor</b> que la <b>Mediana</b> (Media > Mediana). 
        ¿Qué tipo de asimetría presenta esta distribución?
        </div>
        """, unsafe_allow_html=True)
        
        opcion_3 = st.radio(
            "Selecciona la opción correcta:",
            ["Asimetría Negativa (A la izquierda)", "Distribución Simétrica", "Asimetría Positiva (A la derecha)"],
            key="radio_e3"
        )
        
        if st.button("Validar Respuesta", type="primary", use_container_width=True):
            if opcion_3 == "Asimetría Positiva (A la derecha)":
                st.session_state.etapa = 4
                st.rerun()
            else:
                st.error("Incorrecto. Piensa hacia dónde se desplaza la media cuando hay valores muy altos.")


# =====================================================================
# ETAPA 4: RANGO INTERCUARTÍLICO
# =====================================================================
elif st.session_state.etapa == 4:
    st.markdown("<p class='etapa-header'>📊 Etapa 4: Caja y Bigotes (RIC)</p>", unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box">
        <h3>Calculando con Cuartiles</h3>
        Tienes los siguientes datos clave de una muestra:<br>
        • Primer Cuartil (Q1) = <b>12</b><br>
        • Mediana (Q2) = <b>18</b><br>
        • Tercer Cuartil (Q3) = <b>30</b><br><br>
        ¿Cuál es el valor del <b>Rango Intercuartílico (RIC)</b>?
        </div>
        """, unsafe_allow_html=True)
        
        respuesta_4 = st.number_input("Ingresa tu respuesta numérica:", value=0, step=1, key="input_e4")
        
        if st.button("Validar Respuesta", type="primary", use_container_width=True):
            if respuesta_4 == 18:
                st.session_state.etapa = 5
                st.rerun()
            else:
                st.error("Incorrecto. La fórmula del RIC solo requiere dos de esos datos.")


# =====================================================================
# ETAPA 5: PANTALLA FINAL DE ÉXITO
# =====================================================================
elif st.session_state.etapa == 5:
    st.balloons()
    _, center_col, _ = st.columns([2, 4, 2])
    with center_col:
        st.markdown("""
        <div class="pistas-box" style="text-align: center; border-color: #10b981;">
        <h2 style="color: #10b981;">🏆 ¡Felicidades! 🏆</h2>
        <p style="font-size: 1.2rem;">Has superado con éxito el crucigrama y todas las etapas conceptuales de Estadística Descriptiva.</p>
        <b>¡Eres un experto/a manejando datos!</b>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Volver a jugar", type="secondary", use_container_width=True):
            st.session_state.etapa = 0
            st.rerun()
