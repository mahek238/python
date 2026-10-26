import tkinter as tk
def calculate():
    try:
        res = eval(entry.get())
        result_var.set(str(res))
    except Exception as e:
            result_var.set('Err')
root = tk.Tk()
entry = tk.Entry(root); entry.pack()
tk.Button(root, text='=', command=calculate).pack()
result_var = tk.StringVar(); tk.Label(root,
textvariable=result_var).pack()
root.mainloop()