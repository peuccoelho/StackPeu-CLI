import argparse
import os
import subprocess
import json

CONFIG_FILE = ".stackpeurc"


def init_project(project_type):
    print(f"🔧 Inicializando projeto do tipo: {project_type}...")

    if project_type == "fullstack":
        os.makedirs("client/src", exist_ok=True)
        os.makedirs("server/src", exist_ok=True)
        with open("client/package.json", "w") as f:
            f.write(json.dumps({
                "name": "client-app",
                "version": "1.0.0",
                "scripts": {"dev": "vite", "build": "vite build", "preview": "vite preview"}
            }, indent=2))
        with open("server/package.json", "w") as f:
            f.write(json.dumps({
                "name": "server-app",
                "version": "1.0.0",
                "scripts": {"start": "node src/index.js"}
            }, indent=2))
        with open("server/src/index.js", "w") as f:
            f.write("const express = require('express');\nconst app = express();\n\napp.get('/', (req, res) => res.send('Hello from server!'));\n\napp.listen(3000, () => console.log('Server running on port 3000'));\n")
        print(" Projeto fullstack criado com /client e /server")

    elif project_type == "backend":
        os.makedirs("src", exist_ok=True)
        with open("package.json", "w") as f:
            f.write(json.dumps({
                "name": "backend-app",
                "version": "1.0.0",
                "scripts": {"start": "node src/index.js"}
            }, indent=2))
        with open("src/index.js", "w") as f:
            f.write("const express = require('express');\nconst app = express();\n\napp.get('/', (req, res) => res.send('Hello from backend!'));\n\napp.listen(3000, () => console.log('Backend running on port 3000'));\n")
        print(" Projeto backend criado com /src")

    elif project_type == "frontend":
        os.makedirs("src", exist_ok=True)
        with open("package.json", "w") as f:
            f.write(json.dumps({
                "name": "frontend-app",
                "version": "1.0.0",
                "scripts": {"dev": "vite", "build": "vite build", "preview": "vite preview"}
            }, indent=2))
        print(" Projeto frontend criado com /src")

    else:
        print(" Tipo de projeto inválido. Use: fullstack, backend ou frontend.")
        return

    create_support_files(project_type)
    git_init_commit()

    with open(CONFIG_FILE, "w") as f:
        json.dump({"type": project_type}, f, indent=2)
    print(" Configuração salva em .stackpeurc")


def create_support_files(project_type):
    if project_type == "fullstack":
        # .env for server
        with open("server/.env", "w") as f:
            f.write("PORT=3000\n")

        # vite.config.js for client
        with open("client/vite.config.js", "w") as f:
            f.write("""import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()]
})
""")

        # ESLint config (client)
        with open("client/.eslintrc.json", "w") as f:
            f.write("""{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": ["eslint:recommended", "plugin:react/recommended", "prettier"],
  "parserOptions": {
    "ecmaFeatures": {"jsx": true},
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "plugins": ["react"],
  "rules": {}
}
""")

        # ESLint config (server)
        with open("server/.eslintrc.json", "w") as f:
            f.write("""{
  "env": {
    "node": true,
    "es2021": true
  },
  "extends": ["eslint:recommended", "prettier"],
  "parserOptions": {
    "ecmaVersion": 12
  },
  "rules": {}
}
""")

    elif project_type == "backend":
        with open(".env", "w") as f:
            f.write("PORT=3000\n")
        with open(".eslintrc.json", "w") as f:
            f.write("""{
  "env": {
    "node": true,
    "es2021": true
  },
  "extends": ["eslint:recommended", "prettier"],
  "parserOptions": {
    "ecmaVersion": 12
  },
  "rules": {}
}
""")

    elif project_type == "frontend":
        with open(".eslintrc.json", "w") as f:
            f.write("""{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": ["eslint:recommended", "plugin:react/recommended", "prettier"],
  "parserOptions": {
    "ecmaFeatures": {"jsx": true},
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "plugins": ["react"],
  "rules": {}
}
""")

    # prettier.config.js geral para todos os tipos
    with open("prettier.config.js", "w") as f:
        f.write("""module.exports = {
  semi: true,
  singleQuote: true,
  printWidth: 80,
  tabWidth: 2,
  trailingComma: "es5",
};
""")


def git_init_commit():
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Initial commit by StackPeu CLI"])
        print(" Git inicializado e commit inicial criado.")
    else:
        print(" Repositório Git já existe.")


def setup_project():
    if not os.path.exists(CONFIG_FILE):
        print(" Projeto não inicializado. Execute 'init' primeiro.")
        return

    with open(CONFIG_FILE) as f:
        config = json.load(f)

    project_type = config.get("type")

    if project_type == "fullstack":
        print("Instalando dependências para o client...")
        subprocess.run(["npm", "install", "vite", "react", "react-dom"], cwd="client")
        subprocess.run(["npm", "install", "-D", "eslint", "prettier"], cwd="client")

        print(" Instalando dependências para o server...")
        subprocess.run(["npm", "install", "express"], cwd="server")
        subprocess.run(["npm", "install", "-D", "eslint", "prettier"], cwd="server")

    elif project_type == "backend":
        print(" Instalando dependências para backend...")
        subprocess.run(["npm", "install", "express"])
        subprocess.run(["npm", "install", "-D", "eslint", "prettier"])

    elif project_type == "frontend":
        print(" Instalando dependências para frontend...")
        subprocess.run(["npm", "install", "vite", "react", "react-dom"])
        subprocess.run(["npm", "install", "-D", "eslint", "prettier"])

    else:
        print(" Tipo de projeto desconhecido.")
        return

    print(" Dependências instaladas e ambiente configurado.")


def run_dev():
    if not os.path.exists(CONFIG_FILE):
        print(" Projeto não inicializado.")
        return

    with open(CONFIG_FILE) as f:
        config = json.load(f)

    project_type = config.get("type")

    if project_type == "fullstack":
        print(" Rodando client e server em paralelo (use dois terminais)...")
        print("Terminal 1: cd client && npm run dev")
        print("Terminal 2: cd server && npm start")
    elif project_type == "frontend":
        subprocess.run(["npm", "run", "dev"])
    elif project_type == "backend":
        subprocess.run(["npm", "start"])


def check_code():
    if not os.path.exists(CONFIG_FILE):
        print(" Projeto não inicializado.")
        return

    with open(CONFIG_FILE) as f:
        config = json.load(f)

    project_type = config.get("type")

    print(" Verificando lint e formatação...")
    if project_type == "fullstack":
        subprocess.run(["npx", "eslint", "."], cwd="client")
        subprocess.run(["npx", "prettier", "--check", "."], cwd="client")
        subprocess.run(["npx", "eslint", "."], cwd="server")
        subprocess.run(["npx", "prettier", "--check", "."], cwd="server")
    else:
        subprocess.run(["npx", "eslint", "."])
        subprocess.run(["npx", "prettier", "--check", "."])

    print(" Verificação concluída.")


def build_project():
    if not os.path.exists(CONFIG_FILE):
        print(" Projeto não inicializado.")
        return

    with open(CONFIG_FILE) as f:
        config = json.load(f)

    project_type = config.get("type")

    print(" Construindo projeto...")
    if project_type == "fullstack":
        subprocess.run(["npm", "run", "build"], cwd="client")
    elif project_type == "frontend":
        subprocess.run(["npm", "run", "build"])
    else:
        print(" Nada para buildar no projeto backend.")


def test_project():
    if not os.path.exists(CONFIG_FILE):
        print(" Projeto não inicializado.")
        return

    with open(CONFIG_FILE) as f:
        config = json.load(f)

    project_type = config.get("type")

    print(" Executando testes (simulado)...")
    if project_type == "fullstack":
        print("Rodando testes em client e server...")
    else:
        print("Rodando testes no projeto...")

    print(" Testes finalizados (implementação futura).")


def main():
    parser = argparse.ArgumentParser(description="StackPeu CLI - Gerenciamento de projetos fullstack")
    parser.add_argument("command", choices=["init", "setup", "dev", "check", "build", "test"], help="Comando a executar")
    parser.add_argument("--type", choices=["fullstack", "backend", "frontend"], help="Tipo de projeto para init")

    args = parser.parse_args()

    if args.command == "init":
        if not args.type:
            print(" Para 'init' informe --type fullstack|backend|frontend")
            return
        init_project(args.type)
    elif args.command == "setup":
        setup_project()
    elif args.command == "dev":
        run_dev()
    elif args.command == "check":
        check_code()
    elif args.command == "build":
        build_project()
    elif args.command == "test":
        test_project()


if __name__ == "__main__":
    main()
