import customtkinter as ctk
import os 
import yt_dlp 
import re
from PIL import Image
from CTkMessagebox import CTkMessagebox


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


BG_COLOR       = "#0D1117"   
SIDEBAR_COLOR  = "#161B22"   
CARD_COLOR     = "#1C2230"  
ACCENT_COLOR   = "#6E56CF"   
ACCENT_HOVER   = "#7F6BE8"   
MUTED_TEXT     = "#8B949E"   
BORDER_COLOR   = "#2D3748"   
PROGRESS_COLOR = "#6E56CF"   


# --- LOGIC FUNCTIONS ---

def show_about():
    main_view.pack_forget()
    about_view.pack(fill="both", expand=True, padx=30, pady=20)

def show_downloader():
    about_view.pack_forget()
    main_view.pack(fill="both", expand=True, padx=30, pady=20)

def download():
    download_button.configure(text="Connecting...", state="disabled")
    progress_bar.set(0)
    app.update_idletasks() 
    try:
        user_save_location = save_location_options.get()
        custom_name = vid_name_entry.get()    
        _url = vid_url.get()
        selected_quality = quality_menu.get()
        final_saveDirectory = path_options[user_save_location]
        
        filename_temp = f"{custom_name}.%(ext)s" if custom_name.strip() != "" else "%(title)s.%(ext)s"
        full_save_path = f"{final_saveDirectory}/{filename_temp}"
        
        if not os.path.exists(final_saveDirectory): os.makedirs(final_saveDirectory)
    
        if selected_quality == "Data Saver": f_string = "bestvideo[height<=480]+bestaudio/best[height<=480]"
        elif selected_quality == "Standard": f_string = "bestvideo[height<=720]+bestaudio/best[height<=720]"
        else: f_string = "bestvideo+bestaudio/best"
        
        yt_dlp_options = {
            'format': f_string, 'outtmpl': full_save_path, 'noplaylist': True,
            'merge_output_format': 'mp4', 'progress_hooks': [progress_hook],
        }
        
        with yt_dlp.YoutubeDL(yt_dlp_options) as ydl:
            ydl.download([_url])
            
        progress_bar.set(1)
        CTkMessagebox(title="Success", message="Download Complete", icon="check")
        os.system(f'xdg-open "{final_saveDirectory}"')
    except Exception as e:
        CTkMessagebox(title="Error", message=f"Failed: {str(e)}", icon="cancel")
    finally:
        download_button.configure(text="Start Download", state="normal")

def progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0%')
        clean_percent = re.sub(r'\x1b\[[0-9;]*m', '', percent_str).replace('%', '')
        try:
            progress_bar.set(float(clean_percent) / 100)
            download_button.configure(text=f"Downloading {clean_percent.strip()}%")
        except: pass
        app.update_idletasks()
    elif d['status'] == 'finished':
        download_button.configure(text="Merging Files...")
        progress_bar.set(1)

# --- UI SETUP ---------------------------------------------------
path_options = {"Desktop": os.path.expanduser("~/Desktop"), "Downloads": os.path.expanduser("~/Downloads/media")}
app = ctk.CTk()
app.title('Universal Video Downloader')
app.geometry("900x550")
app.resizable(False, False)
app.configure(fg_color=BG_COLOR)

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# SIDEBAR---------------------------------------------------------------
sidebar = ctk.CTkFrame(app, width=200, corner_radius=0, fg_color=SIDEBAR_COLOR, border_color=BORDER_COLOR, border_width=1)
sidebar.grid(row=0, column=0, sticky="nsew")


try:
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "image.png")
    app_logo = ctk.CTkImage(light_image=Image.open(logo_path), dark_image=Image.open(logo_path), size=(100, 100))
    ctk.CTkLabel(sidebar, image=app_logo, text="").pack(pady=30)
except:
    ctk.CTkLabel(sidebar, text="UVD", font=("Cascadia Mono", 24, "bold"), text_color=ACCENT_COLOR).pack(pady=30)

# Sidebar Buttons
ctk.CTkButton(sidebar, text="⬇  Downloader", fg_color="transparent", hover_color=CARD_COLOR,
              border_width=1, border_color=BORDER_COLOR, text_color="white",
              corner_radius=8, command=show_downloader).pack(padx=20, pady=6, fill="x")
ctk.CTkButton(sidebar, text="👤  About", fg_color="transparent", hover_color=CARD_COLOR,
              border_width=1, border_color=BORDER_COLOR, text_color="white",
              corner_radius=8, command=show_about).pack(padx=20, pady=6, fill="x")

# --- RIGHT SIDE CONTAINER --------------------------------------------------------------
container = ctk.CTkFrame(app, fg_color="transparent")
container.grid(row=0, column=1, sticky="nsew")

# 1. DOWNLOADER  FRaME
main_view = ctk.CTkFrame(container, fg_color="transparent")
main_view.pack(fill="both", expand=True, padx=30, pady=20)

url_card = ctk.CTkFrame(main_view, fg_color=CARD_COLOR, corner_radius=12, border_color=BORDER_COLOR, border_width=1)
url_card.pack(fill="x", pady=(0, 20), ipady=10)
ctk.CTkLabel(url_card, text="Video Link", font=("Cascadia Mono", 16, "bold"), text_color="white").pack(anchor="w", padx=20, pady=5)
vid_url = ctk.CTkEntry(url_card, placeholder_text="Paste URL here...", height=40,
                       fg_color="#10151E", border_color=BORDER_COLOR, text_color="white")
vid_url.pack(fill="x", padx=20, pady=10)

settings_card = ctk.CTkFrame(main_view, fg_color=CARD_COLOR, corner_radius=12, border_color=BORDER_COLOR, border_width=1)
settings_card.pack(fill="x", pady=0, ipady=10)
settings_card.grid_columnconfigure((0, 1, 2), weight=1)

vid_name_entry = ctk.CTkEntry(settings_card, placeholder_text="Filename (Optional)",
                               fg_color="#10151E", border_color=BORDER_COLOR, text_color="white")
vid_name_entry.grid(row=0, column=0, padx=15, pady=20, sticky="ew")
quality_menu = ctk.CTkOptionMenu(settings_card, values=["High", "Standard", "Data Saver"],
                                  fg_color=ACCENT_COLOR, button_color=ACCENT_HOVER, text_color="white")
quality_menu.grid(row=0, column=1, padx=15, pady=20, sticky="ew")
save_location_options = ctk.CTkOptionMenu(settings_card, values=list(path_options.keys()),
                                           fg_color=ACCENT_COLOR, button_color=ACCENT_HOVER, text_color="white")
save_location_options.grid(row=0, column=2, padx=15, pady=20, sticky="ew")

progress_bar = ctk.CTkProgressBar(main_view, height=8, corner_radius=4,
                                   fg_color=CARD_COLOR, progress_color=ACCENT_COLOR)
progress_bar.set(0)
progress_bar.pack(fill="x", pady=20)
download_button = ctk.CTkButton(main_view, text="Start Download", height=50,
                                 font=("Cascadia Mono", 18, "bold"), command=download,
                                 fg_color=ACCENT_COLOR, hover_color=ACCENT_HOVER,
                                 corner_radius=10, text_color="white")
download_button.pack(fill="x")

# 2. ABOUT VIEW frame
about_view = ctk.CTkFrame(container, fg_color="transparent")

profile_card = ctk.CTkFrame(about_view, fg_color=CARD_COLOR, corner_radius=16,
                             border_color=BORDER_COLOR, border_width=1)
profile_card.pack(pady=20, padx=20, fill="both", expand=True)


ctk.CTkLabel(profile_card, text="Built by", font=("Cascadia Mono", 13),
             text_color=MUTED_TEXT).pack(pady=(30, 2))
ctk.CTkLabel(profile_card, text="Maron H. Chilomo", font=("Cascadia Mono", 26, "bold"),
             text_color="white").pack()


ctk.CTkFrame(profile_card, height=1, fg_color=BORDER_COLOR).pack(fill="x", padx=40, pady=18)


info_items = [
    "Cavendish University Zambia",

    "Contact: +260972124354\n\n"
    "github.com/mrrwhoo1",
]
for detail in info_items:
    row = ctk.CTkFrame(profile_card, fg_color="transparent")
    row.pack(anchor="center", pady=4)
    # ctk.CTkLabel(row, text=icon, font=("Cascadia Mono", 16)).pack(side="left", padx=(0, 10))
    ctk.CTkLabel(row, text=detail, font=("Cascadia Mono", 14), text_color=MUTED_TEXT).pack(side="left")

# Divider
ctk.CTkFrame(profile_card, height=1, fg_color=BORDER_COLOR).pack(fill="x", padx=40, pady=18)

ctk.CTkButton(profile_card, text="← Back to Downloader", command=show_downloader,
              fg_color=ACCENT_COLOR, hover_color=ACCENT_HOVER, corner_radius=8,
              font=("Cascadia Mono", 13, "bold")).pack(pady=(0, 30))

app.mainloop()