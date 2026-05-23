# Plano de Testes — Sistema de Gestão para Projeto Social Esportivo

## 1. Objetivo

Este documento define o plano de testes do Sistema de Gestão para Projeto Social Esportivo, com foco em TDD First, automação de testes e prevenção de regressões.

## 2. Estratégia de Testes

A estratégia será baseada em testes automatizados utilizando `pytest` e `pytest-flask`.

Os testes devem validar:

- autenticação;
- permissões;
- CRUD de modalidades;
- CRUD de participantes;
- controle de vagas;
- CRUD de usuários;
- dashboard;
- relatórios;
- exportação;
- validações de dados;
- respostas JSON.

## 3. Dependências Necessárias

Adicionar ao `requirements.txt`:

## Testes de Refatoração e Otimização

### CT-031 — Validar carregamento do dashboard após refatoração
O sistema deve continuar exibindo corretamente indicadores e gráficos.

### CT-032 — Validar permissões após refatoração
Usuários sem perfil administrador não devem acessar áreas administrativas.

### CT-033 — Validar relatórios após otimização
Relatórios devem continuar carregando dados, filtros e exportação.

### CT-034 — Validar controle de vagas
O sistema deve impedir cadastro de participantes quando a modalidade atingir o limite.

# Testes de Frontend e Usabilidade

## CT-035 — Validar tela de login responsiva

O sistema deve exibir a tela de login corretamente em desktop, tablet e mobile.

Resultado esperado:
- campos alinhados;
- botão visível;
- layout centralizado;
- mensagens de erro funcionando.

---

## CT-036 — Validar feedback de carregamento

O sistema deve exibir loading/spinner durante requisições JSON.

Resultado esperado:
- loading aparece antes dos dados;
- loading desaparece após resposta da API;
- conteúdo é exibido corretamente.

---

## CT-037 — Validar mensagens de erro visuais

O sistema deve exibir mensagens de erro em modal padronizado.

Resultado esperado:
- erro aparece de forma clara;
- modal não quebra o fluxo do formulário;
- usuário consegue corrigir os dados.

---

## CT-038 — Validar estados vazios

O sistema deve exibir mensagens quando não houver registros cadastrados.

Resultado esperado:
- tabelas vazias mostram mensagem amigável;
- não ocorre erro de renderização.

---

## CT-039 — Validar filtros dos relatórios

O sistema deve permitir filtrar participantes por modalidade e status.

Resultado esperado:
- filtros retornam dados corretos;
- botão limpar restaura a listagem completa.

---

## CT-040 — Validar dashboard com gráfico

O dashboard deve renderizar indicadores, tabela e gráfico de participantes por modalidade.

Resultado esperado:
- cards carregam dados reais;
- gráfico é exibido corretamente;
- tabela de ocupação é preenchida.

---

## CT-041 — Validar navegação do menu

O menu lateral deve permitir acesso às principais telas do sistema.

Resultado esperado:
- links funcionam;
- rotas protegidas exigem login;
- áreas restritas respeitam perfil de usuário.

---

## CT-042 — Validar responsividade das tabelas e formulários

As telas de participantes, modalidades, usuários e relatórios devem manter usabilidade em diferentes tamanhos de tela.

Resultado esperado:
- campos continuam acessíveis;
- botões permanecem visíveis;
- conteúdo não quebra a navegação.

---

## CT-043 — Validar integração frontend/backend

As telas devem consumir APIs JSON corretamente.

Resultado esperado:
- cadastro, edição, exclusão e listagens funcionam via fetch;
- respostas de erro são exibidas ao usuário;
- dados são atualizados sem recarregar a página.


```txt
pytest
pytest-flask
