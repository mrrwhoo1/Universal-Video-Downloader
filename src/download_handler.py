import yt_dlp
import os 

def download( url, output_path = "~/Downloads/multidl"):

    try:
        
        expanded_path = os.path.expanduser(output_path)
        
        if not os.path.exists(expanded_path):
            os.makedirs(expanded_path)
        url_ = url

        ytdlp_options = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{expanded_path}/%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True,
            'format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
            info_dict = ydl.extract_info(url_, download= True)
            video_title = info_dict.get('title', 'Unknown video')
            print(f"Downloaded: {video_title}")
          
            return {"success": True, "title": video_title}

    except Exception as e:
        print(f"Error: {e}")

        return {"success": False, "title": str(e)}






if __name__ == "__main__":
    download()