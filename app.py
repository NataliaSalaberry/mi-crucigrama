import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Crucigrama de Estadística", layout="wide")

# --- ESTILO CSS PERSONALIZADO ---
st.markdown(f"""
    <style>
    /* Imagen de fondo con transparencia */
    .stApp {{
        background-color: rgba(255, 255, 255, 0.85);
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT-vmlvuNFA7ztceIoawtRYmMtYJUrmctRzg&s');
        background-size: cover;
        background-position: center;
        opacity: 0.15;
        z-index: -1;
    }}

    /* Estilo de los cuadraditos azules */
    div[data-baseweb="input"] {{
        background-color: #002366 !important;
        border-radius: 5px;
        border: 1px solid #004080;
    }}
    input {{
        color: white !important;
        text-align: center !important;
        font-weight: bold !important;
        font-size: 20px !important;
    }}
    
    /* Etiquetas de números de pistas */
    .pista-num {{
        font-size: 10px;
        color: #002366;
        font-weight: bold;
        margin-bottom: -15px;
    }}
    
    /* Área de definiciones */
    .pistas-box {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #d5dbdb;
        color: #2e4053;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DEL CRUCIGRAMA ---
solucion = {}
# 1. ESTADISTICA (H - Fila 2)
p1 = "ESTADISTICA"
for i, l in enumerate(p1): solucion[(2, 4 + i)] = l
# 2. PERCENTIL (V - Columna 4)
p2 = "PERCENTIL"
for i, l in enumerate(p2): solucion[(1 + i, 4)] = l
# 3. ASIMETRIA (V - Columna 7)
p3 = "ASIMETRIA"
for i, l in enumerate(p3): solucion[(2 + i, 7)] = l
# 5. VARIANZA (V - Columna 14) 
p5 = "VARIANZA"
for i, l in enumerate(p5): solucion[(1 + i, 14)] = l
# 6. MEDIANA (H - Fila 4)
p6 = "MEDIANA"
for i, l in enumerate(p6): solucion[(4, 11 + i)] = l
# 4. RIC (H - Fila 9)
p4 = "RIC"
for i, l in enumerate(p4): solucion[(9, 6 + i)] = l

clue_nums = {(2, 4): "1", (1, 4): "2", (2, 7): "3", (9, 6): "4", (1, 14): "5", (4, 11): "6"}

# --- INTERFAZ ---
st.title("📊 Crucigrama de Estadística Descriptiva")
st.write("Completa el crucigrama y pulsa el botón para verificar.")

# Crear el tablero
max_row, max_col = 11, 18
user_inputs = {}

# Generar la cuadrícula
for r in range(max_row):
    cols = st.columns(max_col)
    for c in range(max_col):
        with cols[c]:
            if (r, c) in solucion:
                num = clue_nums.get((r, c), "")
                if num:
                    st.markdown(f'<p class="pista-num">{num}</p>', unsafe_allow_html=True)
                else:
                    st.write("") # Espacio para alinear
                
                user_inputs[(r, c)] = st.text_input(
                    label=f"cell_{r}_{c}",
                    value="",
                    max_chars=1,
                    key=f"{r}_{c}",
                    label_visibility="collapsed"
                )
            else:
                st.write("")

# --- VERIFICACIÓN ---
if st.button("VERIFICAR RESULTADOS"):
    aciertos = 0
    for (r, c), letra in user_inputs.items():
        if letra.strip().upper() == solucion[(r, c)]:
            aciertos += 1
    
    if aciertos == len(solucion):
        st.balloons()
        st.success(f"¡Excelente! Todo está correcto ({aciertos}/{len(solucion)})")
    else:
        st.warning(f"Has acertado {aciertos} letras de {len(solucion)}. ¡Sigue intentando!")

# --- DEFINICIONES ---
st.markdown("---")
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
    <b>2.</b> Alguno de los 100 valores posibles que acumulan en una distribución.<br>
    <b>3.</b> Medida del sesgo de una distribución.<br>
    <b>5.</b> Medida de variabilidad.
    </div>
    """, unsafe_allow_html=True)