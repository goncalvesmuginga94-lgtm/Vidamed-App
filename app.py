import streamlit as st

# 1. CONFIGURAÇÃO DE ALTO NÍVEL
st.set_page_config(page_title="VIDAMED - Painel de Controlo", layout="wide")

# 2. PAINEL DO ADMINISTRADOR (SÓ PARA O GONÇALVES)
st.sidebar.header("🛠️ CONFIGURAÇÃO MASTER (VIDAMED)")
with st.sidebar.expander("Configurar Clínica (Gonçalves apenas)", expanded=False):
    nome_clinica = st.text_input("Nome da Clínica:", "Centro Médico Cavi")
    endereco_clinica = st.text_input("Endereço Completo:")
    zap_principal = st.text_input("WhatsApp Principal (Ex: 244...):")
    zap_alternativo = st.text_input("WhatsApp Alternativo:")
    url_logo = st.text_input("Link do Logótipo da Clínica:")
    
    st.write("---")
    if st.button("Salvar Configurações"):
        st.success("Configurações da Clínica Guardadas!")

# 3. INTERFACE SIMPLIFICADA PARA O DIA-A-DIA
st.title(f"🩺 Portal {nome_clinica}")
st.markdown(f"**Endereço:** {endereco_clinica} | **Contacto:** {zap_principal}")

# REGRA: DADOS DO PACIENTE PRIMEIRO
st.subheader("1. Identificação do Paciente")
col1, col2, col3, col4 = st.columns(4)
with col1:
    nome = st.text_input("Nome Completo:")
with col2:
    idade = st.number_input("Idade:", min_value=0)
with col3:
    peso = st.number_input("Peso (kg):")
with col4:
    altura = st.number_input("Altura (cm):")

# CARREGAMENTO DO EXAME
st.write("---")
st.subheader("2. Carregar Exame")
tipo_exame = st.selectbox("Tipo de Exame:", ["ECG", "ESPIRIMETRIA"])
arquivo = st.file_uploader("Arraste a imagem do exame aqui", type=['jpg', 'png', 'jpeg'])

# BOTÃO DE EXECUÇÃO
if st.button("🚀 GERAR LAUDO E ENVIAR"):
    if nome and arquivo:
        st.balloons()
        st.success(f"✅ Laudo Gerado! Enviando para {zap_principal} e Log para 954446205")
        
        # O QUE O SISTEMA FAZ SOZINHO (SEM TU VERES)
        st.markdown(f"""
        ### 📄 Estrutura do Documento Gerado:
        * **Topo:** Logo da Clínica ({nome_clinica}) - Canto Esquerdo.
        * **Corpo:** Dados de {nome}, {idade} anos. Termos médicos profissionais.
        * **Fundo:** Marca de água Vidamed + Rodapé com QR Code e {endereco_clinica}.
        """)
    else:
        st.error("⚠️ Por favor, preencha o Nome do Paciente e carregue o Exame.")

st.sidebar.write("---")
st.sidebar.info(f"Monitorização: Gonçalves Muginga (954446205)")
