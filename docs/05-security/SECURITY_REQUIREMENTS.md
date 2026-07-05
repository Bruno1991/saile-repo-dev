# Security Requirements

- TLS validado por padrão;
- nenhum comando shell com entrada externa;
- URLs aceitas por esquema permitido;
- caminhos resolvidos dentro do diretório autorizado;
- SQL sempre parametrizado;
- JSON com limites e validação;
- senha/token nunca em exceptions ou logs;
- settings sensíveis não copiados para banco de catálogo;
- diagnóstico passa por redaction;
- componentes opcionais desabilitados por padrão quando ampliam superfície de ataque.
