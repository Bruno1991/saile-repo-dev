import sys
import time
try:
    from ytmusicapi import YTMusic
    import yt_dlp
except ImportError:
    print("Por favor, instale as dependências: pip install ytmusicapi yt-dlp")
    sys.exit(1)


def main():
    print("--- PROVA TÉCNICA: ytmusicapi + yt-dlp ---")
    
    # 1. Busca ultra-rápida (ytmusicapi)
    print("\n1. Iniciando busca via ytmusicapi...")
    ytmusic = YTMusic()
    
    start_time = time.time()
    results = ytmusic.search("Linkin Park Numb", filter="songs", limit=1)
    search_time = time.time() - start_time
    
    if not results:
        print("Nenhuma música encontrada.")
        return
        
    song = results[0]
    video_id = song.get("videoId")
    title = song.get("title")
    artists = ", ".join(a.get("name") for a in song.get("artists", []))
    print(f"[OK] Busca concluída em {search_time:.2f}s")
    print(f"   - Título: {title}")
    print(f"   - Artista: {artists}")
    print(f"   - ID: {video_id}")
    
    # 2. Resolução da URL de áudio puro (yt-dlp)
    print("\n2. Resolvendo URL direta de áudio com yt-dlp...")
    url = f"https://music.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'skip_download': True,
    }
    
    start_time = time.time()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info.get("url")
        duration = info.get("duration")
    resolve_time = time.time() - start_time
    
    print(f"[OK] Resolução concluída em {resolve_time:.2f}s")
    print(f"   - Duração: {duration}s")
    print(f"   - Stream URL: {audio_url[:100]}...")
    print("\n--- SUCESSO! A prova técnica confirmou que a abordagem híbrida funciona perfeitamente! ---")

if __name__ == '__main__':
    main()
