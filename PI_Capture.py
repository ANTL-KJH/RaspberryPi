import time
import tkinter
import subprocess
import os
import datetime

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        return

def capFullScreen():
    now = datetime.now()
    str = now.date() + now.time()
    subprocess.call(["scrot", "/home/pi/KJH_Capture/"+str])

def capWindowScreen():
    subprocess.call(["scrot", "-s", "/home/pi/KJH_Capture/"])

def main():
    createDirectory("/home/pi/KJH_Capture")
    top = tkinter.Tk()
    top.title("PI Screen Shot")
    top.geometry("300x150")


    B = tkinter.Button(top, text="Full Screen Capture", width=50, command=capFullScreen)
    B.pack()
    B = tkinter.Button(top, text="Window Capture", width=50, command=capWindowScreen)
    B.pack()

    top.mainloop()

if __name__ == "__main__":
    main()