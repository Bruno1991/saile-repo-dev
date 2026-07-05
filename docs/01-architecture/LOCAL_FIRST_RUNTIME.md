# Local-First Runtime

## Estado primário

Perfis, favoritos, histórico, progresso, cache e preferências são locais. O usuário deve conseguir remover, exportar ou reconstruir o estado quando aplicável.

## Rede

Rede enriquece o estado, não controla a inicialização do add-on. Menus essenciais e settings devem abrir mesmo com provider indisponível.

## Sincronização

Qualquer sincronização entre dispositivos é opt-in, iniciada pelo usuário e fora do baseline atual. Não anunciar descoberta LAN nem transmitir banco automaticamente.

## Recuperação

Banco danificado deve ser preservado para diagnóstico, copiado antes de reparo e reconstruído apenas com confirmação ou política documentada.
