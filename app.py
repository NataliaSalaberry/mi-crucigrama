import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Crucigrama de Estadística", layout="wide")


st.markdown("""
    <style>
    
    .stApp {
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT-vmlvuNFA7ztceIoawtRYmMtYJUrmctRzg&s');
        background-size: cover; /* Cubre el área manteniendo proporción */
        background-position: center center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    
    
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(255, 255, 255, 0.8); 
        z-index: -1;
    }

    
    div[data-baseweb="input"] {
        background-color: #3b82f6 !important; /* Azul más vibrante */
        border: 2px solid #1e3a8a !important;
        border-radius: 4px !important;
    }

   
    input {
        color: #000000 !important; /* Negro puro */
        -webkit-text-fill-color: #000000 !important; 
        text-align: center !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
    }

    
    .pista-num {
        font-size: 13px;
        color: #1e3a8a;
        font-weight: 800;
        margin-bottom: -5px;
        text-align: center;
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

clue_nums = {(2, 4): "1", (1, 4): "2", (2, 7): "3", (9, 6): "4", (1, 14): "5", (4, 11): "6"}


st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>📊 Crucigrama de Estadística Descriptiva</h1>", unsafe_allow_html=True)
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
                    num = clue_nums.get((r, c), "")
                    if num:
                        st.markdown(f'<p class="pista-num">{num}</p>', unsafe_allow_html=True)
                    
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
if st.button("VERIFICAR RESULTADOS", type="primary"):
    aciertos = 0
    for (r, c), letra in user_inputs.items():
        if letra.strip().upper() == solucion[(r, c)]:
            aciertos += 1
    
    if aciertos == len(solucion):
        st.balloons()
        st.success(f"¡Excelente! Todo está correcto ({aciertos}/{len(solucion)})")
    else:
        st.info(f"Has completado {aciertos} letras correctamente de {len(solucion)}.")

# --- DEFINICIONES ---
st.markdown("<br>", unsafe_allow_html=True)
col_p1, col_p2 = st.columns(2)
with col_p1:
    st.markdown("""
    <div class="pistas-box">
    <h3>HORIZONTALES</h3>
    <b>1.</b> Disciplina que permite describir datos.<br>
    <b>4.</b> Medida que brinda el 50% central de una distribución.<br>
    <b>6.</b> Medida que brinda la mitad de una distribución.
    </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown("""
    <div class="pistas-box">
    <h3>VERTICALES</h3>
    <b>2.</b> Valor que acumula un porcentaje de datos en la distribución.<br>
    <b>3.</b> Medida de la falta de simetría de una distribución.<br>
    <b>5.</b> Medida de dispersión o variabilidad.
    </div>
    """, unsafe_allow_html=True)
