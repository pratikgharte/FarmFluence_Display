import tkinter as tk
from tkinter import *
import tkinter as tkinter
from PIL import Image, ImageTk
import os

global mainScreen,menuScreen, menuBtn,cal14Btn ,calBtn ,emptBtn, graphBtn
global highBtn ,lowBtn ,rebootBtn ,resetBtn

loadingScreen=Image.open("/home/pi/python_AtlasOEM_lib/data/loadingScreen.PNG")
loadingScreen=loadingScreen.resize((800,450), Image.ANTIALIAS)
loadingScreen=ImageTk.PhotoImage(loadingScreen)

mainScreen=Image.open("/home/pi/python_AtlasOEM_lib/data/mainScreen.PNG")
mainScreen=mainScreen.resize((800,450), Image.ANTIALIAS)
mainScreen=ImageTk.PhotoImage(mainScreen)

menuScreen= Image.open("/home/pi/python_AtlasOEM_lib/data/menuScreen.PNG")
menuScreen=menuScreen.resize((800,450), Image.ANTIALIAS)
menuScreen=ImageTk.PhotoImage(menuScreen)

menuBtn= Image.open("/home/pi/python_AtlasOEM_lib/data/menuBtn.PNG")
menuBtn=menuBtn.resize((150,50), Image.ANTIALIAS)
menuBtn = ImageTk.PhotoImage(menuBtn)

cal14Btn= Image.open("/home/pi/python_AtlasOEM_lib/data/cal1413Btn.PNG")
cal14Btn=cal14Btn.resize((150,50), Image.ANTIALIAS)
cal14Btn = ImageTk.PhotoImage(cal14Btn)

cal4Btn= Image.open("/home/pi/python_AtlasOEM_lib/data/calBtn.PNG")
cal4Btn=cal4Btn.resize((150,50), Image.ANTIALIAS)
cal4Btn = ImageTk.PhotoImage(cal4Btn)

cal7Btn= Image.open("/home/pi/python_AtlasOEM_lib/data/cal7Btn.PNG")
cal7Btn=cal7Btn.resize((150,50), Image.ANTIALIAS)
cal7Btn = ImageTk.PhotoImage(cal7Btn)

emptBtn= Image.open("/home/pi/python_AtlasOEM_lib/data/emptBtn.PNG")
emptBtn=emptBtn.resize((150,50), Image.ANTIALIAS)
emptBtn = ImageTk.PhotoImage(emptBtn)

graphBtn= Image.open("/home/pi/python_AtlasOEM_lib/data/graphBtn.PNG")
graphBtn=graphBtn.resize((150,50), Image.ANTIALIAS)
graphBtn = ImageTk.PhotoImage(graphBtn)

#highBtn= Image.open("/home/pi/python_AtlasOEM_lib/data/highBtn.PNG")
#highBtn=highBtn.resize((150,50), Image.ANTIALIAS)
#highBtn = ImageTk.PhotoImage(highBtn)

#lowBtn= Image.open("/home/pi/python_AtlasOEM_lib/data/lowBtn.PNG")
#lowBtn=lowBtn.resize((150,50), Image.ANTIALIAS)
#lowBtn = ImageTk.PhotoImage(lowBtn)

rebootBtn= Image.open("/home/pi/python_AtlasOEM_lib/data/rebootBtn.PNG")
rebootBtn=rebootBtn.resize((150,50), Image.ANTIALIAS)
rebootBtn = ImageTk.PhotoImage(rebootBtn)

resetBtn= Image.open("/home/pi/python_AtlasOEM_lib/data/resetBtn.PNG")
resetBtn=resetBtn.resize((150,50), Image.ANTIALIAS)
resetBtn = ImageTk.PhotoImage(resetBtn)
