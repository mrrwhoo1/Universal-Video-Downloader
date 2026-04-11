# 🚀 MultiDL (Universal Video Downloader)

**Version 2.0**

A fast, modern **multi-platform video downloader** built with Python and CustomTkinter.
Simply paste a link and download videos instantly — clean, lightweight, and distraction-free.

---

## 🔥 Why This Project Exists

Most video downloaders today are:

* ❌ Filled with ads and popups
* ❌ Limited to a single platform
* ❌ Closed-source and not customizable
* ❌ Overcomplicated for simple tasks

**MultiDL was built to solve that.**

✅ No ads
✅ Fully open-source
✅ Supports multiple platforms
✅ Simple “paste and download” workflow
✅ Built for learning, automation, and real-world use

---

## ✨ Features

* 🎯 **Multi-Platform Support**
  Download from YouTube, TikTok, Instagram, Facebook, and more.

* ⚡ **One-Click Download**
  Paste a link and start downloading instantly.

* 📊 **Smart Quality Presets**

  * **High Quality** – Best available resolution
  * **Standard (720p)** – Balanced quality & size
  * **Data Saver (480p)** – Optimized for low data usage

* 🔄 **Automatic Audio + Video Merge**
  Uses FFmpeg to combine streams into a single `.mp4` file.

* 📈 **Live Progress Feedback**
  Real-time percentage updates directly in the UI.

* 🐧 **Linux Friendly**
  Automatically opens the download folder using `xdg-open`.

* 🧠 **Beginner-Friendly Codebase**
  Clean structure for learning GUI apps, subprocesses, and automation.

---

## 🖼️ Screenshots

### Simple UI

<img width="1016" height="730" src="https://github.com/user-attachments/assets/09d2bade-992d-4e9a-9eb5-69b1e097eeee" />

### Download Progress Indicator

<img width="917" height="591" src="https://github.com/user-attachments/assets/bbfaffa2-edbc-4c5d-bc18-2b9f20bf4118" />

### Auto-Open Download Folder

<img width="1526" height="777" src="https://github.com/user-attachments/assets/0842b860-514e-4b44-bd0f-61fc24534aa6" />

### About Page

<img width="900" height="581" src="https://github.com/user-attachments/assets/36976c4b-3054-4adf-8940-1bc714fb70fa" />

---

## 🛠️ Built With

* **Python 3**
* **CustomTkinter** – GUI framework
* **yt-dlp** – Media download engine
* **FFmpeg** – Audio/video processing
* **PyInstaller** – Executable packaging

---

## 📥 Installation (Linux – Ubuntu/Fedora)

### 1. Clone the Repository

```bash
git clone https://github.com/mrrwhoo1/Universal-Video-Downloader.git
cd Universal-Video-Downloader
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

```bash
sudo apt update
sudo apt install ffmpeg -y
```

---

## 🚀 Usage

```bash
python3 main.py
```


---

## 📦 Build Executable

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --hidden-import="PIL._tkinter_finder" --name "UniversalDownloader" script.py
```

The compiled application will be available in the `dist/` folder.

---

## ⚠️ Disclaimer

This project is intended for **educational and personal use only**.

* Users are responsible for complying with the terms of service of supported platforms
* Do not use this tool to download copyrighted content without permission
* The developer is not responsible for misuse of this software

---

## 👨‍💻 About the Developer

**Maron H. Chilomo**
Computer Science Student – Cavendish University, Zambia

Interested in:

* Python development
* Automation tools
* GUI applications
* Real-world problem solving through code

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it and improve it
* 🛠️ Contribute ideas or features

---

## 🔗 Connect With Me

* GitHub: https://github.com/mrrwhoo1
* Instagram: https://www.instagram.com/mrr_whoo/
