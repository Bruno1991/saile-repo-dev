# Guia de teste do Saile Media Center

## 1. Teste sem GitHub

Use este caminho quando quiser testar antes de publicar.

1. Abra o Kodi.
2. Vá em Add-ons.
3. Escolha Instalar de um arquivo zip.
4. Selecione `zips/plugin.video.saile.mc/plugin.video.saile.mc-0.1.0.zip`.
5. Abra o addon Saile Media Center.
6. Confirme se aparecem Adulto, Kids e Configurações.

## 2. Teste pelo repositório local zip

1. Instale `zips/repository.saile/repository.saile-1.0.0.zip`.
2. Vá em Instalar do repositório.
3. Abra Saile Repository.
4. Instale Saile Media Center.

## 3. Publicação no GitHub Pages

Na raiz do projeto:

```bash
python tools/preflight_no_secrets.py
python tools/build_repo.py --repo-url https://bruno1991.github.io/saile-repo-dev/
```

Depois envie para o GitHub e habilite Pages.

URL esperada do repositório estático:

```text
https://bruno1991.github.io/saile-repo-dev/
```

## 4. Instalação via File Manager do Kodi

1. Kodi -> Configurações -> Gerenciador de arquivos.
2. Adicionar fonte.
3. URL: `https://bruno1991.github.io/saile-repo-dev/`.
4. Nome: `Saile Repo Dev`.
5. Add-ons -> Instalar de um arquivo zip.
6. Abrir a fonte adicionada e instalar o zip do repositório se listado pelo ambiente Kodi.

Observação: alguns ambientes Kodi não navegam HTML do GitHub Pages como diretório. Nesse caso, baixe ou acesse diretamente o zip do repositório pela página `index.html` e instale manualmente.

## 5. Teste SaileTV

1. Abra Configurações.
2. Preencha:
   - Host Xtream.
   - Usuário.
   - Senha.
3. Volte ao addon.
4. Entre em Adulto -> SaileTV.
5. Use Atualizar conteúdo.
6. Teste TV ao vivo, VOD e Séries.

## 6. Teste SaileFy

1. Abra Configurações.
2. Preencha YouTube API Key.
3. Instale o addon oficial do YouTube no Kodi se quiser testar playback por `plugin://plugin.video.youtube`.
4. Entre em Adulto -> SaileFy.
5. Teste Busca, Top Brasil e Top Mundo.

## 7. Teste sTorrent

1. Abra Configurações.
2. Preencha a URL de uma API JSON legal/autorizada que retorne `items`.
3. Entre em Adulto -> sTorrent.
4. Teste Lançamentos, Categorias, Ranking e Busca.

## 8. Teste Kids

1. Abra Kids.
2. Confirme que somente SaileTV aparece.
3. Confirme que SaileFy e sTorrent não aparecem.

## 9. Teste de PIN

1. Abra Configurações.
2. Defina PIN de 4 a 6 dígitos.
3. Volte para a tela inicial de perfis.
4. Tente abrir Adulto e Configurações.
5. Confirme que o PIN é solicitado.
