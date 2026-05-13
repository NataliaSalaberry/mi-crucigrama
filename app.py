import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Crucigrama de Estadística", layout="wide")


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
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #1e3a8a;
        color: #1e3a8a;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)


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


st.markdown("<h1 style='text-align: center; color: #1e3a8a;font-size: 20px;'>📊 Crucigrama de Conceptos de Estadística Descriptiva</h1>", unsafe_allow_html=True)
st.write("")

st.markdown("<h2 style='text-align: center; color: #1e3a8a;font-size: 14px;'>Elaborado por Natalia Salaberry</h2>", unsafe_allow_html=True)
st.write("")


max_row, max_col = 11, 18
user_inputs = {}


_, center_col, _ = st.columns([1, 10, 1])

with center_col:
    for r in range(max_row):
        cols = st.columns(max_col)
        for c in range(max_col):
            with cols[c]:
                if (r, c) in solucion:
                    # Se eliminó la parte que mostraba 'clue_nums'
                    user_inputs[(r, c)] = st.text_input(
                        label=f"c{r}{c}",
                        value="",
                        max_chars=1,
                        key=f"{r}_{c}",
                        label_visibility="collapsed"
                    )
                else:
                    st.write("")

st.write("")
col1, col2, col3 = st.columns([2, 2, 2])
with col2:
    btn_verificar = st.button("VERIFICAR RESULTADOS", type="primary", use_container_width=True)

if btn_verificar:
    aciertos = 0
    for (r, c), letra in user_inputs.items():
        if letra.strip().upper() == solucion[(r, c)]:
            aciertos += 1
    
    if aciertos == len(solucion):
        st.balloons()
        st.success(f"¡Excelente! Todo está correcto ({aciertos}/{len(solucion)})")
    else:
        st.info(f"Has completado {aciertos} letras correctamente de {len(solucion)}.")


st.markdown("<br>", unsafe_allow_html=True)
col_p1, col_p2 = st.columns(2)
with col_p1:
    st.markdown("""
    <div class="pistas-box">
    <h3>HORIZONTALES</h3>
    <b> Disciplina que permite describir datos.<br>
    <b> Medida que brinda el 50% central de una distribución.<br>
    <b> Medida que indica la mitad de una distribución.
    </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown("""
    <div class="pistas-box">
    <h3>VERTICALES</h3>
    <b> Valor que acumula un porcentaje de datos en la distribución.<br>
    <b> Medida de la falta de simetría de una distribución.<br>
    <b> Medida de variabilidad.
    </div>
    """, unsafe_allow_html=True)
