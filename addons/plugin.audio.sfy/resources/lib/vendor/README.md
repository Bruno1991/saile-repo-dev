# Dependência vendorizada

O diretório recebe o pacote Python `yt_dlp` durante o processo de preparação de release.
Não copie executáveis externos. Execute `python tools/vendor_ytdlp.py --source CAMINHO` com
uma instalação local/licenciada do pacote ou configure a automação de release para obtê-lo.
