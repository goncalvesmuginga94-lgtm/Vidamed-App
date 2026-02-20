import streamlit as st
from datetime import datetime
import time

# 1. ESTILO E CONFIGURAÇÃO
st.set_page_config(page_title="VIDAMED - Gestão por Créditos", layout="wide")

# Inicializar o saldo no sistema (Simulação - no futuro isto virá de um banco de dados)
if 'saldo_creditos' not in st.session_state:
    st.session_state.saldo_creditos = 0  # Começa a zero até tu carregares

# 2. PAINEL MASTER (O TEU COFRE)
with st.sidebar:
    st.header("🔑 GESTÃO FINANCEIRA")
    chave = st.text_input("Chave Master:", type="password")
    
    if chave == "954446205":
        st.success("Olá, Gonçalves!")
        st.subheader("💳 Carregar Créditos")
        novos_creditos = st.number_input("Adicionar exames pagos:", min_value=0, step=10)
        if st.button("Confirmar Recarga"):
            st.session_state.saldo_creditos += novos_creditos
            st.toast(f"Sucesso! +{novos_creditos} créditos adicionados.")
        
        st.write("---")
        st.metric("Saldo Atual da Clínica", f"{st.session_state.saldo_creditos} exames")
    else:
        st.info("Insira a Chave Master para gerir o saldo.")

# 3. INTERFACE DA CLÍNICA
st.title("🩺 Portal VIDAMED")

# MOSTRADOR DE SALDO PARA A CLÍNICA
if st.session_state.saldo_creditos <= 5 and st.session_state.saldo_creditos > 0:
    st.warning(f"⚠️ SALDO BAIXO: Restam apenas {st.session_state.saldo_creditos} exames.")
elif st.session_state.saldo_creditos == 0:
    st.error("🛑 SALDO ESGOTADO: Contacte a administração para recarregar créditos.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Paciente")
    nome = st.text_input("Nome Completo:")
    idade = st.number_input("Idade:", min_value=0)
    tipo = st.selectbox("Exame:", ["ECG", "ESPIRIMETRIA"])
    foto = st.file_uploader("Upload do Gráfico")

with col2:
    st.subheader("👨‍⚕️ Espaço do Médico")
    obs = st.text_area("Observações Clínicas:", height=150)
    
    # O BOTÃO SÓ FUNCIONA SE HOUVER SALDO
    pode_gerar = st.session_state.saldo_creditos > 0
    
    if st.button("🚀 GERAR LAUDO", disabled=not pode_gerar):
        if nome and foto:
            # CONSOME O CRÉDITO
            st.session_state.saldo_creditos -= 1
            
            with st.status("Validando crédito e processando...") as s:
                time.sleep(2)
                s.update(label="✅ Laudo Concluído!", state="complete")
            
            st.success(f"Laudo gerado. Saldo restante: {st.session_state.saldo_creditos}")
        else:
            st.error("Preencha os dados e carregue o exame.")

st.write("---")
st.caption(f"ID da Licença: CAVI-2026 | Gestor: Gonçalves Muginga")
