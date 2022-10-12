# parth bansal 
# https://github.com/parthbansal05
from pytube import YouTube
import threading
from tkinter import Tk
import time

update = 0
stop = 0
link = ""
old_cpy_txt = ""


def downloader(link):
    try:
        vid_obj = YouTube(link)
        print("downloading video "+vid_obj.title)
        vid_obj = vid_obj.streams.get_highest_resolution()
        vid_obj.download()
        print("downloaded video "+vid_obj.title)
    except:
        pass
        # print(link)


while stop == 0:

    if update == 1:
        update = 0
        down_ld = threading.Thread(target=downloader, args=(link,)).start()
    cpy_txt = Tk().clipboard_get()
    if cpy_txt!="testing":
        if old_cpy_txt != cpy_txt:
            link = cpy_txt
            update = 1
        old_cpy_txt = cpy_txt

    time.sleep(1)
