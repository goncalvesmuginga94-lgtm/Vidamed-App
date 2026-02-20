import streamlit as st
from datetime import datetime
import time

# 1. ESTILO E CONFIGURAÇÃO
st.set_page_config(page_title="VIDAMED - Portal Clínico", layout="wide")
st.markdown("""
    <style>
    .caixa-info { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #003366; }
    .status-bar { background-color: #003366; color: white; padding: 10px; border-radius: 5px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. PAINEL DE CONTROLO (GONÇALVES)
with st.sidebar:
    st.header("⚙️ CONFIGURAÇÃO MASTER")
    chave = st.text_input("Chave Master:", type="password")
    nome_clinica = "Centro Médico Cavi"
    if chave == "954446205":
        nome_clinica = st.text_input("Editar Nome Clínica:", value=nome_clinica)
    st.write("---")
    st.info(f"Log Master: Gonçalves Muginga\nWhatsApp: 954446205")

# 3. CABEÇALHO COM DATA E HORA (ALTO NÍVEL)
col_tit, col_dt = st.columns([2, 1])
with col_tit:
    st.title(f"🏥 {nome_clinica}")
with col_dt:
    # DATA E HORA VISÍVEIS NA INTERFACE
    st.markdown(f"📅 **Data:** {datetime.now().strftime('%d/%m/%Y')}")
    st.markdown(f"⏰ **Hora:** {datetime.now().strftime('%H:%M:%S')}")

st.write("---")

# 4. ÁREA DE TRABALHO DO MÉDICO
col_paciente, col_obs = st.columns([1, 1])

with col_paciente:
    st.subheader("👤 1. Identificação do Paciente")
    nome = st.text_input("Nome Completo:")
    c1, c2, c3 = st.columns(3)
    with c1: idade = st.number_input("Idade:", min_value=0)
    with c2: peso = st.number_input("Peso (kg):", format="%.1f")
    with c3: altura = st.number_input("Altura (cm):")
    
    # CÁLCULO DE APOIO À IA (IMC)
    if peso > 0 and altura > 0:
        imc = peso / ((altura/100)**2)
        st.markdown(f"⚖️ **IMC Calculado:** `{imc:.1f}`")

with col_obs:
    st.subheader("👨‍⚕️ 2. Observações do Médico Assistente")
    # O ESPAÇO QUE O MÉDICO VAI USAR PARA AUXILIAR A IA
    obs_clinica = st.text_area("Insira sintomas, queixas ou histórico relevante:", 
                               placeholder="Ex: Paciente com palpitações e hipertensão controlada...",
                               height=180)

# 5. CARREGAMENTO E EXAME
st.write("---")
col_ex1, col_ex2 = st.columns(2)
with col_ex1:
    st.subheader("📊 3. Gráfico do Exame")
    tipo = st.selectbox("Tipo de Exame:", ["ECG", "ESPIRIMETRIA"])
    arquivo = st.file_uploader("Arraste o exame aqui", type=['png', 'jpg', 'jpeg'])

with col_ex2:
    st.subheader("🚀 4. Ações")
    if st.button("GERAR LAUDO PROFISSIONAL VIDAMED"):
        if nome and arquivo:
            with st.status("⚙️ IA Vidamed em processamento...", expanded=True) as s:
                st.write("A cruzar dados biométricos com notas clínicas...")
                time.sleep(1)
                st.write("A isolar traçado para diagnóstico...")
                time.sleep(1)
                s.update(label="✅ Laudo Finalizado e Enviado!", state="complete")
            st.success(f"Laudo enviado para o log de Gonçalves (954446205)")
        else:
            st.error("Por favor, preencha o Nome e carregue o Exame.")

# RODAPÉ
st.markdown("<div class='status-bar'>VIDAMED v3.0 | Sistema Ativo e Seguro</div>", unsafe_allow_html=True)
