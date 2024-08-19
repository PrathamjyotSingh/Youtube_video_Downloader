import yt_dlp

def download_video(url, path='.'):
    try:
        print(f"Attempting to download from URL: {url}")
        
        # Create a YTDLP object
        ydl_opts = {
            'outtmpl': f'{path}/%(title)s.%(ext)s',  # Save video with title as filename
            'format': 'best',  # Download the best available quality
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Download completed! Video saved to '{path}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = 'https://www.youtube.com/watch?v=a3ICNMQW7Ok'  # Replace with your video URL
download_path = r'C:\Users\jyotp\Videos'  # Use raw string to handle backslashes in Windows paths
download_video(video_url, download_path)
