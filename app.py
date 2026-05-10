import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Crucigrama de Estadística", layout="wide")

# --- ESTILO CSS CORREGIDO ---
st.markdown("""
    <style>
    /* 1. Imagen de fondo con mayor prioridad */
    .stApp {
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT-vmlvuNFA7ztceIoawtRYmMtYJUrmctRzg&s');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Capa blanca semitransparente para que se lea el texto */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(255, 255, 255, 0.85); /* Controla la transparencia aquí */
        z-index: -1;
    }

    /* 2. Forzar el color AZUL OSCURO en los cuadraditos de entrada */
    div[data-baseweb="input"] {
        background-color: #002366 !important;
        border: 1px solid #004080 !important;
    }

    /* 3. Forzar el color de la LETRA BLANCA y centrarla */
    input {
        color: white !important;
        -webkit-text-fill-color: white !important; /* Necesario para algunos navegadores */
        text-align: center !important;
        font-weight: bold !important;
        caret-color: white !important; /* El cursor también blanco */
    }

    /* 4. Estilo de los números de las pistas */
    .pista-num {
        font-size: 12px;
        color: #002366;
        font-weight: bold;
        margin-bottom: -10px;
        text-align: center;
    }
    
    /* 5. Contenedor de definiciones */
    .pistas-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #002366;
        color: #002366;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DEL CRUCIGRAMA ---
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

# --- INTERFAZ ---
st.markdown("<h1 style='text-align: center; color: #002366;'>📊 Crucigrama de Estadística Descriptiva</h1>", unsafe_allow_html=True)
st.write("")

# Crear el tablero usando columnas
max_row, max_col = 11, 18
user_inputs = {}

for r in range(max_row):
    cols = st.columns(max_col)
    for c in range(max_col):
        with cols[c]:
            if (r, c) in solucion:
                num = clue_nums.get((r, c), "")
                if num:
                    st.markdown(f'<p class="pista-num">{num}</p>', unsafe_allow_html=True)
                
                # Widget de entrada
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
col_btn, _ = st.columns([1, 4])
with col_btn:
    verificar = st.button("VERIFICAR RESULTADOS")

if verificar:
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
    <b>2.</b> Alguno de los 100 valores posibles que acumulan en una distribución.<br>
    <b>3.</b> Medida del sesgo de una distribución.<br>
    <b>5.</b> Medida de variabilidad.
    </div>
    """, unsafe_allow_html=True)
