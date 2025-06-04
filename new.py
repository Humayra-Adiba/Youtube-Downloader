import tkinter
import customtkinter
import yt_dlp as youtube_dl
import threading
import os

# GUI Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader (youtube-dl)")

# Title
title = customtkinter.CTkLabel(app, text="Put a YouTube video link", text_color="yellow", font=("Arial", 25))
title.pack(padx=10, pady=8)

# Link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, placeholder_text="Paste your link here", textvariable=url)
link.pack(padx=10, pady=8)

# Progress bar
progress = customtkinter.CTkProgressBar(app, width=400)
progress.set(0)
progress.pack(padx=10, pady=(8, 2))

# Progress percentage label
progress_label = customtkinter.CTkLabel(app, text="0%", font=("Arial", 14))
progress_label.pack()

# Finish label
finish = customtkinter.CTkLabel(app, text="", text_color="green", font=("Arial", 20))
finish.pack(padx=10, pady=8)

# Custom progress hook
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0.0%').strip()
        percent_float = float(percent.replace('%', ''))
        progress.set(percent_float / 100)
        progress_label.configure(text=f"{int(percent_float)}%")
        app.update_idletasks()
    elif d['status'] == 'finished':
        finish.configure(text="Download finished", text_color="green")

# Function to start download (in thread)
def startDownload():
    ytLink = link.get()
    if not ytLink.strip():
        finish.configure(text="Please enter a valid URL", text_color="red")
        return

    title.configure(text="Downloading...", text_color="blue")
    finish.configure(text="")
    progress.set(0)
    progress_label.configure(text="0%")

    def download():
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
            'format': 'best',
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([ytLink])
        except Exception as e:
            finish.configure(text=f"Error: {str(e)}", text_color="red")

    threading.Thread(target=download).start()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=8)

# Run app
app.mainloop()
