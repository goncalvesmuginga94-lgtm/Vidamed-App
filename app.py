import streamlit as st

# 1. CONFIGURAÇÃO DE ALTO NÍVEL (LOGO E MARCA DE ÁGUA)
st.set_page_config(page_title="VIDAMED - Portal Profissional", layout="wide")

# Estilo para o Logo (Canto Superior Esquerdo) e Marca de Água (Quase invisível no fundo)
st.markdown("""
    <style>
    .main {
        background-image: url('URL_DO_TEU_LOGO'); /* Aqui colocaremos o teu logo depois */
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.05; /* Marca de água quase invisível */
    }
    .logo-img {
        position: absolute;
        top: 0px;
        left: 0px;
        width: 150px; /* Tamanho médio e nítido */
    }
    </style>
    """, unsafe_allow_status=True)

# 2. CONTROLO DE AUTORIDADE E PAGAMENTO
def verificar_pagamento(clinica):
    # Regra: Se a clínica não pagar, tu alteras aqui para False e o sistema bloqueia
    status_pagamento = True 
    return status_pagamento

# 3. INTERFACE DO SISTEMA
st.title("🩺 VIDAMED - Sistema de Gestão de Exames")
st.sidebar.header("CONTROLO DE ACESSO")
clinica_nome = st.sidebar.text_input("Nome da Clínica/Centro:", value="Centro Médico Cavi")

if not verificar_pagamento(clinica_nome):
    st.error("⚠️ ACESSO BLOQUEADO: Entre em contacto com o Administrador (Gonçalves Muginga).")
    st.stop()

# 4. ENTRADA MANUAL (REGRA DE SEGURANÇA)
st.subheader("📝 Identificação do Paciente (Entrada Manual Obrigatória)")
col1, col2 = st.columns(2)
with col1:
    nome_paciente = st.text_input("Nome Completo do Paciente:")
with col2:
    idade_paciente = st.number_input("Idade do Paciente:", min_value=0, max_value=120)

# 5. SELEÇÃO DE EXAME E SINAL
st.subheader("📁 Processamento de Exame")
tipo_exame = st.selectbox("Selecione o Exame:", ["ECG", "ESPIRIMETRIA", "IMAGIOLOGIA"])
whatsapp_envio = st.text_input("WhatsApp para envio do Laudo (Log):")

arquivo = st.file_uploader("Carregar imagem do exame/gráfico", type=['png', 'jpg', 'jpeg', 'pdf'])

if st.button("GERAR LAUDO PROFISSIONAL"):
    if nome_paciente and arquivo:
        # Aqui o sistema vai processar usando o sinal "ECG" ou "ESPIRIMETRIA"
        st.success(f"A processar {tipo_exame} para o paciente {nome_paciente}...")
        st.info(f"Log: Resultado será enviado para {whatsapp_envio}")
        
        if tipo_exame == "ESPIRIMETRIA":
            st.info("🔄 Formatação em Quadrado Ativada (Sinal: ESPIRIMETRIA)")
    else:
        st.warning("Por favor, preencha o Nome e carregue o exame.")

st.sidebar.write("---")
st.sidebar.write(f"📊 Contador de Exames: 124 (Fevereiro/2026)")
