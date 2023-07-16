import numpy as np
import cv2
from tkinter import Tk, ttk, Button, Label, filedialog, Canvas, PhotoImage, simpledialog
import os
from PIL import ImageTk, Image
import tkinter as tk


root = Tk()
win = root
win.title("task 1")
win.geometry("600x600")
win.configure(bg='#CA649B')

canvas = Canvas(win, height=430, width=400, bg="#f2f1ed")
canvas.pack(pady=20)
canvas.create_rectangle(20,20,380,380,outline="#8f8881", fill="#30302e")


def selectPic():
    global img
    global filename
    global path
    global src
    global imgtk
    filename = filedialog.askopenfilename(initialdir="/Pictures")
    i = Image.open(filename)

    path =os.path.join(os.getcwd(), filename)
    img = cv2.imread(path)
    #img = img.resize((380,340))
    #img = img.resize(img,(380, 340)) 
    img=i.resize((380,340), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(Image.open(filename))
    src = cv2.imread(path)
    #img = ImageTk.PhotoImage(image=img) error
    canvas.create_image(380,340, image=img)

def rightRotate():
            global img
            img = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
            img = cv2.resize(img, (380,340),interpolation = cv2.INTER_AREA)
            img = cv2.imshow('', img)
            canvas.create_image(200,190,image=img)
            #tk.Label(win, image=img, width=380, height=320)

def downRotate():
            global img
            img = cv2.rotate(src, cv2.ROTATE_180)
            img = cv2.resize(img, (380,340),interpolation = cv2.INTER_AREA)
            img = cv2.imshow('', img)
            canvas.create_image(200,190,image=img)
            #tk.Label(win, image=img, width=380, height=320)
def leftRotate():
            global img
            img = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
            img = cv2.resize(img, (380,340),interpolation = cv2.INTER_AREA)
            img = cv2.imshow('', img)
            canvas.create_image(200,190,image=img)
            #tk.Label(win, image=img, width=380, height=320)

def upRotate():
            global img
            img = cv2.rotate(src, cv2.ROTATE_180)
            img = cv2.rotate(src, cv2.ROTATE_180)
            img = cv2.resize(img, (380,340),interpolation = cv2.INTER_AREA)
            img = cv2.imshow('', img)
            canvas.create_image(200,190,image=img)
            #tk.Label(win, image=img, width=380, height=320)

onImg = Image.open("/Users/AEliP/Downloads/switchOn.png")
on = onImg.resize((60,30), Image.Resampling.LANCZOS)
myOn = ImageTk.PhotoImage(on)

offImg = Image.open("/Users/AEliP/Downloads/switchOff.png")
off = offImg.resize((60,30), Image.Resampling.LANCZOS)
myOff = ImageTk.PhotoImage(off)


def switch():
    global is_on
    global imgtk
    # Determine is on or off
    if is_on:
        onBtn.config(image=myOff)
        is_on=False
        #Image.fromarray(None)
        #tk.Label.destroy()
        imgtk =cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        b,g,r = cv2.split(imgtk)
        imgtk = cv2.merge((r,g,b))
        imgtk = Image.fromarray(imgtk)
        imgtk = ImageTk.PhotoImage(image=imgtk)
       
        tk.Label(win, image=imgtk, width=380, height=320).pack() 
        #canvas.create_image(50,50, image=img)
        #cv2.waitKey(1)
    else:
        onBtn.config(image=myOn)
        is_on=True
        #tk.Label.destroy()
        imgtk =cv2.cvtColor(src, cv2.COLOR_HSV2BGR)
        b,g,r = cv2.split(imgtk)
        imgtk = cv2.merge((r,g,b))
        imgtk = Image.fromarray(imgtk)
        imgtk = ImageTk.PhotoImage(image=imgtk)
        tk.Label(win, image=imgtk, width=380, height=320).pack() 
        #cv2.waitKey(1)

upl = Image.open("/Users/AEliP/Downloads/button.png")
upload = upl.resize((60,60), Image.Resampling.LANCZOS)
myUpload = ImageTk.PhotoImage(upload) 

uploadBtn = Button(win, image=myUpload, bg="#CA649B", activeforeground='white',activebackground='#CA649B',borderwidth=0, command=selectPic).place(x=410, y=470, height=60 ,width=60)

upBtn=Button(win, text="🢁", bd=0,bg="#CA649B",activeforeground='white',activebackground='#CA649B',borderwidth=0,command=upRotate).place(x=125, y=470)
#upBtn.pack()
rightBtn=Button(win, text="🢂",bd=0,bg="#CA649B",activeforeground='white',activebackground='#CA649B',borderwidth=0, command=rightRotate).place(x=150, y=490)
#rightBtn.pack()
downBtn=Button(win, text="🢃", bd=0,bg="#CA649B",activeforeground='white',activebackground='#CA649B',borderwidth=0,command=downRotate).place(x=125, y=510)
#downBtn.pack()
leftBtn=Button(win, text="🢀", bd=0,bg="#CA649B",activeforeground='white',activebackground='#CA649B',borderwidth=0,command=leftRotate).place(x=100, y=490)
#leftBtn.pack()

onBtn = Button(win,image=myOn, bd=0,bg="#CA649B", command=switch, activebackground='#CA649B', borderwidth=0)
onBtn.pack(pady=40)

win.mainloop()
cv2.waitKey(0)
cv2.destroyAllWindows()