# Backup and Recovery

## Backup

Usar API de backup SQLite quando disponível ou cópia consistente com conexão fechada. Nomear com versão e timestamp. Não incluir credenciais externas.

## Recuperação

1. parar escritas;
2. preservar arquivo original;
3. executar `quick_check` e registrar resultado;
4. tentar restore de backup conhecido;
5. reconstruir apenas cache, nunca estado do usuário sem aviso;
6. validar schema e conteúdo;
7. registrar incidente.

## Exportação

Dados exportáveis devem ter formato versionado, validação de tamanho e importação transacional.
