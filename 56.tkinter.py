import tkinter as tk
root = tk.Tk()
tk.Label(root, text='Name').pack()
e = tk.Entry(root); e.pack()
tk.Button(root, text='Click', command=lambda: print(e.get())).pack()
root.mainloop()