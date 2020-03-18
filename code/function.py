import tkinter as tk
from math import fabs
from math import pi
import math

def sin(x):
    g = 0
    t = x
    n = 1
    while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return g

def cos(x):
    x = 1.57079 - x
    return sin(x)

def tan(x):
    return sin(x)/cos(x)

def cot(x):
    return cos(x)/sin(x)

window = tk.Tk()
window.title("trigonometric function")
window.geometry("300x200")

e = tk.Entry(window,
             width=20,
             bg="tan")
e.pack()

def compute_sin():
    t.delete('1.0', 'end')
    var = float(e.get())
    result = sin(var)
    t.insert("end", result)

def compute_cos():
    t.delete('1.0', 'end')
    var = float(e.get())
    result = cos(var)
    t.insert("end", result)

def compute_tan():
    t.delete('1.0', 'end')
    var = float(e.get())
    if cos(var)==0:
        t.insert("end", "error")
    else:
        result = tan(var)
        t.insert("end", result)

def compute_cot():
    t.delete('1.0', 'end')
    var = float(e.get())
    if sin(var)==0:
        t.insert("end", "error")
    else:
        result = cot(var)
        t.insert("end", result)

b1 = tk.Button(window,
               text="sin",
               # width=15,height=2,
               width=15, height=1,
               command=compute_sin, )
b1.pack()

b2 = tk.Button(window,
               text="cos",
               width=15, height=1,
               command=compute_cos)
b2.pack()

b3 = tk.Button(window,
               text="tan",
               width=15, height=1,
               command=compute_tan)
b3.pack()

b4 = tk.Button(window,
               text="cot",
               width=15, height=1,
               command=compute_cot)
b4.pack()

t = tk.Text(window,
            width=20, height=2,
            bg="gray"
            )
t.pack()

window.mainloop()


