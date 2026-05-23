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

```txt
pytest
pytest-flask
