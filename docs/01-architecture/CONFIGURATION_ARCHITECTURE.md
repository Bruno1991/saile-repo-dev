# Configuration Architecture

Settings do Kodi são a interface de configuração. A camada de configuração converte strings em tipos, valida hosts, remove barras inconsistentes e nunca retorna segredo em `repr` ou log.

Defaults não podem habilitar comportamento remoto sensível. Alterações que invalidam cache devem acionar invalidação seletiva. IDs de settings publicados são contratos e exigem migração quando renomeados.
