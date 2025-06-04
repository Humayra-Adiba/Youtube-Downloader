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

## Run with `main.exe` (Recommended for Windows)

No setup needed! Just run:

```
main.exe
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
├── main.py               # Main Python script
├── main.exe              # Standalone Windows executable
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── icon.ico              # Optional app icon (used in .exe)
```

---


