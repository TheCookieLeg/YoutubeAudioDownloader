from yt_dlp import YoutubeDL
import os

output_folder = r"C:\Users\TheCookieLegend\Music"

playlist_link = "https://www.youtube.com/playlist?list=PLbWyUSpYqZfHJ8E2RmIE5Kz52aEAqb1dO"

# Only download items 348-352
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(playlist_title)s', '%(playlist_index)s - %(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ignoreerrors': True,
    'progress_hooks': [],
    'playlist_items': '340-343',  
}

def my_hook(d):
    if d['status'] == 'finished':
        print(f"Downloaded: {d['info_dict']['title']}")

ydl_opts['progress_hooks'].append(my_hook)
os.makedirs(output_folder, exist_ok=True)

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_link])