import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

row = 1
col = 0

for b in buttons:
    if b == "=":
        tk.Button(root, text=b, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=b, width=5, height=2,
                  command=lambda x=b: click(x)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=22, command=clear).grid(row=row, column=0, columnspan=4)

root.mainloop()