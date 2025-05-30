import yt_dlp

def download(link):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # High quality MP4
        'outtmpl': '%(title)s.%(ext)s',  # Save as video title
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("Downloaded successfully!")
    except Exception as e:
        print("Error occurred:", e)

link = input("Enter Link: ")
download(link)
