import yt_dlp

# Vá ate o codigo fonte da pagina(f12), na aba network em filter, busque por .m3u0 ou .mp4 va ate o item e busque a url

url = ""

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
    'format': 'best'  # Melhor qualidade disponível
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
