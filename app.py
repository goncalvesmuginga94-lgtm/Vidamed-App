import streamlit as st

# 1. CONFIGURAÇÃO BÁSICA
st.set_page_config(page_title="VIDAMED", layout="wide")

# 2. TÍTULO E SEGURANÇA (NOME MANUAL)
st.title("🩺 VIDAMED - Gestão de Exames")

st.sidebar.header("CONTROLO")
clinica = st.sidebar.text_input("Clínica:", value="Centro Médico Cavi")

# REGRA DE OURO: Nome e Idade inseridos por ti
st.subheader("📝 Dados do Paciente")
nome_paciente = st.text_input("Digite o Nome Completo:")
idade_paciente = st.number_input("Digite a Idade:", min_value=0)

# 3. SELEÇÃO DE EXAME
tipo_exame = st.selectbox("Tipo de Exame:", ["ECG", "ESPIRIMETRIA", "IMAGIOLOGIA"])
arquivo = st.file_uploader("Carregar Imagem do Exame", type=['png', 'jpg', 'jpeg'])

if st.button("GERAR LAUDO PROFISSIONAL"):
    if nome_paciente and arquivo:
        st.success(f"Laudo de {tipo_exame} em processamento para {nome_paciente}...")
        # Aqui o sistema já sabe que deve usar o sinal "ECG" ou "ESPIRIMETRIA"
    else:
        st.error("Por favor, digite o nome e carregue o ficheiro.")

st.sidebar.write("---")
st.sidebar.write("✅ Sistema Ativo e Seguro")
