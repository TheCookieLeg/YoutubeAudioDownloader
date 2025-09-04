from yt_dlp import YoutubeDL
import os

# Ask user for playlist link
playlist_link = input("Enter the playlist link: ")

# Options for yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(r"C:\Users\TheCookieLegend\Music", '%(playlist_title)s', '%(playlist_index)s - %(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ignoreerrors': True,
    'progress_hooks': [],
    'sleep_interval': 0,
    'sleep_interval_requests': 0,
    'ratelimit': None,
    'concurrent_fragment_downloads': 5,  # speeds up downloads
}

# Hook function to print each finished song
def my_hook(d):
    if d['status'] == 'finished':
        print(f"Downloaded: {d['info_dict']['title']}")

ydl_opts['progress_hooks'].append(my_hook)

# Create the base Music folder if it doesn't exist
os.makedirs(r"C:\Users\TheCookieLegend\Music", exist_ok=True)

# Download the playlist
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_link])

print("Playlist download complete!")