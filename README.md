# Universal Video Downloader 🚀

**A "Paste and Forget" media downloader built with Python and CustomTkinter.**

This application allows users to download videos from YouTube, TikTok, Instagram, and Facebook while managing data consumption through built-in quality presets. It uses the powerful yt_dpl engine.

## ✨ Features

* **Universal Compatibility:** Supports YouTube, TikTok, Instagram, Facebook, and more.
* **Data Saving Presets:** * **High Quality:** Best available resolution.
* **Standard (720p):** Balanced quality and size.
* **Data Saver (480p):** Optimized for low data usage.


* **Real-time Feedback:** The download button transforms to show a live percentage progress.
* **Auto-Merge:** Automatically merges high-quality video and audio into a single `.mp4` using FFmpeg.
* **Ubuntu Optimized:** Native support for `xdg-open` to reveal your downloads immediately.

## 🛠️ Built With

* **Language:** Python 3
* **GUI:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Engine:** [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* **Processing:** FFmpeg (Required for merging)
* **Packaging:** PyInstaller

## 📥 Installation (Ubuntu/Linux)

### 1. Clone the Repository

```bash
git clone https://github.com/mrrwhoo1/Universal-Video-Downloader.git
cd Universal-Video-Downloader

```

### 2. Install Dependencies

It is recommended to use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

### 3. Install FFmpeg

FFmpeg is required to merge high-quality video and audio streams:

```bash
sudo apt update && sudo apt install ffmpeg -y

```

## 🚀 Usage

Run the script directly:

```bash
python3 script.py

```

## 📦 Creating an Executable

To build your own standalone binary on Ubuntu:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --hidden-import="PIL._tkinter_finder" --name "UniversalDownloader" script.py

```

The finished app will be located in the `dist/` folder.

---

## 👨‍💻 About the Developer

I am **Maron H. Chilomo**, a second-year Computer Science student at **Cavendish University**, Zambia. This project was developed to simplify the process of media extraction and to explore GUI development and subprocess management in Python.

**Connect with me:**

* GitHub: [@mrrwhoo1](https://www.google.com/search?q=https://github.com/mrrwhoo1)
