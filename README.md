# ☁️ Catálogo de Produtos na Nuvem: Arquitetura Azure e Python

Este projeto é uma aplicação de ponta a ponta (**End-to-End**) para cadastro e visualização de produtos, desenvolvida para demonstrar habilidades práticas em **Engenharia de Dados**, **Cloud Computing (Microsoft Azure)** e desenvolvimento de interfaces com **Python**.

<img width="1120" height="755" alt="image" src="https://github.com/user-attachments/assets/7ee5753d-51c3-4722-bd3f-5b0967e7180a" />
<img width="905" height="846" alt="image" src="https://github.com/user-attachments/assets/96530188-4674-4f1a-b5dd-1ddb4142c46e" />

---

# 🎯 Objetivo do Projeto

O objetivo principal foi construir uma **arquitetura de dados funcional na nuvem**, saindo do zero até a interface do usuário.

O projeto simula o **back-end e front-end de um E-commerce**, separando:

- Armazenamento de arquivos pesados (imagens)
- Armazenamento de dados relacionais (informações dos produtos)

Tudo isso utilizando **boas práticas de segurança e desenvolvimento**.

---

# 🛠️ Tecnologias e Ferramentas Utilizadas

## ☁️ Cloud & Infraestrutura

- Microsoft Azure SQL Database — Banco de dados relacional na nuvem  
- Microsoft Azure Blob Storage — Armazenamento de objetos (imagens dos produtos)  
- SQL Server Management Studio (SSMS) — Gerenciamento e administração remota do banco  

## 💻 Desenvolvimento & Front-end

- Python 3.11+ — Linguagem principal  
- Streamlit — Interface web interativa  
- PyMSSQL — Conexão entre Python e SQL Server  
- Python-dotenv — Gerenciamento seguro de credenciais  

---

# 🚀 Processo de Desenvolvimento e Aprendizado

## 1. Provisionamento da Infraestrutura na Nuvem (Azure)

O primeiro passo foi configurar o ambiente no portal do Azure:

- Criação de servidor lógico SQL  
- Provisionamento do banco de dados  
- Configuração de Firewall do Azure  
- Adição do IP público na allowlist  

<img width="1616" height="401" alt="image" src="https://github.com/user-attachments/assets/f545895c-33fc-4940-a0d1-b78add5c8b66" />
<img width="1487" height="736" alt="image" src="https://github.com/user-attachments/assets/de5ff041-33db-4a3f-836a-48282245a2b1" />

---

## 2. Modelagem e Gerenciamento do Banco de Dados (SSMS)

Após configurar a nuvem:

- Conexão remota via SSMS  
- Criação da estrutura DDL  
- Criação da tabela `Produtos`  

<img width="578" height="738" alt="image" src="https://github.com/user-attachments/assets/6489fa73-e214-417f-9bf6-fb87f56418f5" />

---

## 3. Armazenamento em Blob (Azure Storage)

Para otimizar o banco relacional:

- Imagens não são salvas no SQL  
- Criação de container no Azure Blob Storage  
- Upload com UUID único  
- Retorno de URL pública  
- Salvamento da URL no banco SQL  

<img width="1062" height="584" alt="image" src="https://github.com/user-attachments/assets/1908bb39-887d-4fb7-a4bc-1eea0013c0e2" />
<img width="1751" height="611" alt="image" src="https://github.com/user-attachments/assets/de0016e4-cd30-4d9c-b29b-0bc3e96d866b" />
<img width="1546" height="437" alt="image" src="https://github.com/user-attachments/assets/90c929e3-b8c5-40db-a07f-0bda7652d92d" />

---

## 4. Construção da Interface e Integração (Python + Streamlit)

A interface foi construída com foco em:

- Validação de campos  
- Pop-ups de carregamento (`st.spinner`)  
- Notificações (`st.toast`)  
- Comunicação segura com banco  

<img width="1379" height="799" alt="image" src="https://github.com/user-attachments/assets/0361a79a-7bb3-4cbf-890d-09e173486a62" />

---

# 🛡️ Boas Práticas Implementadas

Durante o desenvolvimento, foram aplicadas práticas essenciais:

### 🔐 Segurança de Credenciais

- Uso de `.env`
- Credenciais fora do código
- `.env` ignorado pelo Git

### 🛡️ Prevenção contra SQL Injection

- Uso de queries parametrizadas
- Evitando f-strings em SQL
- Utilização de `pymssql`

### ⚠️ Tratamento de Exceções

- Uso de `try/except`
- Feedback amigável ao usuário
- Prevenção de falhas

### 🔄 Gerenciamento de Conexões

- Uso de `conn.commit()`
- Uso de `conn.close()`
- Evitando gargalos de conexão

---

# 💡 Insights e Próximos Passos

Este projeto ajudou a compreender, na prática, como diferentes partes de um **ecossistema de dados** se conectam.

Fluxo completo:

- Formulário  
- Upload da imagem  
- Armazenamento no Blob  
- Registro no banco SQL  

---

# 🚀 Próximos Passos (Evolução do Projeto)

- Conectar Azure SQL ao Power BI ou Google Looker Studio  
- Criar dashboard de análise de produtos  
- Hospedar aplicação Streamlit na nuvem  
- Implementar autenticação de usuários  
- Adicionar API REST  

---

# ⚙️ Como Executar Localmente

## 1. Clone o Repositório

```bash
git clone https://github.com/IannyCorreia/Catalogo-de-Produtos-na-Nuvem.git
```

## 2. Instale as dependências
```bash
pip install -r requirements.txt
```

## 3. Crie um arquivo .env na raiz do projeto
```bash
BLOB_CONNECTION_STRING=sua_string_aqui
BLOB_CONTAINER_NAME=seu_container
BLOB_ACCOUNT_NAME=sua_conta

SQL_SERVER=seu_servidor.database.windows.net
SQL_DATABASE=seu_banco
SQL_USER=seu_usuario
SQL_PASSWORD=sua_senha
```

## 4. Execute o aplicativo
```bash
streamlit run main.py
```
