import customtkinter as ctk
import os 
import yt_dlp 
#import sys
#import subprocess
#import json
from CTkMessagebox import CTkMessagebox




# def format_selector(url):
#     sql_format_ids = [ ]
    
#     try:
#         result = subprocess.run("yt-dlp", url, "--dump-json", capture_output=True, text=True,check= True)
#         print(result)
#         data = json.loads(result.stdout)
        
#         formats = data.get("formats", [ ])
        
            
#     except subprocess.CalledProcessError as e:
#         CTkMessagebox(title="Error", message=f"{e.returncode}: {e.stderr}", icon="cancel")
            
        
#         #formats list
#     if format not in result:
#         CTkMessagebox(title="Error", message="No Available formats", icon="cancel")
    
#     for video in enumerate(result["formats"]):
#         CTkMessagebox(title="Format List", message=f"{video[0]}. {video[1]}.{video[1]["ext"]}")
#         sql_format_ids.append(video[1]["format_id"])


        
def download():
    
    download_button.configure(text="Connecting...", state="disabled")
    app.update_idletasks() 
    
    try:
        user_save_location = save_location_options.get()
        custom_name = vid_name_entry.get()    
        _url = vid_url.get()
        selected_quality = quality_menu.get()
        
        
        final_saveDirectory = path_options[user_save_location]
        # final_selectedQuality = pa
        
        if custom_name.strip() == "":
            filename_temp = "%(title)s.%(ext)s"
        else:
            filename_temp = f"{custom_name}.%(ext)s"
            
        full_save_path= f"{final_saveDirectory}/{filename_temp}"
        
        if not os.path.exists(final_saveDirectory):
            os.makedirs(final_saveDirectory)
            
            
        
    
        if selected_quality == "Data Saver":
            f_string = "bestvideo[height<=480]+bestaudio/best[height<=480]"
        elif selected_quality == "Standard":
            f_string = "bestvideo[height<=720]+bestaudio/best[height<=720]"
        else:
            f_string = "bestvideo+bestaudio/best"
        
        yt_dlp_options = {
    # 'impersonate': 'chrome',
    'format': f_string, 
    'outtmpl': full_save_path,
    'noplaylist': True,
    'merge_output_format': 'mp4', 
    'progress_hooks': [progress_hook],
}
        
        with yt_dlp.YoutubeDL(yt_dlp_options) as ydl:
            ydl.download([_url])
            
        CTkMessagebox(title="Success", message="Download Complete", icon="check")
        os.system(f'xdg-open "{final_saveDirectory}"')
    except Exception as e:
        CTkMessagebox(title="Error", message=f"Failed: {str(e)}", icon="cancel")
        
    finally:
        download_button.configure(text="Download", state="normal")
    

def progress_hook(d):
    if d['status'] == 'downloading':
        # Extract the percentage string (e.g., '52.3%')
        percent = d.get('_percent_str', '0%')
        # Remove the weird color codes if they appear
        clean_percent = percent.replace('\x1b[0;32m', '').replace('\x1b[0m', '')
        # Update the button text
        download_button.configure(text=f"Downloading: {clean_percent}")
        app.update_idletasks() # Force the GUI to refresh
    elif d['status'] == 'finished':
        download_button.configure(text="Merging...")
        app.update_idletasks()     



path_options = {
    "Desktop": os.path.expanduser("~/Desktop"),
    "Downloads": os.path.expanduser("~/Downloads/media")
}
options = list(path_options.keys()) 

#Application build 
app = ctk.CTk()
app.title('Video Downloader')
app.geometry("600x400")
app.resizable(False, False)
ctk.set_appearance_mode("system")

app.grid_columnconfigure(0,weight= 1)
app.grid_rowconfigure(0, weight= 1)
name_label = ctk.CTkLabel(app, text= "Univeral Video Downloader", font=("Cascadia Mono", 20))
name_label.grid(row = 0)


#universal downloader interface
dashboard_frame = ctk.CTkFrame(app, width= 560,height= 320, corner_radius=40)
dashboard_frame.grid(row = 1, pady = 30)
dashboard_frame.grid_propagate(False)

vid_url_label = ctk.CTkLabel(dashboard_frame, text= "Paste URL Below", font = ("Cascadia Mono", 20))
vid_url_label.pack(anchor = "w", padx = 12, pady = 10)
vid_url= ctk.CTkEntry(dashboard_frame, width= 400, placeholder_text= "Paste video link here...(e.g https://www.youtube/video)")
vid_url.pack(pady = 5)

name_row_frame = ctk.CTkFrame(dashboard_frame,fg_color= "transparent")
name_row_frame.pack(fill = "x")
entry_column_frame = ctk.CTkFrame(dashboard_frame, fg_color = "transparent")
entry_column_frame.pack(fill = "x")

vid_name_label = ctk.CTkLabel(name_row_frame, text= "Video Name (Optional)", font = ("Cascadia Mono", 20))
vid_name_label.pack(side="left", pady = 10)
vid_name_entry = ctk.CTkEntry(entry_column_frame, placeholder_text="Enter name here", width= 210)
vid_name_entry.pack(pady = 5, side = "left")

save_location_label = ctk.CTkLabel(name_row_frame, text= "SAVE LOCATION", font = ("Cascadia Mono", 20))
save_location_label.pack(side = "right")
save_location_options = ctk.CTkOptionMenu(entry_column_frame, values = options )
save_location_options.pack(side = "right")

quality_group = ctk.CTkFrame(dashboard_frame, fg_color="transparent")
quality_group.pack( padx=20, pady=10)

quality_label = ctk.CTkLabel(quality_group, text="QUALITY", font=("Cascadia Mono", 14))
quality_label.pack()

quality_menu = ctk.CTkOptionMenu(quality_group, values=["High", "Standard", "Data Saver"], width=150)
quality_menu.pack()


download_button =ctk.CTkButton(dashboard_frame, text = "Download", font=("Cascadia Mono", 20), command=download)
download_button.pack(pady = 40,anchor = "center")







app.mainloop()