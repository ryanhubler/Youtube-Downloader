from tkinter import *
from tkinter import messagebox

from ytdl import *
from viddownload import *



def yt_mp3download():
    name = [name_Tf.get()]
    yt_download(name)
    return messagebox.showinfo('message','DOWNLOAD FINISHED')
def yt_viddownload():
    name = [name_Tf.get()]
    yt_videodownload(name)
    return messagebox.showinfo('message','DOWNLOAD FINISHED')
def yt_webmdownload():
    name = [name_Tf.get()]
    yt_fastdownload(name)
    return messagebox.showinfo('message','DOWNLOAD FINISHED')
ws = Tk()
ws.title('Youtube Downloader')
ws.geometry('400x400')


    
    

Label(ws, text="Enter URL").pack()
name_Tf = Entry(ws)
namep2 = name_Tf

name_Tf.pack()

Button(ws, text="Download MP3", command=yt_mp3download).pack()
Button(ws, text="Download WEBM(FAST)", command=yt_webmdownload).pack()
Button(ws, text="Download MP4 (VERY SLOW)", command=yt_viddownload).pack()

ws.mainloop()
