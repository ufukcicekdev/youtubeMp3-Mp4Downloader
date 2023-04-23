import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from pytube import YouTube
import os



def Download(link,yt_format):
    youtubeObject = YouTube(link)
    try:
        if yt_format == "Mp3":
            youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
            destination = str("DownLoadMp3List")
            out_file = youtubeObject.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'

        elif yt_format == "Mp4":
            youtubeObject = youtubeObject.streams.filter().get_highest_resolution()
            destination = str("DownLoadMp4List")
            out_file = youtubeObject.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
        os.rename(out_file, new_file)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


def insert_row():
    name = name_entry.get()
    subscription_status = status_combobox.get()
    print(name, subscription_status)
    Download(name,subscription_status)


def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

root = tk.Tk()
root.title("Youtube Downloader")
style = ttk.Style(root)
root.tk.call("source","forest-light.tcl")
root.tk.call("source","forest-dark.tcl")

style.theme_use("forest-dark")


frame = ttk.Frame(root)
frame.pack()


widgets_frame = ttk.LabelFrame(frame,text = "Youtube Link")
widgets_frame.grid(row=0,column=0,padx=20, pady=10)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Link")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
name_entry.grid(row=0, column=0,sticky="ew")



combo_list = ["Mp3", "Mp4"]

status_combobox = ttk.Combobox(widgets_frame, values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=2, column=0, padx=5, pady=5,  sticky="ew")


button = ttk.Button(widgets_frame, text="Download", command=insert_row)
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")


mode_switch = ttk.Checkbutton(
    widgets_frame, text="Mode", style="Switch", command=toggle_mode)
mode_switch.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")



root.mainloop()