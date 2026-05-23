# ESPECIFICAÇÃO DO PROJETO

# Sistema de Gestão para Projeto Social Esportivo

---

# 1. Descrição Geral

O projeto consiste no desenvolvimento de um sistema web para gerenciamento de projetos sociais esportivos, permitindo o controle de participantes, modalidades esportivas, usuários, relatórios administrativos e indicadores gerenciais.

A aplicação será desenvolvida utilizando arquitetura cliente-servidor baseada no padrão MVC (Model-View-Controller), utilizando Python com framework Flask.

O sistema terá interface web responsiva, permitindo acesso por computadores, tablets e smartphones.

A aplicação será containerizada utilizando Docker e terá controle de versão através do GitHub.

O desenvolvimento contará com apoio de Inteligência Artificial, utilizando o ChatGPT como ferramenta auxiliar para geração de código, revisão, testes, documentação e melhorias.

---

# 2. Usuários do Sistema

## 2.1 Administrador

Usuário responsável pelo gerenciamento geral do sistema.

### Funcionalidades:
- Fazer login;
- Fazer logout;
- Alterar senha;
- Gerenciar atendentes;
- Gerenciar participantes;
- Gerenciar modalidades;
- Visualizar dashboard;
- Emitir relatórios gerenciais;
- Exportar relatórios;
- Consultar logs administrativos;
- Ativar e desativar usuários;
- Controlar permissões de acesso.

---

## 2.2 Atendente

Usuário responsável pelo atendimento operacional do sistema.

### Funcionalidades:
- Fazer login;
- Fazer logout;
- Alterar senha;
- Cadastrar participantes;
- Consultar participantes;
- Editar dados dos participantes;
- Alterar status do participante;
- Consultar modalidades;
- Emitir relatórios operacionais.

---

## 2.3 Cliente

Usuário participante do projeto social.

### Funcionalidades:
- Realizar autocadastro;
- Fazer login;
- Fazer logout;
- Alterar senha;
- Consultar seus dados;
- Atualizar informações pessoais;
- Consultar modalidade vinculada.

---

# 3. Casos de Uso

## 3.1 Cliente
- Realizar autocadastro;
- Fazer login;
- Fazer logout;
- Alterar senha;
- Consultar cadastro;
- Atualizar dados pessoais;
- Consultar modalidade esportiva vinculada.

## 3.2 Atendente
- Fazer login;
- Fazer logout;
- Alterar senha;
- Cadastrar participantes;
- Consultar participantes;
- Editar participantes;
- Alterar status do participante;
- Consultar modalidades;
- Emitir relatórios operacionais.

## 3.3 Administrador
- Fazer login;
- Fazer logout;
- Alterar senha;
- Cadastrar atendentes;
- Consultar atendentes;
- Editar atendentes;
- Desativar atendentes;
- Gerenciar participantes;
- Gerenciar modalidades;
- Visualizar dashboard;
- Emitir relatórios gerenciais;
- Exportar relatórios;
- Consultar logs do sistema;
- Configurar dados iniciais do sistema;
- Controlar permissões por perfil.

---

# 4. Arquitetura

A arquitetura do sistema será baseada em aplicação web utilizando padrão MVC.

## Camadas da aplicação:

### Camada de Apresentação (View)
Responsável pela interface do usuário utilizando:
- HTML5;
- CSS3;
- Bootstrap;
- Jinja2;
- JavaScript.

### Camada de Controle (Controller)
Responsável por receber requisições, validar permissões e chamar os serviços necessários:
- Python;
- Flask;
- Blueprints.

### Camada de Serviços (Service)
Responsável pelas regras de negócio:
- Autenticação;
- Usuários;
- Participantes;
- Modalidades;
- Relatórios;
- Logs;
- Permissões.

### Camada de Dados (Model)
Responsável pela persistência dos dados:
- SQLite;
- Models Python;
- Consultas SQL.

---

# 5. Plataforma Tecnológica

| Camada | Tecnologia |
|---|---|
| Linguagem Back-end | Python |
| Framework Web | Flask |
| Template Engine | Jinja2 |
| Front-end | HTML5 + CSS3 |
| Interface Responsiva | Bootstrap |
| Scripts | JavaScript |
| Banco de Dados | SQLite |
| Containerização | Docker |
| Controle de Versão | GitHub |
| Ambiente de Desenvolvimento | Replit |
| Inteligência Artificial | ChatGPT |

---

# 6. Estrutura de Diretórios

```text
projeto_social/
│
├── app/
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── dashboard_controller.py
│   │   ├── alunos_controller.py
│   │   ├── modalidades_controller.py
│   │   ├── usuarios_controller.py
│   │   ├── relatorios_controller.py
│   │   └── logs_controller.py
│   │
│   ├── models/
│   │   ├── usuario.py
│   │   ├── aluno.py
│   │   ├── modalidade.py
│   │   └── log.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── usuario_service.py
│   │   ├── aluno_service.py
│   │   ├── modalidade_service.py
│   │   ├── relatorio_service.py
│   │   └── log_service.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── alunos/
│   │   ├── modalidades/
│   │   ├── usuarios/
│   │   ├── relatorios/
│   │   └── logs/
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   │
│   ├── database/
│   │   ├── database.py
│   │   └── schema.sql
│   │
│   └── utils/
│       ├── permissoes.py
│       ├── validadores.py
│       └── exportadores.py
│
├── config/
│   └── config.py
│
├── docker/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .env.example
├── run.py
└── README.md
```

---

# 7. Convenções

## 7.1 Convenções Python
- Seguir padrão PEP 8;
- Utilizar snake_case para variáveis e funções;
- Utilizar CamelCase para classes;
- Utilizar UPPER_CASE para constantes;
- Separar controllers, services, models e templates.

## 7.2 Convenções de Templates
- Utilizar extensão .html;
- Utilizar Jinja2;
- Utilizar layout base;
- Criar componentes reutilizáveis;
- Manter formulários separados por módulo.

## 7.3 Convenções GitHub
- Utilizar commits descritivos;
- Utilizar versionamento contínuo;
- Organizar branches por funcionalidades;
- Registrar alterações relevantes no README.

## 7.4 Convenções de Rotas
- Usar rotas claras e padronizadas;
- Utilizar prefixos por módulo;
- Proteger rotas conforme perfil do usuário.

Exemplo:
```text
/auth/login
/auth/logout
/auth/register
/dashboard
/alunos
/modalidades
/usuarios
/relatorios
/logs
```

---

# 8. Serviços do Sistema

## 8.1 Serviço de Autenticação
Responsável por:
- Login;
- Logout;
- Autocadastro de cliente;
- Controle de sessão;
- Alteração de senha;
- Recuperação de senha;
- Criptografia de senha;
- Validação de usuário ativo.

## 8.2 Serviço de Usuários
Responsável por:
- Cadastro de atendentes;
- Cadastro do administrador inicial;
- Edição de usuários;
- Desativação de usuários;
- Controle de perfis;
- Controle de permissões.

## 8.3 Serviço de Participantes
Responsável por:
- Cadastro de alunos;
- Consulta de participantes;
- Edição de participantes;
- Exclusão de participantes;
- Validação de CPF;
- Filtro por modalidade;
- Filtro por status.

## 8.4 Serviço de Modalidades
Responsável por:
- Cadastro de modalidades;
- Consulta de modalidades;
- Edição de modalidades;
- Exclusão de modalidades;
- Controle de vagas;
- Bloqueio de exclusão quando houver participantes vinculados.

## 8.5 Serviço de Relatórios
Responsável por:
- Relatório de alunos;
- Relatório de modalidades;
- Indicadores estatísticos;
- Geração de gráficos;
- Exportação para Excel;
- Exportação para PDF;
- Impressão dos relatórios.

## 8.6 Serviço de Logs
Responsável por:
- Registrar cadastro de usuários;
- Registrar edição de usuários;
- Registrar exclusão ou desativação;
- Registrar operações administrativas;
- Permitir consulta por administradores.

## 8.7 Serviço de Dashboard
Responsável por:
- Total de alunos ativos;
- Total de alunos inativos;
- Total de modalidades;
- Total geral de participantes;
- Gráfico de alunos por modalidade;
- Listagem dos últimos alunos cadastrados.

---

# 9. Variáveis de Ambiente

| Variável | Descrição |
|---|---|
| SECRET_KEY | Chave secreta Flask |
| FLASK_ENV | Ambiente de execução |
| DATABASE_URL | Caminho banco SQLite |
| ADMIN_EMAIL | E-mail administrador inicial |
| ADMIN_PASSWORD | Senha administrador inicial |
| ADMIN_NAME | Nome do administrador inicial |
| DEBUG_MODE | Define se a aplicação roda em modo debug |
| APP_PORT | Porta de execução da aplicação |
| SESSION_TIMEOUT | Tempo máximo de sessão |

## Exemplo:

```env
SECRET_KEY=segredo_flask
FLASK_ENV=development
DATABASE_URL=sqlite:///database.db
ADMIN_EMAIL=admin@projeto.com
ADMIN_PASSWORD=123456
ADMIN_NAME=Administrador Inicial
DEBUG_MODE=True
APP_PORT=5000
SESSION_TIMEOUT=3600
```

---

# 10. Fluxo de Cadastro de Usuários

## 10.1 Cliente
- Cliente acessa a tela de autocadastro;
- Informa nome, e-mail, senha e dados pessoais;
- Sistema valida os dados;
- Sistema cria a conta com perfil cliente;
- Cliente realiza login.

## 10.2 Atendente
- Administrador acessa o painel de usuários;
- Administrador cadastra novo atendente;
- Sistema valida os dados;
- Sistema cria a conta com perfil atendente;
- Sistema registra log da operação.

## 10.3 Administrador
- O sistema deve criar um administrador inicial automaticamente;
- Os dados do administrador inicial serão definidos nas variáveis de ambiente;
- O administrador inicial terá acesso completo ao sistema;
- O administrador poderá gerenciar atendentes, participantes, modalidades e relatórios.

---

# 11. Modelagem Inicial do Banco de Dados

## 11.1 Tabela usuarios

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único |
| nome | TEXT | Nome do usuário |
| email | TEXT | E-mail de acesso |
| senha | TEXT | Senha criptografada |
| perfil | TEXT | administrador, atendente ou cliente |
| status | TEXT | ativo ou inativo |
| criado_em | DATETIME | Data de criação |
| atualizado_em | DATETIME | Data de atualização |

---

## 11.2 Tabela alunos

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único |
| nome | TEXT | Nome completo |
| cpf | TEXT | CPF do participante |
| data_nascimento | DATE | Data de nascimento |
| telefone | TEXT | Telefone ou WhatsApp |
| endereco | TEXT | Endereço completo |
| nome_pai | TEXT | Nome do pai |
| nome_mae | TEXT | Nome da mãe |
| modalidade_id | INTEGER | Modalidade vinculada |
| status | TEXT | ativo ou inativo |
| criado_em | DATETIME | Data de criação |
| atualizado_em | DATETIME | Data de atualização |

---

## 11.3 Tabela modalidades

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único |
| nome | TEXT | Nome da modalidade |
| descricao | TEXT | Descrição da modalidade |
| vagas | INTEGER | Quantidade de vagas |
| criado_em | DATETIME | Data de criação |
| atualizado_em | DATETIME | Data de atualização |

---

## 11.4 Tabela logs

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único |
| usuario_id | INTEGER | Usuário responsável pela ação |
| acao | TEXT | Ação realizada |
| modulo | TEXT | Módulo afetado |
| descricao | TEXT | Descrição da operação |
| criado_em | DATETIME | Data e hora do registro |

---

# 12. Especificações Técnicas

## /run.py
- ação: criar
- descrição:
Arquivo principal responsável por iniciar a aplicação Flask.

- pseudocódigo:
```text
1. Importar função de criação da aplicação
2. Criar instância da aplicação
3. Carregar porta definida em variável de ambiente
4. Executar servidor Flask
```

---

## /app/__init__.py
- ação: criar
- descrição:
Inicializar aplicação Flask, registrar blueprints e preparar configurações.

- pseudocódigo:
```text
1. Criar aplicação Flask
2. Carregar configurações do ambiente
3. Inicializar banco de dados
4. Registrar controllers
5. Criar administrador inicial se não existir
6. Retornar aplicação configurada
```

---

## /app/database/database.py
- ação: criar
- descrição:
Gerenciar conexão com o banco de dados SQLite.

- pseudocódigo:
```text
1. Ler DATABASE_URL
2. Abrir conexão SQLite
3. Retornar conexão ativa
4. Fechar conexão ao final da requisição
```

---

## /app/database/schema.sql
- ação: criar
- descrição:
Definir estrutura inicial do banco de dados.

- pseudocódigo:
```text
1. Criar tabela usuarios
2. Criar tabela alunos
3. Criar tabela modalidades
4. Criar tabela logs
5. Definir chaves primárias e estrangeiras
```

---

## /app/controllers/auth_controller.py
- ação: criar
- descrição:
Controlador responsável por login, logout, autocadastro, alteração e recuperação de senha.

- pseudocódigo:
```text
1. Exibir tela de login
2. Receber credenciais
3. Validar usuário e senha
4. Verificar status ativo
5. Criar sessão
6. Redirecionar conforme perfil
7. Permitir logout
8. Permitir autocadastro de cliente
9. Permitir alteração de senha
10. Permitir solicitação de recuperação de senha
```

---

## /app/controllers/dashboard_controller.py
- ação: criar
- descrição:
Controlador responsável pela tela inicial com indicadores e gráficos.

- pseudocódigo:
```text
1. Verificar usuário autenticado
2. Consultar total de alunos ativos
3. Consultar total de alunos inativos
4. Consultar total de modalidades
5. Consultar total geral de alunos
6. Consultar últimos alunos cadastrados
7. Gerar dados para gráfico por modalidade
8. Renderizar dashboard
```

---

## /app/controllers/alunos_controller.py
- ação: criar
- descrição:
Controlador responsável pelo CRUD completo de participantes/alunos.

- pseudocódigo:
```text
1. Verificar permissão de administrador ou atendente
2. Listar alunos cadastrados
3. Permitir busca por nome
4. Permitir filtro por modalidade
5. Permitir filtro por status
6. Exibir formulário de cadastro
7. Validar dados obrigatórios
8. Validar CPF
9. Verificar duplicidade de CPF
10. Salvar aluno
11. Editar aluno existente
12. Alterar status do aluno
13. Excluir aluno com confirmação
14. Registrar log da operação
```

---

## /app/controllers/modalidades_controller.py
- ação: criar
- descrição:
Controlador responsável pelo CRUD completo de modalidades esportivas.

- pseudocódigo:
```text
1. Verificar permissão de administrador ou atendente
2. Listar modalidades
3. Exibir total de alunos por modalidade
4. Cadastrar nova modalidade
5. Validar nome da modalidade
6. Validar quantidade de vagas
7. Editar modalidade
8. Verificar se há alunos vinculados antes de excluir
9. Bloquear exclusão quando houver vínculo
10. Excluir modalidade quando permitido
11. Registrar log da operação
```

---

## /app/controllers/usuarios_controller.py
- ação: criar
- descrição:
Controlador responsável pelo gerenciamento de atendentes e controle de perfis.

- pseudocódigo:
```text
1. Verificar permissão de administrador
2. Listar usuários
3. Filtrar usuários por nome, e-mail, perfil ou status
4. Cadastrar atendente
5. Validar e-mail duplicado
6. Criptografar senha
7. Editar dados do usuário
8. Alterar perfil quando permitido
9. Desativar usuário
10. Bloquear autoexclusão
11. Registrar log da operação
```

---

## /app/controllers/relatorios_controller.py
- ação: criar
- descrição:
Controlador responsável pelos relatórios de alunos e modalidades.

- pseudocódigo:
```text
1. Verificar usuário autenticado
2. Exibir relatório de alunos
3. Aplicar filtro por modalidade
4. Aplicar filtro por status
5. Aplicar filtro por período de cadastro
6. Exibir relatório de modalidades
7. Calcular percentual de ocupação de vagas
8. Gerar gráficos
9. Permitir impressão
10. Permitir exportação Excel
11. Permitir exportação PDF
```

---

## /app/controllers/logs_controller.py
- ação: criar
- descrição:
Controlador responsável pela consulta dos logs administrativos.

- pseudocódigo:
```text
1. Verificar permissão de administrador
2. Listar logs do sistema
3. Filtrar logs por usuário
4. Filtrar logs por módulo
5. Filtrar logs por data
6. Exibir detalhes da operação
```

---

## /app/services/auth_service.py
- ação: criar
- descrição:
Serviço de autenticação e segurança de acesso.

- pseudocódigo:
```text
1. Criptografar senha
2. Validar senha informada
3. Criar sessão de usuário
4. Encerrar sessão
5. Verificar permissão por perfil
6. Validar usuário ativo
7. Processar alteração de senha
8. Processar recuperação de senha
```

---

## /app/services/usuario_service.py
- ação: criar
- descrição:
Serviço de regras de negócio dos usuários.

- pseudocódigo:
```text
1. Criar administrador inicial
2. Cadastrar atendente
3. Validar e-mail único
4. Editar usuário
5. Desativar usuário
6. Bloquear autoexclusão
7. Registrar log
```

---

## /app/services/aluno_service.py
- ação: criar
- descrição:
Serviço de regras de negócio dos participantes.

- pseudocódigo:
```text
1. Validar nome obrigatório
2. Validar CPF quando informado
3. Verificar duplicidade de CPF
4. Salvar aluno
5. Atualizar aluno
6. Alterar status
7. Excluir aluno
8. Listar alunos com filtros
```

---

## /app/services/modalidade_service.py
- ação: criar
- descrição:
Serviço de regras de negócio das modalidades.

- pseudocódigo:
```text
1. Validar nome da modalidade
2. Validar quantidade de vagas
3. Criar modalidade
4. Editar modalidade
5. Verificar vínculo com alunos
6. Excluir modalidade quando permitido
7. Calcular ocupação de vagas
```

---

## /app/services/relatorio_service.py
- ação: criar
- descrição:
Serviço responsável pela geração de relatórios e indicadores.

- pseudocódigo:
```text
1. Buscar alunos conforme filtros
2. Buscar modalidades conforme filtros
3. Calcular totais
4. Calcular percentuais
5. Gerar dados para gráficos
6. Exportar Excel
7. Exportar PDF
```

---

## /app/services/log_service.py
- ação: criar
- descrição:
Serviço responsável pelo registro de logs.

- pseudocódigo:
```text
1. Receber usuário responsável
2. Receber módulo afetado
3. Receber ação realizada
4. Montar descrição da operação
5. Salvar log no banco
```

---

## /app/utils/permissoes.py
- ação: criar
- descrição:
Funções auxiliares para controle de acesso.

- pseudocódigo:
```text
1. Verificar se usuário está logado
2. Verificar se usuário é administrador
3. Verificar se usuário é atendente
4. Verificar se usuário é cliente
5. Bloquear acesso não autorizado
```

---

## /app/utils/validadores.py
- ação: criar
- descrição:
Funções de validação de formulários.

- pseudocódigo:
```text
1. Validar campos obrigatórios
2. Validar CPF
3. Validar e-mail
4. Validar senha
5. Retornar mensagens de erro
```

---

## /app/utils/exportadores.py
- ação: criar
- descrição:
Funções responsáveis pela exportação de relatórios.

- pseudocódigo:
```text
1. Receber dados do relatório
2. Gerar arquivo Excel
3. Gerar arquivo PDF
4. Retornar arquivo para download
```

---

## /app/templates/base.html
- ação: criar
- descrição:
Template base da aplicação.

- pseudocódigo:
```text
1. Definir estrutura HTML principal
2. Carregar Bootstrap
3. Carregar arquivo CSS
4. Exibir menu conforme perfil do usuário
5. Definir área de conteúdo
6. Carregar scripts JavaScript
```

---

## /app/templates/login.html
- ação: criar
- descrição:
Tela de login do sistema.

- pseudocódigo:
```text
1. Exibir formulário de login
2. Solicitar e-mail e senha
3. Enviar dados para auth_controller
4. Exibir mensagem de erro quando inválido
```

---

## /app/templates/register.html
- ação: criar
- descrição:
Tela de autocadastro do cliente.

- pseudocódigo:
```text
1. Exibir formulário de autocadastro
2. Receber dados do cliente
3. Validar campos obrigatórios
4. Criar usuário com perfil cliente
5. Redirecionar para login
```

---

## /app/templates/dashboard.html
- ação: criar
- descrição:
Tela inicial com indicadores gerenciais.

- pseudocódigo:
```text
1. Exibir cards de indicadores
2. Exibir últimos alunos cadastrados
3. Exibir gráfico por modalidade
4. Exibir atalhos rápidos
```

---

## /app/templates/alunos/listar.html
- ação: criar
- descrição:
Tela de listagem de participantes.

- pseudocódigo:
```text
1. Exibir tabela de alunos
2. Exibir filtros por nome, modalidade e status
3. Exibir botão de cadastro
4. Exibir ações de editar, status e excluir
```

---

## /app/templates/alunos/form.html
- ação: criar
- descrição:
Formulário de cadastro e edição de participantes.

- pseudocódigo:
```text
1. Exibir campos do participante
2. Exibir lista de modalidades
3. Validar CPF
4. Enviar dados para controller
```

---

## /app/templates/modalidades/listar.html
- ação: criar
- descrição:
Tela de listagem de modalidades.

- pseudocódigo:
```text
1. Exibir modalidades cadastradas
2. Exibir quantidade de vagas
3. Exibir total de participantes vinculados
4. Exibir ações de editar e excluir
```

---

## /app/templates/modalidades/form.html
- ação: criar
- descrição:
Formulário de cadastro e edição de modalidades.

- pseudocódigo:
```text
1. Exibir campo nome
2. Exibir campo descrição
3. Exibir campo vagas
4. Validar dados
5. Enviar para controller
```

---

## /app/templates/usuarios/listar.html
- ação: criar
- descrição:
Tela de gerenciamento de usuários.

- pseudocódigo:
```text
1. Exibir usuários cadastrados
2. Filtrar por nome, e-mail, perfil ou status
3. Exibir botão de cadastro de atendente
4. Exibir ações de editar e desativar
```

---

## /app/templates/usuarios/form.html
- ação: criar
- descrição:
Formulário de cadastro e edição de usuários.

- pseudocódigo:
```text
1. Exibir campos do usuário
2. Validar e-mail
3. Definir perfil
4. Definir status
5. Salvar usuário
```

---

## /app/templates/relatorios/alunos.html
- ação: criar
- descrição:
Relatório de alunos.

- pseudocódigo:
```text
1. Exibir filtros
2. Listar alunos filtrados
3. Exibir botão imprimir
4. Exibir botão exportar Excel
5. Exibir botão exportar PDF
```

---

## /app/templates/relatorios/modalidades.html
- ação: criar
- descrição:
Relatório de modalidades.

- pseudocódigo:
```text
1. Exibir modalidades
2. Exibir total de alunos
3. Exibir vagas disponíveis
4. Exibir percentual de ocupação
5. Exibir gráfico
```

---

## /app/templates/logs/listar.html
- ação: criar
- descrição:
Tela de consulta de logs administrativos.

- pseudocódigo:
```text
1. Exibir lista de logs
2. Filtrar por usuário
3. Filtrar por módulo
4. Filtrar por período
5. Exibir detalhes da ação
```

---

## /app/static/css/style.css
- ação: criar
- descrição:
Arquivo de estilos personalizados.

- pseudocódigo:
```text
1. Definir cores principais
2. Definir layout do dashboard
3. Definir responsividade
4. Definir estilo de tabelas
5. Definir estilo de formulários
```

---

## /app/static/js/main.js
- ação: criar
- descrição:
Arquivo JavaScript principal.

- pseudocódigo:
```text
1. Validar formulários
2. Aplicar máscaras
3. Exibir alertas
4. Confirmar exclusões
5. Atualizar elementos visuais
```

---

## /Dockerfile
- ação: criar
- descrição:
Arquivo responsável pela criação do container Docker.

- pseudocódigo:
```text
1. Definir imagem base Python
2. Definir diretório de trabalho
3. Copiar requirements.txt
4. Instalar dependências
5. Copiar arquivos do projeto
6. Expor porta da aplicação
7. Executar aplicação Flask
```

---

## /docker-compose.yml
- ação: criar
- descrição:
Arquivo para orquestrar a aplicação em contêiner.

- pseudocódigo:
```text
1. Definir serviço web
2. Definir build pelo Dockerfile
3. Mapear porta da aplicação
4. Carregar variáveis de ambiente
5. Definir volume do banco SQLite
```

---

## /requirements.txt
- ação: criar
- descrição:
Arquivo de dependências Python.

- pseudocódigo:
```text
1. Incluir Flask
2. Incluir python-dotenv
3. Incluir bibliotecas de exportação Excel
4. Incluir bibliotecas de geração PDF
```

---

## /.env.example
- ação: criar
- descrição:
Modelo de variáveis de ambiente.

- pseudocódigo:
```text
1. Listar SECRET_KEY
2. Listar DATABASE_URL
3. Listar ADMIN_EMAIL
4. Listar ADMIN_PASSWORD
5. Listar DEBUG_MODE
```

---

## /README.md
- ação: criar
- descrição:
Documentação inicial do projeto.

- pseudocódigo:
```text
1. Descrever objetivo do sistema
2. Informar tecnologias utilizadas
3. Explicar instalação
4. Explicar execução com Docker
5. Explicar perfis de usuário
```

---

# 13. Segurança

O sistema deverá implementar:
- Login obrigatório;
- Logout seguro;
- Controle de sessão;
- Criptografia de senhas;
- Controle de permissões por perfil;
- Proteção contra acesso não autorizado;
- Validação de formulários;
- Validação de CPF;
- Validação de e-mail;
- Bloqueio de usuários inativos;
- Bloqueio de autoexclusão;
- Registro de logs administrativos.

---

# 14. Regras de Negócio

## 14.1 Usuários
- Cliente pode se autocadastrar;
- Atendente só pode ser cadastrado por administrador;
- Deve haver um administrador inicial;
- Usuários inativos não podem acessar o sistema;
- Usuário não pode excluir sua própria conta;
- Senhas devem ser criptografadas.

## 14.2 Participantes
- Nome do participante é obrigatório;
- CPF deve ser validado quando informado;
- CPF não pode ser duplicado;
- Participante deve possuir status ativo ou inativo;
- Participante pode ser vinculado a uma modalidade.

## 14.3 Modalidades
- Nome da modalidade é obrigatório;
- Quantidade de vagas deve ser número inteiro;
- Modalidade com participantes vinculados não pode ser excluída;
- Sistema deve calcular ocupação de vagas.

## 14.4 Relatórios
- Relatórios devem permitir filtros;
- Relatórios devem permitir impressão;
- Relatórios devem permitir exportação;
- Dashboard deve apresentar indicadores em tempo real.

---

# 15. Estrutura de Rotas Flask

```text
/auth/login
/auth/logout
/auth/register
/auth/alterar-senha
/auth/recuperar-senha

/dashboard

/alunos
/alunos/novo
/alunos/<id>/editar
/alunos/<id>/excluir
/alunos/<id>/status

/modalidades
/modalidades/nova
/modalidades/<id>/editar
/modalidades/<id>/excluir

/usuarios
/usuarios/novo
/usuarios/<id>/editar
/usuarios/<id>/desativar

/relatorios/alunos
/relatorios/modalidades
/relatorios/alunos/exportar-excel
/relatorios/alunos/exportar-pdf
/relatorios/modalidades/exportar-excel
/relatorios/modalidades/exportar-pdf

/logs
```

---

# 16. Objetivo Final

O objetivo do projeto é desenvolver uma aplicação web moderna, organizada, segura e responsiva para auxiliar no gerenciamento administrativo de projetos sociais esportivos.

O sistema deverá proporcionar maior controle operacional, organização das informações, acompanhamento das modalidades, gestão dos participantes, emissão de relatórios e melhoria na tomada de decisão da coordenação do projeto social.
