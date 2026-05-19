import yt_dlp
import os 

def download( url,progress_hook = None ,output_path = "~/Downloads/multidl"):

    try:
        
        expanded_path = os.path.expanduser(output_path)
        
        if not os.path.exists(expanded_path):
            os.makedirs(expanded_path)
        url_ = url

        ytdlp_options = {
                        'format': 'bestvideo+bestaudio/best',
                        'merge_output_format': 'mp4',
                        'outtmpl': f'{expanded_path}/%(title)s.%(ext)s',
                        'keepvideo': False,
                        'quiet': True,
                        'no_warnings': True,
                        'noplaylist': True,
                        'noprogress': False,  # ADD THIS — ensures progress hooks fire
                        'progress_hooks': [progress_hook] if progress_hook else []
                    }

        
        with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
            info_dict = ydl.extract_info(url_, download= True)
            video_title = info_dict.get('title', 'Unknown video')

            filename = ydl.prepare_filename(info_dict)



            print(f"Downloaded: {video_title}")
          
            return {"success": True, 
                    "title": video_title, 
                     "file_path": filename}

    except Exception as e:
        print(f"Error: {e}")

        return {"success": False, "title": str(e)}






if __name__ == "__main__":
    download()