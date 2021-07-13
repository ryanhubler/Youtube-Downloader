import youtube_dl

ydl_opts = {
    'postprocessors': [{
    'key': 'FFmpegVideoConvertor',
    'preferedformat': 'mp4'
}]
}
ydl_opts2 = {}

def yt_videodownload(url):
    print(url)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: #youtube_dl stuff
        ydl.download(url) 
def yt_fastdownload(url):
    print(url)
    with youtube_dl.YoutubeDL(ydl_opts2) as ydl: #youtube_dl stuff
        ydl.download(url) 