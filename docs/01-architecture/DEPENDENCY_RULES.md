# Dependency Rules

## Biblioteca padrão primeiro

Preferir biblioteca padrão quando ela atende com segurança. Toda dependência externa deve justificar funcionalidade, tamanho, licença, compatibilidade do runtime e manutenção.

## Runtime versus desenvolvimento

Ferramentas de lint, testes e typing não entram no ZIP do add-on. Dependências de runtime devem ser declaradas em `addon.xml` ou empacotadas de modo permitido e compatível.

## Imports

Imports não devem executar rede, migração destrutiva ou UI. Dependências opcionais falham com mensagem explícita e capability detection.

## Proibição de vendoring casual

Não copiar pacote inteiro para o add-on sem licença, versão, checksum e motivo registrados.
