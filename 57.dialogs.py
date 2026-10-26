import tkinter as tk
from tkinter import messagebox as mb
root = tk.Tk()
def on_quit():
 if mb.askyesno('Verify','Really quit?'):
    mb.showinfo('Quit','Exiting now')
 root.destroy()
tk.Button(root, text='Quit', command=on_quit).pack()
root.mainloop()