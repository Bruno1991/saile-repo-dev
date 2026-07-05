# Contribuindo com o SAILE

## Fluxo

1. leia `AGENTS.md` e a especificação mestre;
2. crie uma mudança pequena e rastreável;
3. adicione ou atualize testes;
4. atualize documentos exigidos pela matriz;
5. execute validadores;
6. abra PR descrevendo causa, solução, risco e evidência.

## Regras de código

- Python claro, tipado onde agrega segurança e sem dependências desnecessárias;
- SQL parametrizado e migrações versionadas;
- APIs Kodi isoladas em gateways de apresentação;
- rede isolada em providers/clients;
- nenhuma credencial em fixtures;
- mensagens ao usuário localizáveis;
- nenhum emoji como substituto de ícone na UI do add-on.

## Commits

Commits devem representar unidades coerentes. Não misture refatoração ampla com correção urgente. Artefatos gerados só entram quando a política do repositório exigir.

## Pull requests

A descrição deve incluir arquivos, contratos, testes, dispositivos, screenshots quando UI mudou e riscos restantes. PR sem evidência não deve ser aprovado.
