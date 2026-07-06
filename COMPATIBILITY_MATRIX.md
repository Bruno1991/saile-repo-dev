# Matriz de compatibilidade

## Alvo inicial

- Kodi 21.2 Omega como baseline do projeto.
- Python 3 fornecido pelo Kodi; não assumir o Python do sistema.
- Windows, Linux, Android, Android TV e Fire TV/Firestick.
- Controle remoto como método primário de navegação em TV.

## Regras

1. Não usar paths absolutos nem gravar dentro da pasta de instalação do addon.
2. Não depender de executável externo global para funções essenciais.
3. Toda dependência Python precisa ser empacotável/instalável no ecossistema Kodi alvo.
4. yt-dlp muda rapidamente; encapsular sua API e testar fixtures/seleção de formatos.
5. FTS5 e WAL devem ser detectados/testados; oferecer fallback seguro.
6. Metadados usam API moderna do Kodi quando disponível, encapsulada para evitar espalhar condicionais.

## Testes mínimos de plataforma

| Cenário | Windows | Linux | Android/Fire TV |
|---|---:|---:|---:|
| instalar sRepo por ZIP | obrigatório | obrigatório | obrigatório |
| instalar/atualizar sTv | obrigatório | obrigatório | obrigatório |
| instalar/atualizar sFy | obrigatório | obrigatório | obrigatório |
| sincronizar catálogo Xtream | obrigatório | obrigatório | obrigatório |
| reproduzir live/VOD/episódio | obrigatório | obrigatório | obrigatório |
| buscar e reproduzir áudio | obrigatório | obrigatório | obrigatório |
| migrar SQLite | obrigatório | obrigatório | obrigatório |
