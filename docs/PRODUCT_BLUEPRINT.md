# SOCIAL MED — Product Blueprint v1.0

## 1. Visão do produto

A SOCIAL MED é uma plataforma SaaS institucional para clínicas e unidades de saúde em Angola. O seu propósito é melhorar a organização do relacionamento com pacientes, a continuidade do acompanhamento, a fidelização e a eficiência operacional das equipas.

A plataforma responde a perguntas como:
- Que pacientes precisam de contacto de seguimento?
- Quem está há demasiado tempo sem contacto, segundo regras operacionais configuradas?
- Quem precisa de ajuda para marcar ou confirmar o próximo atendimento?
- Que contactos foram feitos, por quem e com que resultado?
- Que conteúdos institucionais/educativos aprovados podem ser partilhados?
- Como evoluem os indicadores de continuidade e relacionamento?

### Limites clínicos inegociáveis

A SOCIAL MED não diagnostica, prescreve, interpreta sintomas, calcula risco clínico nem recomenda alterações de tratamento. Não duplica exames, medições, consultas, prescrições, medicação ou prontuários. Se uma comunicação indicar necessidade de avaliação clínica, a equipa deve seguir o protocolo de encaminhamento definido pela clínica.

## 2. Marca e experiência

- Marca da plataforma: **SOCIAL MED** (duas palavras).
- Posicionamento: institucional, profissional, humano, confiável e discreto.
- Mercado inicial: Angola.
- Idioma inicial: português claro, preparado para internacionalização posterior.
- Identidade visual: azul-marinho, teal, branco e cinzas; contraste acessível e hierarquia clara.
- A marca da plataforma mantém-se visível; cada clínica poderá configurar elementos próprios sem substituir a identidade institucional.
- Não inventar logótipos oficiais, certificações, integrações ou conformidade legal.

## 3. Modelo SaaS e subscrições

As subscrições fazem parte do produto desde o início. Preparar:
- Catálogo de planos: Starter, Professional e Enterprise.
- Ciclo de subscrição, estado, datas de início/renovação e período de teste, quando aprovado.
- Limites e funcionalidades por plano.
- Histórico de alterações e eventos de facturação.
- Gestão de cancelamento, suspensão, atraso e reactivação.
- Área de administração SOCIAL MED para gerir organizações e estado comercial sem acesso por defeito aos dados operacionais dos pacientes.

**Pendente antes de cobrar:** preços em AOA, periodicidade, regras fiscais/contratuais, período de teste, política de cancelamento e fornecedor/gateway de pagamento. Não simular pagamentos ou confirmações.

## 4. Utilizadores e permissões

- Administrador SOCIAL MED: gere tenants e subscrições; não consulta dados de pacientes por defeito.
- Administrador da clínica: gere equipa, programas, modelos, regras operacionais e relatórios da sua clínica.
- Coordenador: distribui tarefas e acompanha pendências.
- Agente de atendimento: acede apenas aos dados mínimos para executar tarefas e registar contactos.
- Profissional de saúde (opcional): recebe encaminhamentos de relacionamento estritamente necessários; sem módulo de prontuário.
- Paciente: portal fora do MVP.

Permissões são verificadas no backend e reforçadas por RLS. Ocultar botões não é autorização.

## 5. Âmbito funcional do MVP

1. Autenticação, recuperação de acesso e onboarding protegido.
2. Organizações/tenants e gestão de membros.
3. Dashboard com métricas derivadas de dados reais disponíveis.
4. Registo mínimo de pacientes e referência externa opcional.
5. Programas operacionais de acompanhamento.
6. Inscrição de pacientes em programas.
7. Consentimentos e preferências por canal, incluindo prova, versão e revogação.
8. Fila de tarefas, atribuição, prazo, estado e histórico.
9. Registo de interacções e resultados operacionais.
10. Modelos/conteúdos com revisão e aprovação.
11. Campanhas em rascunho/pré-visualização; sem envio real até integração aprovada.
12. Relatórios operacionais e exportação autorizada.
13. Subscrições, planos, limites e estado comercial.
14. Administração da plataforma e auditoria.

## 6. Modelo de dados inicial

Tabelas base propostas:
- tenants
- profiles
- tenant_memberships
- patients
- programs
- patient_program_enrollments
- communication_consents
- interactions
- follow_up_tasks
- message_templates
- campaigns
- campaign_recipients / message_delivery_logs
- audit_logs
- subscription_plans
- tenant_subscriptions
- subscription_events
- plan_entitlements

Usar UUIDs, timestamps, constraints/enums e tenant_id nas entidades pertencentes a uma clínica. Não guardar palavras-passe em profiles. Definir chaves estrangeiras e índices de acordo com os padrões de consulta.

## 7. Segurança, privacidade e governação

- RLS activa em todas as tabelas expostas pela API.
- Acesso por associação activa a tenant e função permitida.
- Negação por defeito; políticas SELECT/INSERT/UPDATE/DELETE avaliadas separadamente.
- Nunca confiar em tenant_id fornecido pelo frontend sem validação backend.
- Impedir acesso cruzado via joins, RPCs, Edge Functions, ficheiros e exportações.
- service_role apenas no servidor; nunca no browser ou repositório.
- Auditoria de acções relevantes sem copiar conteúdo sensível integral.
- Consentimento de comunicação por canal, com revogação efectiva. Consentimento de comunicação não deve ser confundido automaticamente com fundamento jurídico para todo o tratamento de dados.
- Minimização de dados; dados fictícios em desenvolvimento.
- Definir retenção, eliminação, backups, recuperação, MFA, resposta a incidentes e contratos com orientação jurídica e de segurança adequada ao mercado.

### Testes de aceitação de segurança

Criar pelo menos duas clínicas de teste e utilizadores distintos. Demonstrar que um utilizador de A não consegue ler, inserir, actualizar, apagar, exportar ou inferir dados de B, incluindo por IDs alterados, RPCs e Edge Functions. Testar utilizadores sem membership, membership suspensa e funções sem permissão.

## 8. Arquitectura

### Operação
- Frontend: Lovable.
- Autenticação e base operacional: Supabase.
- Operações privilegiadas: Supabase Edge Functions ou backend seguro.
- Software clínico oficial da clínica continua a ser a fonte dos registos clínicos.
- Integrações isoladas por interfaces; não presumir que as clínicas dispõem de APIs.

### Analítica futura
Databricks não é dependência do MVP.
- Bronze: eventos mínimos, rastreáveis, com metadados e controlo de qualidade.
- Silver: normalização, deduplicação, validação e pseudonimização.
- Gold: métricas agregadas de continuidade e relacionamento, com protecção contra reidentificação.
- Não copiar prontuários clínicos.
- Não afirmar sincronização enquanto não existir pipeline testado e aprovado.

## 9. Ecrãs principais

- Login e recuperação de acesso.
- Onboarding da clínica.
- Dashboard.
- Pacientes e ficha mínima de relacionamento.
- Programas e inscrições.
- Fila de tarefas.
- Histórico de interacções.
- Consentimentos e preferências.
- Biblioteca de conteúdos aprovados.
- Campanhas.
- Relatórios/exportações.
- Membros e permissões.
- Subscrição e plano.
- Configurações da clínica.
- Administração SOCIAL MED.

Todos os ecrãs devem prever estados vazio, carregamento, erro, sucesso e ausência de permissão; responsividade desktop e móvel.

## 10. Fases de implementação

### Fase 0 — Protótipo
Validar navegação, linguagem, fluxos e hierarquia visual com dados fictícios. Não ligar dados reais.

### Fase 1 — Fundação segura
Criar projecto Supabase, migrations, tenants, profiles, memberships, autenticação, funções e políticas RLS. Fazer revisão de segurança e testes negativos antes de inserir dados reais.

### Fase 2 — Operação
Implementar pacientes mínimos, programas, inscrições, tarefas, interacções, consentimentos e auditoria.

### Fase 3 — Conteúdos e relatórios
Implementar aprovação de conteúdos, pré-visualização de campanhas, métricas transparentes e exportações com autorização.

### Fase 4 — Monetização
Implementar planos, entitlements, subscrições, estados comerciais e integração de pagamentos apenas após escolha e configuração do fornecedor.

### Fase 5 — Integrações e analítica
Configurar canais de comunicação com consentimentos e logs verificáveis. Preparar Databricks apenas quando houver fonte, necessidade e aprovação.

## 11. Critérios de aceitação do MVP

- Um utilizador só acede a tenants aos quais pertence e conforme a sua função.
- Testes negativos comprovam isolamento entre clínicas.
- Consentimentos por canal são respeitados antes de qualquer contacto.
- Fluxo completo: paciente mínimo → programa → tarefa → interacção → histórico.
- Tarefas filtráveis por estado, responsável e prazo.
- Dashboard não inventa números, envios ou sincronizações.
- Nenhum segredo privado no frontend.
- Não existem módulos de diagnóstico, exames, prescrição ou medicação.
- Subscrições e limites de plano têm estados rastreáveis; pagamentos não são simulados.
- Documentação de tabelas, funções, RLS, variáveis de ambiente e testes.
- Dados fictícios até aprovação de segurança e autorização formal da clínica.

## 12. Decisões ainda pendentes

- Nome legal da entidade contratante e dados fiscais.
- Preços, periodicidade e limites exactos de cada plano.
- Gateway de pagamento e meios aceites em Angola.
- Política de teste, suspensão, cancelamento, reembolso e cobrança em atraso.
- Requisitos legais e contratuais aplicáveis ao tratamento de dados e às comunicações.
- Fornecedores de WhatsApp/SMS/email e respectivos contratos.
- Política de retenção e prazos de eliminação.
- Necessidade e prioridade de integrações com sistemas clínicos existentes.

Não inventar estas decisões. Mantê-las como pendentes até validação.
