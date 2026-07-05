# Reproducible Build

O mesmo commit, configuração e ferramenta devem produzir o mesmo conjunto lógico de arquivos. Timestamps de ZIP podem variar se não normalizados, mas conteúdo, versão e manifest devem ser determinísticos. Build não depende de arquivos pessoais, `.env` ou estado anterior do diretório de saída.
