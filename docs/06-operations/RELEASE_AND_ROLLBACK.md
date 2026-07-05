# Release and Rollback

## Antes

Backup do banco de teste, instalação limpa, upgrade da versão anterior, migração e smoke tests.

## Rollback

Manter artefato anterior e conhecer compatibilidade do banco. Se schema não for reversível, restaurar backup ou publicar hotfix compatível; não instalar código antigo sobre schema novo sem teste.

## Abort criteria

Segredo detectado, migração falha, ZIP incorreto, playback crítico quebrado, incompatibilidade não documentada ou hash divergente.
