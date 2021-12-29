import tkinter as tk
from tkinter import *
import tkinter as tkinter
from PIL import Image, ImageTk
root=Tk()
from Preload import *
import time


class MainScreen:
    def __init__(self, win):
        load_C = Label(root, bg="#eaebef", image=loadingScreen,height=450, width=800)
        load_C.image=mainScreen
        load_C.place(x=0,y=0)
        root.after(2000,self.main_Screen)
    def main_Screen(self):
        main_C = Label(root, bg="#eaebef", image=mainScreen,height=450, width=800)
        main_C.image=mainScreen
        main_C.place(x=0,y=0)

        lbl = tk.Label(root, text="00", width=5,bg='#d6dbbd',anchor='center', height=1, font=('calibri', 20, 'bold'))
        lbl.place(x=130,y=180)
        lbl1 = tk.Label(root, text="00", width=5,bg='#d6dbbd', height=1,anchor='center', font=('calibri', 20, 'bold'))
        lbl1.place(x=360,y=180)
        lbl2 = tk.Label(root, text="00", width=5,bg='#d6dbbd', height=1,anchor='center', font=('calibri', 20, 'bold'))
        lbl2.place(x=590,y=180)
        
        menu_Btn=Button(main_C,image=menuBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        menu_Btn.place(x=20,y=380)
    def menu_Screen(self):
        menu_C = Label(root, bg="#eaebef", image=menuScreen,height=450, width=800)
        menu_C.image=mainScreen
        menu_C.place(x=0,y=0)

        highPH_Btn=Button(menu_C,image=highBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        highPH_Btn.place(x=20,y=100)
        lowPH_Btn=Button(menu_C,image=lowBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        lowPH_Btn.place(x=20,y=170)
        cal4_Btn=Button(menu_C,image=cal4Btn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        cal4_Btn.place(x=20,y=240)
        cal7_Btn=Button(menu_C,image=cal7Btn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        cal7_Btn.place(x=20,y=310)

        highEC_Btn=Button(menu_C,image=highBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        highEC_Btn.place(x=270,y=100)
        lowEC_Btn=Button(menu_C,image=lowBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        lowEC_Btn.place(x=270,y=170)
        cal14_Btn=Button(menu_C,image=cal14Btn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        cal14_Btn.place(x=270,y=240)
        empty_Btn=Button(menu_C,image=emptBtn,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        empty_Btn.place(x=270,y=310)

        reset_Btn=Button(menu_C,image=resetBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        reset_Btn.place(x=540,y=100)
        reboot_Btn=Button(menu_C,image=rebootBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        reboot_Btn.place(x=540,y=170)
        graph_Btn=Button(menu_C,image=menuBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        graph_Btn.place(x=540,y=240)
        empty_Btn2=Button(menu_C,image=emptBtn,command=self.main_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        empty_Btn2.place(x=540,y=310)

##    def numPad(self):
##        from pynput.keyboard import Key, Controller
##        keyboard = Controller()
##
####        def NumKeys(i):
####            entry.inser
##            keyboard.release(str(i))
##        thresh_C = Label(root, bg="#eaebef", image=menuScreen,height=450, width=800)
##        thresh_C.image=mainScreen
##        thresh_C.place(x=0,y=0)
##        buttons=[0,0,0,0,0,0,0,0,0,0]
##        frame = Frame(root)
##        frame.place(x=10,y=10)
##        a=0
##        for j in range(3):
##            for i in range(3):
##                buttons[a]=Button(frame,text=str(a),height=3,width=5)
##                buttons[a].grid(column=i,row=j)
##                a=a+1
##        buttons[9]=Button(frame,text=str(9),height=3,width=5)
##        buttons[9].grid(column=1,row=4)
        

mywin=MainScreen(root)
root.title('Budan Farms')
root.geometry("800x450+0+0")
root.mainloop()
