#same code in gtp2.py
#it gave 32gb of file of knowledge date COA
#searched on claude
# now trying some codes


#1. Download lower quality:
import yt_dlp

def download(link):
    ydl_opts = {
        'format': 'best[height<=1080]',  # Limit to 720p or 1080p
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("Downloaded successfully!")
    except Exception as e:
        print("Error occurred:", e)


#2. Check available formats first:
def check_formats(link):
    ydl_opts = {'listformats': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(link, download=False)


#3. Download specific quality with size limit:
# def download(link):
#     ydl_opts = {
#         'format': 'best[height<=1080]',  # Under 2GB or max 1080p
#         'outtmpl': '%(title)s.%(ext)s',
#     }
    
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([link])
#             print("Downloaded successfully!")
#     except Exception as e:
#         print("Error occurred:", e)


link = input("Enter Link: ")
check_formats(link)  # Run this to see all available qualities
# download(link)