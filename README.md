# SOCIAL MED — Plataforma de Relacionamento e Continuidade

A SOCIAL MED é uma plataforma SaaS institucional para clínicas e unidades de saúde em Angola, focada na organização do relacionamento, fidelização e continuidade do acompanhamento dos pacientes.

> **Limite do produto:** SOCIAL MED não é um sistema clínico nem substitui o software oficial da clínica. Não gere diagnósticos, exames, prescrições, medicação, medições clínicas ou prontuários.

## Estado actual

Este repositório contém um **protótipo navegável em Streamlit**, com dados fictícios guardados apenas na sessão:
- Visão geral e prioridades operacionais;
- Registo demonstrativo de pacientes;
- Programas de acompanhamento;
- Fila de tarefas;
- Histórico de interacções;
- Preferências/consentimentos por canal;
- Planeamento de campanhas e conteúdos;
- Indicadores operacionais;
- Estrutura demonstrativa de planos SaaS.

Não estão implementados neste protótipo: autenticação real, persistência, multi-tenancy seguro, políticas RLS, faturação, gateway de pagamentos, envio de mensagens, integração clínica ou sincronização Databricks. Os botões e estados não devem ser interpretados como operações de produção.

## Executar localmente

Requisitos: Python 3.10 ou superior.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

## Direcção de arquitectura aprovada

- Mercado inicial: Angola.
- Marca institucional: **SOCIAL MED**.
- Frontend de produto pretendido: Lovable.
- Autenticação e base operacional: Supabase.
- Segurança: isolamento multi-tenant, RBAC, RLS e auditoria.
- Subscrições: fazem parte do produto desde o início; pagamentos reais só após escolha e configuração do fornecedor.
- Databricks: camada analítica futura, não dependência operacional do MVP.
- Desenvolvimento e demonstração: apenas dados fictícios até aprovação formal de segurança.

Ver [docs/PRODUCT_BLUEPRINT.md](docs/PRODUCT_BLUEPRINT.md) para o plano de implementação e requisitos.

## Segurança — acções obrigatórias antes de produção

1. Não introduzir dados reais de pacientes nesta demonstração.
2. Implementar autenticação e autorização no backend; esconder elementos na interface não é controlo de acesso.
3. Activar RLS em todas as tabelas expostas e testar acessos cruzados entre clínicas.
4. Guardar segredos apenas em ambiente de servidor/Edge Functions.
5. Definir retenção, eliminação, backups, resposta a incidentes e obrigações contratuais/legais com aconselhamento adequado.
6. Não activar campanhas nem integrações sem fornecedor, consentimentos válidos e registos verificáveis.

## Fases propostas

1. Validar experiência e fluxos com dados fictícios.
2. Aprovar modelo de dados, permissões e políticas RLS.
3. Implementar autenticação, tenants, memberships e auditoria no Supabase.
4. Implementar fluxos operacionais e testes de isolamento.
5. Implementar planos, subscrições e facturação.
6. Só depois configurar canais de comunicação externos e relatórios.
7. Preparar pipeline analítico Databricks quando existir necessidade, base legal, fonte e aprovação.

## Nota de implementação

O protótipo Streamlit é uma etapa de validação visual/funcional, não a arquitectura final multi-tenant. A transição para Lovable + Supabase deve ser feita de forma explícita, com migrations versionadas e testes automatizados.
