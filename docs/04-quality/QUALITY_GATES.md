# Quality Gates

## Gate de tarefa

- escopo e causa compreendidos;
- sintaxe e imports validados;
- testes relevantes passam;
- tratamento de erro e redaction verificados;
- documentos da matriz atualizados;
- nenhuma regressão conhecida escondida;
- `PROJECT_STATUS.md` atualizado.

## Gate de banco

- migração aplicada em fixture anterior;
- integridade verificada;
- transação e rollback testados;
- dados essenciais preservados;
- recovery documentado.

## Gate Kodi

- `addon.xml` parseável;
- rotas finalizam corretamente;
- playback usa fluxo oficial;
- settings/localização válidos;
- caminhos usam APIs compatíveis;
- log do Kodi inspecionado.

## Gate de release

- versão coerente em todos os artefatos;
- ZIP possui diretório raiz correto e não contém arquivos proibidos;
- hashes regenerados;
- changelog e compatibility matrix atualizados;
- instalação limpa e atualização testadas;
- rollback conhecido;
- artefatos gerados por pipeline limpo.
