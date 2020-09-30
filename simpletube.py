from pytube import YouTube
import os
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry('500x300')
root.title("SimpleTube")
inst1=Label(root,text="Paste the Youtube url", font=("bold",15))
inst1.place(x=150,y=150)

canvas=Canvas(root,width=110,height=110)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\dhanush\\Desktop\\icon.png"))
canvas.create_image(10,0,anchor=NW,image=image)
canvas.pack()


mylink=StringVar()
pastelink=Entry(root, width=50, textvariable=mylink)
pastelink.place(x=100,y=200)


def downloadVideo():
    x=str(mylink.get())
    ytvideo= YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('./ytdownload'):
        os.makedirs('./ytdownload')
    ytvideo.download('./ytdownload')

button1=Button(root,text="Download", width=10,bg="green",fg="yellow",command=downloadVideo)
button1.place(x=200,y=250)

root.mainloop()