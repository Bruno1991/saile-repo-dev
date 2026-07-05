# Provider Registry

O registry associa `provider_id` a factory e capabilities. Registro ocorre no bootstrap, sem chamada de rede. Providers indisponíveis por dependência opcional devem aparecer como não suportados, não desaparecer silenciosamente. Duplicidade de ID é erro de inicialização.
