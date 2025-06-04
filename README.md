#  YouTube Downloader (GUI) using yt-dlp

A simple, user-friendly desktop YouTube downloader built with Python. This GUI-based tool uses `yt-dlp` and `customtkinter` to let you download YouTube videos (including Shorts) with one click.

---

## ✨ Features

-  Download videos in best available quality
-  Real-time download progress bar with percentage
-  Supports YouTube Shorts
-  Standalone `.exe` available (no Python required)
-  GUI built with `customtkinter`
-  Handles invalid URLs and common errors

---

## Run with `yt_downloader.exe` (Recommended for Windows)

No setup needed! Just run:

```
yt_downloader.exe
```

>  No Python installation required  
>  Works out-of-the-box on Windows

---

##  Run with Python (For Developers)

###  Requirements

- Python 3.7 or higher
- pip packages listed in `requirements.txt`

###  Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
python main.py
```

---

##  Build Your Own Executable

Want to create a standalone `.exe` yourself?

### Using PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

> Make sure `ffmpeg` is installed and added to PATH for best results.

---

##  Project Structure

```
Youtube-Downloader/
├── .gitignore             # Git ignored files
├── LICENSE                # MIT License
├── README.md              # Project documentation
├── icon.ico               # Application icon
├── new.py                 # Older version using youtube_dl (archived)
├── requirements.txt       # Python dependencies
├── yt-dlp.py              # Main application using yt-dlp
├── yt_downloader.exe      # Compiled Windows executable
```

---


