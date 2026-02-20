import streamlit as st
from datetime import datetime
import time

# 1. FORÇAR CORES SOCIALMED (PRETO, VERMELHO, BRANCO)
st.set_page_config(page_title="SocialMed - Portal Master", layout="wide")

st.markdown("""
    <style>
    /* FORÇAR FUNDO PRETO EM TUDO */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000 !important;
        color: #ffffff !important;
    }

    /* FORÇAR BARRA LATERAL ESCURA */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
        border-right: 2px solid #ff0000 !important;
    }

    /* FORÇAR BOTÃO VERMELHO SOCIALMED */
    div.stButton > button {
        background-color: #ff0000 !important;
        color: white !important;
        border: 2px solid #ff0000 !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 20px !important;
        padding: 10px !important;
    }
    
    /* BOTÃO QUANDO PASSA O RATO */
    div.stButton > button:hover {
        background-color: #ffffff !important;
        color: #ff0000 !important;
        border: 2px solid #ff0000 !important;
    }

    /* FORÇAR TÍTULOS EM VERMELHO */
    h1, h2, h3, span, label {
        color: #ff0000 !important;
    }

    /* CAIXAS DE TEXTO */
    .stTextArea textarea, .stTextInput input {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #ff0000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar créditos
if 'saldo_creditos' not in st.session_state:
    st.session_state.saldo_creditos = 60

# 2. PAINEL DE CONTROLO MASTER
with st.sidebar:
    st.markdown("<h2 style='color:white !important;'>🛠️ GESTÃO MASTER</h2>", unsafe_allow_html=True)
    chave = st.text_input("Chave Master:", type="password")
    
    nome_clinica = "Centro Médico Cavi"
    endereco_clinica = "Endereço não configurado"

    if chave == "954446205":
        st.success("Modo Master: SocialMed Ativo")
        nome_clinica = st.text_input("Nome da Clínica:", value=nome_clinica)
        endereco_clinica = st.text_input("Endereço:", value=endereco_clinica)
        
        st.write("---")
        novos = st.number_input("Adicionar Créditos:", min_value=0)
        if st.button("RECARREGAR AGORA"):
            st.session_state.saldo_creditos += novos
            st.toast("Saldo Atualizado!")
    
    st.markdown(f"<p style='color:white;'>Saldo: {st.session_state.saldo_creditos} exames</p>", unsafe_allow_html=True)

# 3. INTERFACE PRINCIPAL
col_l, col_t, col_d = st.columns([1, 2, 1])
with col_l:
    st.markdown("<h1 style='margin:0;'>🔴</h1>", unsafe_allow_html=True)
with col_t:
    st.markdown(f"<h1 style='text-align:center;'>PORTAL {nome_clinica.upper()}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:white !important;'>{endereco_clinica}</p>", unsafe_allow_html=True)
with col_d:
    st.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")
    st.write(f"⏰ {datetime.now().strftime('%H:%M:%S')}")

st.write("---")

# 4. TRIAGEM E MÉDICO
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Triagem do Paciente")
    nome_p = st.text_input("Nome do Paciente:")
    c1, c2, c3 = st.columns(3)
    with c1: idade_p = st.number_input("Idade:", min_value=0)
    with c2: peso_p = st.number_input("Peso (kg):", format="%.1f")
    with c3: altura_p = st.number_input("Altura (cm):")
    
    st.write("---")
    st.subheader("📊 Exame")
    tipo = st.selectbox("Serviço:", ["ECG", "ESPIRIMETRIA"])
    arquivo = st.file_uploader("Upload do Gráfico")

with col2:
    st.subheader("👨‍⚕️ Espaço do Médico")
    obs = st.text_area("Notas Clínicas:", height=200, placeholder="Escreva aqui...")
    
    st.write(f"**Créditos:** {st.session_state.saldo_creditos}")
    
    if st.button("🚀 GERAR LAUDO SOCIALMED"):
        if nome_p and arquivo and st.session_state.saldo_creditos > 0:
            st.session_state.saldo_creditos -= 1
            with st.status("⚙️ IA SocialMed a Processar...") as s:
                time.sleep(2)
                s.update(label="✅ LAUDO CONCLUÍDO!", state="complete")
        else:
            st.error("Verifique os dados ou o saldo.")

st.write("---")
st.markdown("<center><p style='color:gray;'>SOCIALMED © 2026 | Marketing & Tecnologia</p></center>", unsafe_allow_html=True)
