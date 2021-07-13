import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best', #quality settings
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

def yt_download(url):
    print(url)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: #youtube_dl stuff
        ydl.download(url) 