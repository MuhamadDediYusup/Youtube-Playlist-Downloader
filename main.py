import yt_dlp
import os

def download_playlist(playlist_url, output_path, format_choice):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        if format_choice == 'mp4':
            ydl_opts = {
                'outtmpl': f'{output_path}/%(title)s.%(ext)s', 
                'format': 'bestvideo+bestaudio/best',
            }
        elif format_choice == 'mp3':
            ydl_opts = {
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',  
                'format': 'bestaudio/best', 
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:  # Format asli
            ydl_opts = {
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',  
                'format': 'best',
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading playlist: {playlist_url}")
            ydl.download([playlist_url])

        print("All videos downloaded successfully.")

    except Exception as e:
        print(f"Error processing playlist: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")

    output_path = input("Enter the output folder (default: ./downloads): ") or "./downloads"

    print("Choose format:")
    print("1. MP4 (video)")
    print("2. MP3 (audio only)")
    print("3. Original format")
    format_choice = input("Enter your choice (1/2/3): ")

    if format_choice == '1':
        format_choice = 'mp4'
    elif format_choice == '2':
        format_choice = 'mp3'
    else:
        format_choice = 'original'

    download_playlist(playlist_url, output_path, format_choice)
