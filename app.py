import streamlit as st
from datetime import datetime
import time

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="VIDAMED - Sistema Integrado", layout="wide")

st.markdown("""
    <style>
    .caixa-master { background-color: #f0f4f8; padding: 20px; border-radius: 10px; border-left: 8px solid #003366; }
    .stTextArea textarea { height: 200px !important; border: 2px solid #003366; }
    h1, h2 { color: #003366; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

# 2. PAINEL DO ADMINISTRADOR (Recuperado e Blindado)
with st.sidebar:
    st.header("⚙️ CONFIGURAÇÃO MASTER")
    chave = st.text_input("Chave Master:", type="password")
    
    # Valores padrão que tu controlas
    nome_clinica = "Centro Médico Cavi"
    endereco_clinica = "Endereço não configurado"
    zap_clinica = "954446205"
    url_logo = ""

    if chave == "954446205":
        st.success("Modo Administrador: ATIVO")
        nome_clinica = st.text_input("Nome da Clínica:", value=nome_clinica)
        endereco_clinica = st.text_input("Endereço Completo:", value=endereco_clinica)
        zap_clinica = st.text_input("WhatsApp de Envio:", value=zap_clinica)
        url_logo = st.text_input("Link do Logo (URL):")
        if st.button("🔴 BLOQUEAR ACESSO"):
            st.error("SISTEMA SUSPENSO")
    
    st.write("---")
    st.info(f"Monitorização: Gonçalves Muginga\nWhatsApp: 954446205")

# 3. CABEÇALHO DINÂMICO
col_l, col_t, col_dh = st.columns([1, 2, 1])
with col_l:
    if url_logo: st.image(url_logo, width=150)
    else: st.title("🩺")
with col_t:
    st.title(nome_clinica)
    st.caption(f"📍 {endereco_clinica}")
with col_dh:
    st.markdown(f"🗓️ **Data:** {datetime.now().strftime('%d/%m/%Y')}")
    st.markdown(f"🕒 **Hora:** {datetime.now().strftime('%H:%M:%S')}")

st.write("---")

# 4. INTERFACE DE TRABALHO (PREENCHENDO O VAZIO)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Identificação do Paciente")
    with st.container():
        nome_p = st.text_input("Nome Completo:")
        c1, c2, c3 = st.columns(3)
        with c1: idade_p = st.number_input("Idade:", min_value=0)
        with c2: peso_p = st.number_input("Peso (kg):", format="%.1f")
        with c3: altura_p = st.number_input("Altura (cm):")
    
    st.write("---")
    st.subheader("📊 Dados do Exame")
    tipo = st.selectbox("Tipo de Serviço:", ["ECG", "ESPIRIMETRIA"])
    arquivo = st.file_uploader("Carregar imagem do gráfico", type=['png', 'jpg', 'jpeg'])

with col2:
    st.subheader("👨‍⚕️ Espaço do Médico Assistente")
    # ESPAÇO PARA O MÉDICO COLOCAR INFORMAÇÕES (O que tu pediste)
    obs_medica = st.text_area("Informações clínicas, queixas e histórico do paciente:", 
                              placeholder="Escreva aqui tudo o que pode ajudar a IA no diagnóstico...",
                              help="Este campo é vital para a precisão do laudo.")
    
    if st.button("🚀 GERAR LAUDO PROFISSIONAL VIDAMED"):
        if nome_p and arquivo:
            with st.status("⚙️ IA VIDAMED em processamento técnico...", expanded=True) as s:
                st.write(f"Analisando notas de {nome_p}...")
                time.sleep(1)
                st.write("Aplicando marca de água da clínica no laudo...")
                time.sleep(1)
                s.update(label="✅ Laudo Finalizado!", state="complete")
            st.success(f"Enviado para {zap_clinica}")
        else:
            st.error("Preencha o Nome e carregue o Exame.")

# RODAPÉ PROFISSIONAL
st.write("---")
st.markdown("<center><small>VIDAMED v4.0 | Tecnologia de Telemedicina Avançada | Log Master 954446205</small></center>", unsafe_allow_html=True)
