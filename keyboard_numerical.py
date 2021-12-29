import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.entries = [tk.Entry(self) for i in range(4)]
        for i,e in enumerate(self.entries):
            e.grid(row=i, column=0)

        keypad_frame = tk.Frame(self)
        keypad_frame.grid(row=0, rowspan=4, column=1, sticky="eswn")

        tk.Button(keypad_frame, text="7", command=lambda: self.set_text("7")).grid(row=0, column=0)
        tk.Button(keypad_frame, text="8", command=lambda: self.set_text("8")).grid(row=0, column=1)
        tk.Button(keypad_frame, text="9", command=lambda: self.set_text("9")).grid(row=0, column=2)
        tk.Button(keypad_frame, text="4", command=lambda: self.set_text("4")).grid(row=1, column=0)
        tk.Button(keypad_frame, text="5", command=lambda: self.set_text("5")).grid(row=1, column=1)
        tk.Button(keypad_frame, text="6", command=lambda: self.set_text("6")).grid(row=1, column=2)
        tk.Button(keypad_frame, text="1", command=lambda: self.set_text("1")).grid(row=2, column=0)
        tk.Button(keypad_frame, text="2", command=lambda: self.set_text("2")).grid(row=2, column=1)
        tk.Button(keypad_frame, text="3", command=lambda: self.set_text("3")).grid(row=2, column=2)
        tk.Button(keypad_frame, text="0", command=lambda: self.set_text("0")).grid(row=3, column=1)

        self.mainloop()

    def set_text(self, text):
        widget = self.focus_get()
        if widget in self.entries:
            widget.insert("insert", text)

if __name__  == "__main__":      
    App()
