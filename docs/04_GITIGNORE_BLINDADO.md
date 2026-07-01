# Instruções para criar e validar um gitignore blindado

O projeto tem um token com acesso total ao GitHub em um arquivo `.env` local. Esse arquivo nunca pode ser enviado ao GitHub.

## 1. Regra principal

Nunca subir:

- `.env`.
- `.env.*`.
- Tokens.
- Chaves privadas.
- Bancos SQLite reais.
- Logs.
- Dumps.
- Backups.
- Arquivos de mídia.
- Caches.
- Zips temporários.

## 2. `.gitignore` obrigatório

O arquivo `.gitignore` na raiz deste pacote já contém as regras blindadas. O Antigravity deve preservar essas regras e só adicionar exceções conscientemente.

Trecho crítico:

```gitignore
.env
.env.*
!.env.example
*.key
*.pem
*.token
*token*
*secret*
*credential*
*.db
*.sqlite
*.sqlite3
*.log
saile_dump*.md
```

## 3. Se o `.env` já foi rastreado por acidente

Rodar na raiz do repositório:

```bash
git rm --cached .env
git rm --cached .env.* 2>/dev/null || true
git status --short
```

Depois confirmar que `.env` aparece como ignorado ou não aparece mais no status.

## 4. Validar ignore

```bash
git check-ignore -v .env
python tools/preflight_no_secrets.py
```

Se `git check-ignore` não mostrar regra para `.env`, o gitignore está errado.

## 5. Preflight obrigatório antes de commit

Sempre rodar:

```bash
python tools/preflight_no_secrets.py
```

Esse script bloqueia padrões de risco, como:

- Arquivo `.env` dentro de arquivos rastreáveis.
- Possíveis tokens.
- Chaves privadas.
- Bancos `.db`.
- Logs.

## 6. Comando seguro de commit

```bash
python tools/preflight_no_secrets.py
python tools/build_repo.py --repo-url https://bruno1991.github.io/saile-repo-dev/
git status --short
git add plugin.video.saile.mc repository.saile tools docs README.md .gitignore .env.example addons.xml addons.xml.md5 index.html zips
git status --short
git commit -m "Prepare Saile Media Center test repository"
git push origin main
```

Antes de confirmar o commit, conferir visualmente que não existe `.env`, `.db`, `.log` ou dump no `git status`.

## 7. Nunca fazer

Não execute:

```bash
git add .
```

sem antes rodar o preflight e olhar o status. Em projeto com token local, `git add .` sem revisão é risco alto.

## 8. Recomendação adicional

Crie um hook local de pre-commit:

```bash
mkdir -p .git/hooks
cat > .git/hooks/pre-commit <<'EOF'
#!/usr/bin/env bash
python tools/preflight_no_secrets.py
EOF
chmod +x .git/hooks/pre-commit
```

Esse hook é local e não precisa ser versionado.
