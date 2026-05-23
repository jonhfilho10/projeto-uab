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

```txt
pytest
pytest-flask