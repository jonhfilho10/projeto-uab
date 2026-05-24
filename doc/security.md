# Relatório de Inspeção de Segurança

## Sistema
Sistema de Gestão para Projeto Social Esportivo

## Objetivo
Realizar inspeção de segurança no projeto, considerando boas práticas de desenvolvimento seguro e OWASP Top 10.

## Escopo Avaliado
- app/controllers/
- app/templates/
- app/utils/
- app/database/
- requirements.txt
- .env
- run.py

---

# Resumo Executivo

| Severidade | Quantidade |
|---|---:|
| Crítica | 0 |
| Alta | 2 |
| Média | 5 |
| Baixa | 3 |

---

# 5 Ações Mais Urgentes

1. Implementar criptografia/hash de senhas.
2. Remover chave secreta fixa do código e usar variável de ambiente.
3. Configurar cookies de sessão com proteção.
4. Adicionar proteção contra CSRF em formulários.
5. Criar logs de segurança para ações administrativas.

---

# Achados de Segurança

## 1. Senhas armazenadas sem criptografia

**Severidade:** Alta  
**Categoria OWASP:** A04 Cryptographic Failures / A07 Authentication Failures  
**Local:** controllers de usuários e autenticação  

### Descrição
O sistema utiliza senha simples no cadastro e login de usuários. Isso representa risco caso o banco de dados seja acessado indevidamente.

### Impacto
Exposição direta das senhas dos usuários.

### Recomendação
Utilizar hash seguro com `werkzeug.security`.

```python
from werkzeug.security import generate_password_hash, check_password_hash

senha_hash = generate_password_hash(senha)
check_password_hash(senha_hash, senha_digitada)
