# StackPeu CLI

**StackPeu CLI** é uma ferramenta de linha de comando escrita em Python para criar, configurar e automatizar projetos **Node.js** e **Full Stack** com facilidade.

---

## Funcionalidades

- Inicialização de projetos:

  - Backend (Node.js + Express)
  - Frontend (React + Vite)
  - Fullstack (client + server)

- Instalação automática de dependências

- Geração de estrutura de pastas e arquivos iniciais

- Configuração de ESLint e Prettier

- Inicialização de repositório Git com commit inicial

- Comandos para desenvolvimento, build, verificação de código e testes simulados

---

## Requisitos

- Python 3.8+
- Node.js e npm instalados

---

## Instalação

Clone este repositório ou copie o arquivo `stackpeucli.py` para sua máquina:

```bash
git clone https://github.com/seu-usuario/stackpeucli.git
cd stackpeucli
```

Ou, se estiver usando somente o script:

```bash
mkdir meu-projeto && cd meu-projeto
copy caminho/para/stackpeucli.py .
```

---

## Guia de uso (Passo a passo)

### 1. Iniciar um novo projeto

```bash
python stackpeucli.py init --type [fullstack | backend | frontend]
```

Exemplos:

- Projeto fullstack (client + server):

  ```bash
  python stackpeucli.py init --type fullstack
  ```

- Projeto apenas backend:

  ```bash
  python stackpeucli.py init --type backend
  ```

- Projeto apenas frontend:

  ```bash
  python stackpeucli.py init --type frontend
  ```

---

### 2. Instalar dependências

```bash
python stackpeucli.py setup
```

---

### 3. Rodar testes simulados

```bash
python stackpeucli.py test
```

---

### 4. Verificar código com ESLint e Prettier

```bash
python stackpeucli.py check
```

---

### 5. Rodar em modo de desenvolvimento

- Para **backend**:

  ```bash
  python stackpeucli.py dev
  ```

- Para **frontend**:

  ```bash
  python stackpeucli.py dev
  ```

- Para **fullstack**:

  ```bash
  python stackpeucli.py dev
  ```

  Isso mostrará instruções como:

  ```
  Terminal 1: cd client && npm run dev
  Terminal 2: cd server && npm start
  ```

---

### 6. Build do projeto (somente frontend ou fullstack)

```bash
python stackpeucli.py build
```

---

## Estrutura gerada (exemplo fullstack)

```
meu-projeto/
├── client/
│   ├── package.json
│   ├── vite.config.js
│   └── src/
├── server/
│   ├── package.json
│   └── src/
│       └── index.js
├── .stackpeurc
├── .env
├── .eslintrc.json
├── .prettierrc
└── .git/
```

---

## Ideias futuras

- Suporte para TypeScript
- Deploy automatizado (Vercel, Heroku, etc.)
- Geração de componentes/templates
- Suporte a Docker

---

## Autor

Pedro Antonio Coelho Santa Rita




