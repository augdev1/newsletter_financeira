# 🤖 Newsletter Financeira AI

##  Visão Geral

Este projeto é um agente autônomo que cria e envia uma newsletter financeira diária por e-mail. O agente utiliza um Large Language Model (LLM) para gerar um boletim informativo detalhado, formatado e perspicaz com base nos movimentos do mercado nas últimas 24 horas.

O processo é totalmente automatizado: em um horário definido, o sistema coleta as informações, o agente de IA redige o conteúdo conforme um prompt detalhado e, em seguida, o envia para uma lista de destinatários pré-definida.

---

## ✨ Funcionalidades Principais

- **Geração Automatizada de Newsletter:** Executa diariamente em um horário agendado, sem necessidade de intervenção manual.
- **Conteúdo Guiado por IA:** Utiliza a API da Groq com o modelo Llama 3.1 para gerar análises financeiras de alta qualidade e com um tom humano.
- **Análise Financeira Detalhada:** A newsletter cobre múltiplas seções:
  - **Destaques do Dia:** As manchetes mais importantes.
  - **Mercado de Ações (IBOVESPA):** Resumo, notícias positivas e pontos de atenção.
  - **Mercado Imobiliário:** Tendências e principais movimentações.
  - **Câmbio e Economia:** Cotação do dólar, cenário econômico e notícias relevantes.
- **Disparo de E-mails:** Funcionalidade integrada para enviar automaticamente a newsletter gerada para uma lista de assinantes usando uma conta Gmail.
- **Configurável:** Todos os parâmetros essenciais (credenciais de e-mail, destinatários, horário de envio) são gerenciados através de um arquivo `.env`.

<img width="1568" height="813" alt="image" src="https://github.com/user-attachments/assets/fa468552-2d26-48d7-8be9-7446b688cf5b" />
---

## ⚙️ Como Funciona

O fluxo de trabalho foi desenhado da seguinte forma:

1.  **Agendamento:** Um script (`03.news_financeira.py`) fica em execução contínua, aguardando o horário `SEND_AT` definido no arquivo `.env` (ex: `13:55`).
2.  **Gatilho:** Ao atingir o horário agendado, o processo de criação da newsletter é iniciado.
3.  **Geração do Prompt:** O script carrega o template de instruções do arquivo `prompt.py` e insere a data atual.
4.  **Execução do Agente de IA:** O agente `agno` envia o prompt para o modelo da `Groq/Llama 3.1`. O prompt instrui a IA a atuar como um analista financeiro sênior e a criar uma newsletter detalhada, utilizando fontes confiáveis.
5.  **Parsing do Conteúdo:** O agente retorna o texto completo da newsletter no formato Markdown pré-definido.
6.  **Envio do E-mail:** O script utiliza a função `envia_email_tool` para disparar um e-mail contendo a newsletter gerada para os `DESTINATARIOS` definidos no `.env`.
7.  **Loop:** O processo aguarda o dia seguinte para enviar uma nova edição.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **IA & LLMs:**
  - `agno`: Framework para criação de agentes autônomos.
  - `groq`: Cliente Python para a API da Groq (executando Llama 3.1).
  - `tavily-python`: Ferramenta de busca para o agente.
- **E-mail:**
  - `smtplib`: Biblioteca nativa do Python para envio de e-mails via SMTP.
- **Dependências:**
  - `python-dotenv`: Para carregar variáveis de ambiente do arquivo `.env`.
- **Ambiente de Desenvolvimento:**
  - `venv`: Para gerenciamento de dependências específicas do projeto.

---

## 🚀 Setup e Instalação

Siga os passos abaixo para executar o projeto localmente:

**1. Clone este repositório:**
```bash
git clone https://github.com/augdev1/newsletter_financeira.git
cd NEWSLETTER_AUG
```

**2. Crie e ative o ambiente virtual:**
```bash
# Cria a pasta .venv
python -m venv .venv

# Ativa o ambiente (Windows)
.venv\Scripts\activate
```

**3. Instale as dependências:**
Crie um arquivo `requirements.txt` com o conteúdo abaixo:
```
tagno
groq
python-dotenv
tavily-python
```
Em seguida, instale-as:
```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente:**
Crie um arquivo chamado `.env` na raiz do projeto e preencha-o com suas credenciais.

**Importante:** Para a `EMAIL_PASSWORD`, você precisará gerar uma [Senha de App do Google](https://support.google.com/accounts/answer/185833) em vez de usar sua senha normal, caso tenha a autenticação de dois fatores ativada.

```env
# Arquivo .env

# Chave da API da Groq
GROQ_API_KEY="sua_chave_secreta_aqui"

# Configuração do E-mail (Gmail)
EMAIL_ADDRESS="seu_usuario@gmail.com"
EMAIL_PASSWORD="sua_senha_de_app_do_google"

# Lista de e-mails destinatários (separados por vírgula)
DESTINATARIOS="email1@exemplo.com,email2@exemplo.com"

# Horário para enviar a newsletter (formato 24h HH:MM)
SEND_AT="13:55"
```

---

## ▶️ Utilização

Para iniciar o agente de automação, basta executar o script principal:

```bash
python 03.news_financeira.py
```

O script ficará em execução no terminal, exibindo o andamento. Ele aguardará até o horário definido em `SEND_AT` para gerar e enviar a newsletter.

```
Agendamento de envio da newsletter às 13:55
```

Quando o horário for atingido, você verá os logs de envio do e-mail.

---

## 📂 Estrutura do Projeto

```
.
├── .env                # Arquivo de variáveis de ambiente (secreto)
├── 01.agente.py        # Script de exemplo para testes com o agente
├── 02.email_tool.py    # Script com a função básica de envio de e-mail
├── 03.news_financeira.py # Script principal que orquestra o processo
├── prompt.py           # Template de instruções detalhadas para o agente de IA
├── README.md           # Este documento
└── .venv/              # Pasta do ambiente virtual Python
```

