import tkinter as tk
from math import fabs
from math import pi
from tkinter import messagebox


#trigonometric functions
def radian2angle(x):
    return 180*x/(pi)

def angle2radian(x):
    return x*(pi)/180

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
window.geometry("320x400")

flag = 0
def p_program():
    global flag
    flag = 0
    tk.messagebox.showinfo(title='programming language', message='you have selected python!')

def m_program():
    global flag
    flag = 1
    tk.messagebox.showinfo(title='programming language', message='you have selected M language!')

#top menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)  # tearoff 可以单独出来
menubar.add_cascade(label='Options', menu=filemenu)
filemenu.add_command(label='Python Language', command=p_program)
filemenu.add_command(label='M Language', command=m_program)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
window.config(menu=menubar)

tk.Label(window, text='请输入要计算的数: ').place(x=30, y=40)
tk.Label(window, text='弧度').place(x=165, y=10)
tk.Label(window, text='角度').place(x=245, y=10)


#input number
var_radian_input = tk.StringVar()
entry_radian_input = tk.Entry(window,
                              textvariable=var_radian_input,
                              width=8,bg="tan")
entry_radian_input.place(x=150, y=40)

var_angle_input = tk.StringVar()
entry_angle_input = tk.Entry(window,
                              textvariable=var_angle_input,
                              width=8,bg="tan")
entry_angle_input.place(x=230, y=40)

#弧度和角度之间转换
def convert():
    if (entry_radian_input.get() == "")&(entry_angle_input.get() == ""):
        radian_value = float(entry_radian_input.get())
        angle_value = float(entry_angle_input.get())
        var_angle_input.set("error")    #后面改成弹窗info
    elif entry_radian_input.get() == "":
        angle_value = float(entry_angle_input.get())
        radian_value = angle2radian(angle_value)
        var_radian_input.set("%.5f"%radian_value)
    else:
        radian_value = float(entry_radian_input.get())
        angle_value = radian2angle(radian_value)
        var_angle_input.set("%.5f"%angle_value)
    return radian_value,angle_value

'''
无输入点击有bug，输入角度时有bug
'''
def compute_sin():
    var,_ = convert()
    result = sin(var)
    var_sin_result.set("%.8f"%result)

def compute_cos():
    var,_ = convert()
    result = cos(var)
    var_cos_result.set("%.8f"%result)

def compute_tan():
    var,var1 = convert()
    if (var1 % 90) == 0:
        var_tan_result.set("error")
    else:
        result = tan(var)
        var_tan_result.set("%.8f"%result)

def compute_cot():
    var,_ = convert()
    if (var%90) == 0:
        var_cot_result.set("error")
    else:
        result = cot(var)
        var_cot_result.set("%.8f"%result)

def clear_all():
    var_sin_result.set("")
    var_cos_result.set("")
    var_tan_result.set("")
    var_cot_result.set("")
    var_angle_input.set("")
    var_radian_input.set("")


#compute button
btn_sin = tk.Button(window, text='sin',
                    width=12, height=2,command=compute_sin).place(x=30, y=90)
btn_cos = tk.Button(window, text='cos',
                    width=12, height=2,command=compute_cos).place(x=30, y=150)
btn_tan = tk.Button(window, text='tan',
                    width=12, height=2,command=compute_tan).place(x=30, y=210)
btn_cot = tk.Button(window, text='cot',
                    width=12, height=2,command=compute_cot).place(x=30, y=270)
btn_clear = tk.Button(window, text='清除',
                    width=12, height=1,command=clear_all).place(x=50, y=330)
btn_quit = tk.Button(window, text='退出',
                    width=12, height=1,command=window.quit).place(x=160, y=330)

#result output
var_sin_result = tk.StringVar()
l_sin = tk.Label(window,width=17, height=2,
                 textvariable=var_sin_result,
                 font=(12), #删除了字体
                 bg="gray")
l_sin.place(x=150, y=90)

var_cos_result = tk.StringVar()
l_cos = tk.Label(window,width=17, height=2,
                 textvariable=var_cos_result,
                 font=(12),bg="gray")
l_cos.place(x=150, y=150)

var_tan_result = tk.StringVar()
l_tan = tk.Label(window,width=17, height=2,
                 textvariable=var_tan_result,
                 font=(12),bg="gray")
l_tan.place(x=150, y=210)

var_cot_result = tk.StringVar()
l_cot = tk.Label(window,width=17, height=2,
                 textvariable=var_cot_result,
                 font=(12),bg="gray")
l_cot.place(x=150, y=270)


window.mainloop()
