# Book Guide do Antigravity para o Saile Media Center

Este guia define como o agente deve trabalhar no projeto sem se perder na lógica.

## 1. Missão do agente

Construir e manter o Saile Media Center como um addon Kodi local-first, com três apps internos:

- SaileTV: Xtream/IPTV.
- SaileFy: YouTube/música.
- sTorrent: API JSON configurável para catálogo e reprodução resolvível.

O agente deve seguir o roadmap visual e a documentação do projeto. Não deve inventar produto paralelo, servidor externo obrigatório, microserviço remoto ou arquitetura que fuja de Python, SQLite e GitHub Pages.

## 2. Ordem obrigatória de leitura antes de codar

1. `README.md`.
2. `docs/00_ROADMAP_IMPLEMENTATION.md`.
3. `docs/01_SAILE_MASTER_SPEC.md`.
4. `docs/02_SKILLS_LIBRARY.md`.
5. `docs/04_GITIGNORE_BLINDADO.md`.
6. Código atual.

## 3. Regras de ouro

1. O roadmap manda na navegação.
2. SQLite manda no estado local.
3. Providers mandam nas APIs externas.
4. UI não chama API externa diretamente.
5. Kids nunca acessa SaileFy ou sTorrent.
6. Token do GitHub nunca entra no Git.
7. `.env` nunca entra no Git.
8. Nenhum endpoint pirata deve ser embutido.
9. O addon deve abrir mesmo sem credenciais configuradas.
10. Toda falha de API deve ser tratada sem quebrar a UI.

## 4. Como decidir onde codar

Use esta tabela mental:

```text
Menu, item de lista, botão, ícone -> ui.py/router.py
Credencial e settings -> settings.py/resources/settings.xml
Dados locais -> storage.py
Perfil, Kids, PIN -> profiles.py
Xtream -> providers/xtream.py
YouTube -> providers/youtube.py
Torrent JSON -> providers/torrent_json.py
Build repo -> tools/build_repo.py
Segurança de Git -> .gitignore/tools/preflight_no_secrets.py
```

## 5. Proibições

O agente não pode:

- Subir `.env`.
- Ler token e imprimir token.
- Criar endpoint de pirataria hardcoded.
- Transformar o addon em app web obrigatório.
- Criar backend remoto obrigatório.
- Trocar SQLite por banco remoto.
- Remover perfis.
- Remover PIN.
- Remover Kids.
- Expor SaileFy ou sTorrent no Kids.
- Quebrar instalação via GitHub Pages.
- Colocar dados fictícios como se fossem API real.

## 6. Política sobre APIs finais ainda não decididas

Quando uma API final ainda não foi decidida, o agente deve criar adapter genérico configurável e contrato claro, sem inventar endpoint final.

Exemplo correto:

```text
Criar provider torrent_json.py que lê uma URL configurada e normaliza JSON.
```

Exemplo errado:

```text
Hardcodar site pirata ou scraper específico.
```

## 7. Política de entregas

Toda entrega deve conter:

- Caminho do arquivo.
- Arquivo completo ou patch claro.
- Motivo da mudança.
- Teste executado.
- Impacto em build e repositório.

Para mudanças grandes, atualizar documentação em `docs/`.

## 8. Definition of Done

Uma tarefa só está pronta quando:

1. O addon abre no Kodi.
2. A rota nova aparece no local correto.
3. A rota não quebra sem credencial.
4. Logs não expõem segredo.
5. Kids continua bloqueado.
6. `preflight_no_secrets.py` passa.
7. `build_repo.py` passa.
8. A documentação foi atualizada quando a regra mudou.

## 9. Prompt operacional para o Antigravity

Use este prompt quando for pedir ao agente para continuar:

```text
Você está trabalhando no projeto Saile Media Center.
Antes de codar, leia README.md, docs/00_ROADMAP_IMPLEMENTATION.md, docs/01_SAILE_MASTER_SPEC.md, docs/02_SKILLS_LIBRARY.md e docs/04_GITIGNORE_BLINDADO.md.
Siga o roadmap visual à risca.
Runtime do addon: somente Python e SQLite dentro do Kodi.
GitHub Pages serve apenas index.html, addons.xml, checksum e zips.
Não crie servidor externo obrigatório.
Não suba .env, token, banco, log, dumps ou mídia.
Não implemente endpoint pirata hardcoded.
Não exponha SaileFy ou sTorrent para perfil Kids.
Ao alterar código, entregue caminho exato, arquivo completo quando necessário, teste feito e impacto.
Rode tools/preflight_no_secrets.py e tools/build_repo.py antes de considerar pronto.
```
