import yt_dlp

def download(url):
    
    ytdlp_options = {
        "outtmpl": "downloads/%(title)s.%(ext)s"
    }