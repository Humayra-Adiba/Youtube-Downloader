
import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError

# Function to update progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress.set(percentage_of_completion / 100)
    progress_label.configure(text=f"{int(percentage_of_completion)}%")
    app.update_idletasks()

# Function to download the video
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="blue")
        finish.configure(text="")

        video.download()
        finish.configure(text="Download finished", text_color="green")
    except RegexMatchError:
        finish.configure(text="Error: Invalid YouTube URL", text_color="red")
    except Exception as e:
        finish.configure(text=f"Error: {str(e)}", text_color="red")

# GUI Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame 
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Title
title = customtkinter.CTkLabel(app, text="Put a YouTube video link", text_color="yellow", font=("Arial", 25))
title.pack(padx=10, pady=8)

# Link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, placeholder_text="Paste your link here", textvariable=url)
link.pack(padx=10, pady=8)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=8)

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

# Run app
app.mainloop()

