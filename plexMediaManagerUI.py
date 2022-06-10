from tkinter import *
from tkinter.ttk import *
from pygame import mixer

master = Tk()
master.title('Plex Media Manager')
width = master.winfo_screenwidth()
height = master.winfo_screenheight()
mixer.init()
mixer.music.load("menuMusic.mp3")
master.geometry("500x400")

def play():

    mixer.init()
    mixer.music.load("menuMusic.mp3")
    mixer.music.play(-1)
def stop():
    mixer.music.stop()
label = Label(master,text="Welcome to Plex Media Manager")
label.pack(pady=10)
btn = Button(master,text="Click to stop music",command = stop)
btn1 = Button(master,text="Click to play music",command = play)
btn.pack()
btn1.pack()
mixer.music.play(-1)

mainloop()