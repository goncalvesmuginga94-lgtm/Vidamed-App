import streamlit as st
from datetime import date, datetime, timedelta

st.set_page_config(page_title="SOCIAL MED | Gestão de Relacionamento", page_icon="●", layout="wide")

# Protótipo navegável com dados fictícios. Não ligar a dados reais antes de implementar
# autenticação, autorização, persistência segura e políticas RLS no backend.

st.markdown("""
<style>
:root { color-scheme: light; }
.stApp { background: #f5f7fa; color: #182230; }
[data-testid="stSidebar"] { background: #101c2c; }
[data-testid="stSidebar"] * { color: #f7f9fc !important; }
.block-container { padding-top: 1.7rem; max-width: 1500px; }
.hero { background: linear-gradient(120deg,#10243b,#174a5b); padding: 1.5rem 1.8rem;
        border-radius: 18px; color: white; margin-bottom: 1.2rem; }
.hero h1 { color: white; margin: 0; font-size: 2rem; }
.hero p { color: #d6e5ec; margin: .45rem 0 0; }
.metric { background: white; border: 1px solid #e4eaf0; border-radius: 14px;
          padding: 1rem 1.1rem; min-height: 112px; }
.metric small { color: #687789; }
.metric h2 { margin: .25rem 0; color: #14283d; }
.pill { display:inline-block; padding: .2rem .6rem; border-radius: 99px;
        background:#e7f4f1; color:#17695c; font-size:.78rem; }
div.stButton > button[kind="primary"] { background:#0e756c; border-color:#0e756c; }
</style>
""", unsafe_allow_html=True)

if "patients" not in st.session_state:
    st.session_state.patients = [
        {"id":"P-1001","name":"Ana Manuel","phone":"+244 9XX XXX 101","program":"Acompanhamento contínuo","status":"Activo","last_contact":date.today()-timedelta(days=4),"consent":"WhatsApp e telefone"},
        {"id":"P-1002","name":"Paulo António","phone":"+244 9XX XXX 202","program":"Bem-estar e continuidade","status":"Activo","last_contact":date.today()-timedelta(days=18),"consent":"Telefone"},
        {"id":"P-1003","name":"Marta Joaquim","phone":"+244 9XX XXX 303","program":"Acompanhamento contínuo","status":"Pendente","last_contact":date.today()-timedelta(days=27),"consent":"Sem consentimento activo"},
        {"id":"P-1004","name":"José Pedro","phone":"+244 9XX XXX 404","program":"Bem-estar e continuidade","status":"Activo","last_contact":date.today()-timedelta(days=2),"consent":"WhatsApp"},
    ]
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"title":"Confirmar disponibilidade para próximo atendimento","patient":"Paulo António","owner":"Equipa de atendimento","due":date.today(),"status":"Pendente"},
        {"title":"Actualizar preferência de contacto","patient":"Marta Joaquim","owner":"Coordenador","due":date.today()+timedelta(days=1),"status":"Pendente"},
        {"title":"Registar resultado do contacto","patient":"Ana Manuel","owner":"Equipa de atendimento","due":date.today()-timedelta(days=1),"status":"Concluída"},
    ]
if "interactions" not in st.session_state:
    st.session_state.interactions = [
        {"date":date.today()-timedelta(days=2),"patient":"Ana Manuel","channel":"WhatsApp","result":"Contacto realizado","owner":"Equipa de atendimento"},
        {"date":date.today()-timedelta(days=5),"patient":"José Pedro","channel":"Telefone","result":"Próximo passo combinado","owner":"Coordenador"},
    ]

with st.sidebar:
    st.markdown("## SOCIAL MED")
    st.caption("Plataforma de relacionamento e continuidade")
    st.divider()
    page = st.radio("NAVEGAÇÃO", ["Visão geral","Pacientes","Programas","Tarefas","Interacções","Consentimentos","Campanhas e conteúdos","Relatórios","Subscrição","Configurações"], label_visibility="collapsed")
    st.divider()
    st.caption("WORKSPACE DE DEMONSTRAÇÃO")
    st.info("Clínica Exemplo Luanda\n\nDados exclusivamente fictícios.")
    st.caption("MVP • Angola")

st.markdown('<div class="hero"><h1>SOCIAL MED</h1><p>Relacionamento, fidelização e continuidade no acompanhamento dos pacientes.</p></div>', unsafe_allow_html=True)
st.warning("Protótipo de demonstração: os dados são fictícios e guardados apenas na sessão. Autenticação, base de dados, RLS, pagamentos e mensagens externas ainda não estão ligados.")

patients = st.session_state.patients
tasks = st.session_state.tasks

if page == "Visão geral":
    overdue = sum(1 for t in tasks if t["status"] == "Pendente" and t["due"] < date.today())
    pending = sum(1 for t in tasks if t["status"] == "Pendente")
    active = sum(1 for p in patients if p["status"] == "Activo")
    c = st.columns(4)
    metrics = [("Pacientes na carteira",len(patients)),("Acompanhamentos activos",active),("Tarefas pendentes",pending),("Tarefas em atraso",overdue)]
    for col,(label,value) in zip(c,metrics):
        col.markdown(f'<div class="metric"><small>{label}</small><h2>{value}</h2><small>Dados de demonstração</small></div>',unsafe_allow_html=True)
    st.subheader("Prioridades operacionais")
    attention = [p for p in patients if (date.today()-p["last_contact"]).days >= 14 or p["status"] != "Activo"]
    if attention:
        st.dataframe([{"Paciente":p["name"],"Programa":p["program"],"Último contacto":p["last_contact"].strftime("%d/%m/%Y"),"Estado":p["status"],"Consentimento":p["consent"]} for p in attention],use_container_width=True,hide_index=True)
    else: st.success("Não existem prioridades operacionais na demonstração.")
    st.subheader("Próximas tarefas")
    st.dataframe([{"Tarefa":t["title"],"Paciente":t["patient"],"Responsável":t["owner"],"Prazo":t["due"].strftime("%d/%m/%Y"),"Estado":t["status"]} for t in tasks],use_container_width=True,hide_index=True)

elif page == "Pacientes":
    st.subheader("Gestão de pacientes")
    with st.expander("＋ Registar paciente de demonstração",expanded=False):
        with st.form("new_patient"):
            name=st.text_input("Nome")
            phone=st.text_input("Contacto")
            program=st.selectbox("Programa",["Acompanhamento contínuo","Bem-estar e continuidade","Programa personalizado"])
            consent=st.selectbox("Preferência/consentimento registado",["Pendente de registo","Telefone","WhatsApp","WhatsApp e telefone","Sem consentimento activo"])
            submitted=st.form_submit_button("Adicionar à demonstração",type="primary")
            if submitted:
                if name.strip():
                    st.session_state.patients.append({"id":f"P-{1000+len(st.session_state.patients)+1}","name":name.strip(),"phone":phone,"program":program,"status":"Pendente","last_contact":date.today(),"consent":consent})
                    st.success("Registo adicionado apenas à sessão de demonstração.")
                    st.rerun()
                else: st.error("Indique o nome.")
    st.dataframe([{"ID":p["id"],"Paciente":p["name"],"Contacto":p["phone"],"Programa":p["program"],"Estado":p["status"],"Último contacto":p["last_contact"].strftime("%d/%m/%Y"),"Preferência":p["consent"]} for p in patients],use_container_width=True,hide_index=True)

elif page == "Programas":
    st.subheader("Programas de acompanhamento")
    st.write("Organize iniciativas de continuidade e relacionamento definidas e aprovadas por cada clínica.")
    for name,desc,count in [("Acompanhamento contínuo","Rotinas operacionais de contacto e apoio à marcação.",2),("Bem-estar e continuidade","Comunicação de continuidade e informação institucional aprovada.",2)]:
        with st.container(border=True):
            st.markdown(f"### {name}")
            st.write(desc)
            st.caption(f"{count} participantes fictícios • Estado: demonstração")

elif page == "Tarefas":
    st.subheader("Fila de trabalho")
    with st.expander("＋ Criar tarefa"):
        with st.form("new_task"):
            title=st.text_input("Descrição da tarefa")
            patient=st.selectbox("Paciente", [p["name"] for p in patients])
            owner=st.text_input("Responsável",value="Equipa de atendimento")
            due=st.date_input("Prazo",value=date.today())
            if st.form_submit_button("Criar tarefa",type="primary"):
                if title.strip():
                    st.session_state.tasks.append({"title":title.strip(),"patient":patient,"owner":owner,"due":due,"status":"Pendente"})
                    st.success("Tarefa criada nesta sessão.")
                    st.rerun()
    for i,t in enumerate(st.session_state.tasks):
        with st.container(border=True):
            left,right=st.columns([4,1])
            left.markdown(f"**{t['title']}**")
            left.caption(f"{t['patient']} • {t['owner']} • Prazo: {t['due'].strftime('%d/%m/%Y')}")
            right.write(t["status"])
            if t["status"]=="Pendente" and right.button("Concluir",key=f"done_{i}"):
                st.session_state.tasks[i]["status"]="Concluída"
                st.rerun()

elif page == "Interacções":
    st.subheader("Histórico de interacções")
    with st.expander("＋ Registar contacto"):
        with st.form("new_interaction"):
            patient=st.selectbox("Paciente", [p["name"] for p in patients])
            channel=st.selectbox("Canal",["Telefone","WhatsApp","Presencial","Email"])
            result=st.selectbox("Resultado",["Contacto realizado","Sem resposta","Próximo passo combinado","Encaminhado para equipa clínica"])
            owner=st.text_input("Responsável",value="Equipa de atendimento")
            if st.form_submit_button("Registar interacção",type="primary"):
                p=next(x for x in patients if x["name"]==patient)
                if channel in p["consent"] or channel=="Presencial":
                    st.session_state.interactions.insert(0,{"date":date.today(),"patient":patient,"channel":channel,"result":result,"owner":owner})
                    p["last_contact"]=date.today()
                    st.success("Interacção registada nesta sessão.")
                    st.rerun()
                else: st.error("A preferência/consentimento apresentado não autoriza este canal. Confirme o registo antes de contactar.")
    st.dataframe([{"Data":x["date"].strftime("%d/%m/%Y"),"Paciente":x["patient"],"Canal":x["channel"],"Resultado":x["result"],"Responsável":x["owner"]} for x in st.session_state.interactions],use_container_width=True,hide_index=True)

elif page == "Consentimentos":
    st.subheader("Preferências e consentimentos")
    st.write("O consentimento deve ser registado por canal, com data, versão do texto e prova de recolha no backend definitivo.")
    st.dataframe([{"Paciente":p["name"],"Preferência registada":p["consent"],"Estado":("Requer validação" if "Sem consentimento" in p["consent"] or "Pendente" in p["consent"] else "Registo de demonstração")} for p in patients],use_container_width=True,hide_index=True)

elif page == "Campanhas e conteúdos":
    st.subheader("Campanhas e conteúdos aprovados")
    st.info("Nesta fase é possível planear e pré-visualizar conteúdos. O envio real de WhatsApp, SMS ou email está desactivado até existir fornecedor configurado, consentimentos validados e registo de entrega.")
    st.selectbox("Estado da campanha",["Rascunho","Em revisão","Aprovada para configuração"])
    st.text_area("Conteúdo da mensagem",placeholder="Escreva conteúdo institucional aprovado pela clínica.")
    st.button("Guardar rascunho",disabled=True,help="Persistência será activada com o backend.")

elif page == "Relatórios":
    st.subheader("Indicadores operacionais")
    st.caption("Valores derivados exclusivamente dos registos fictícios desta sessão.")
    st.metric("Interacções registadas",len(st.session_state.interactions))
    st.metric("Tarefas concluídas",sum(1 for t in tasks if t["status"]=="Concluída"))
    st.metric("Pacientes com preferência por WhatsApp",sum(1 for p in patients if "WhatsApp" in p["consent"]))
    st.info("Relatórios avançados, exportações autorizadas e métricas agregadas serão ligados ao backend após implementação das permissões.")

elif page == "Subscrição":
    st.subheader("Planos e subscrição")
    st.write("Estrutura comercial preparada para o modelo SaaS da SOCIAL MED. Nenhum pagamento é cobrado nesta demonstração.")
    cols=st.columns(3)
    plans=[("Starter","Para clínicas pequenas","1 unidade • equipa essencial"),("Professional","Para clínicas em crescimento","Mais utilizadores • relatórios avançados"),("Enterprise","Para grupos e redes","Multiunidade • configuração contratual")]
    for col,(name,desc,features) in zip(cols,plans):
        with col.container(border=True):
            st.markdown(f"### {name}")
            st.write(desc)
            st.caption(features)
            st.button("Plano de demonstração",key=f"plan_{name}",disabled=True)
    st.warning("Preços em AOA, facturação, renovação, período de teste e gateway de pagamento carecem de configuração comercial e integração aprovadas.")

elif page == "Configurações":
    st.subheader("Configurações da clínica")
    st.text_input("Nome da organização",value="Clínica Exemplo Luanda",disabled=True)
    st.selectbox("Idioma principal",["Português"],disabled=True)
    st.selectbox("Fuso horário",["Africa/Luanda"],disabled=True)
    st.info("Gestão de membros, funções, identidade visual, políticas de retenção e auditoria serão activadas com autenticação e backend seguros.")

st.divider()
st.caption(f"SOCIAL MED © {date.today().year} • Protótipo funcional de interface • {datetime.now().strftime('%d/%m/%Y %H:%M')}")
