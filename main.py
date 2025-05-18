import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame 
app= customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# adding UI elements
title = customtkinter.CTkLabel(app, text="Put a youtube video link")
title.pack(padx=10, pady=8)

# run app
app.mainloop()
