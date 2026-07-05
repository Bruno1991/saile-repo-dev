# Data Dictionary

| Campo | Tipo | Regra |
|---|---|---|
| provider_id | TEXT | identificador interno estável, sem segredo |
| external_id | TEXT | ID opaco fornecido pelo provider |
| media_type | TEXT | enum validado: live, movie, series, season, episode, music |
| title/name | TEXT | texto de exibição; nunca usado como chave |
| art | TEXT/JSON | URLs ou mapa normalizado; pode estar ausente |
| payload | TEXT/JSON | somente dados necessários; schema versionado |
| created_at | TEXT | UTC, formato definido pelo repositório |
| updated_at | TEXT | UTC, atualizado em mudança real |
| expires_at | TEXT | validade do cache; NULL quando não aplicável |
| position | REAL/INTEGER | unidade documentada e não negativa |
| completed | INTEGER | 0 ou 1 com CHECK quando possível |

O dicionário deve acompanhar o schema real, incluindo nulabilidade, defaults, origem e dado sensível.
