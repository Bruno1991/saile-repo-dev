# Torrent Provider Specification

## Escopo permitido

O provider pode integrar metadados e fontes que o usuário esteja legalmente autorizado a acessar, como conteúdo próprio, domínio público ou distribuição licenciada. O projeto não deve incluir catálogo ilícito, bypass de bloqueios, credenciais de trackers privados ou automação destinada a infração.

## Arquitetura

A UI manipula itens de domínio. Um adapter opcional resolve metadados e uma engine local aprovada por ADR realiza operações compatíveis com o dispositivo. Componentes nativos não podem ser assumidos em todas as plataformas.

## Segurança

- validar magnet/URI e limites de tamanho;
- não executar arquivos baixados;
- restringir caminhos ao perfil do add-on;
- evitar exposição de IP/estado sem informar o usuário;
- permitir cancelamento e limpeza;
- nunca abrir portas automaticamente sem decisão explícita.

## Compatibilidade

Cada engine e plataforma exige matriz própria. Falha de capability deve desabilitar a função sem quebrar o restante do add-on.
