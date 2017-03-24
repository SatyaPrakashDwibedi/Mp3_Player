import mp3play as mp3
from time import sleep
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *

root=Tk()
showinfo("Info...",message="Choose File To Be Opened")
f=askopenfile(parent=root,mode='rb',title="Sweet Heart Choose File....")
clip=mp3.load(f.name)
clip.play()
sleep(clip.seconds())
clip.stop()
root.destroy()
