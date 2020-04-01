import tkinter as tk
from tkinter import messagebox
from func  import *
import ctypes


#加载matlab生成的动态库dll文件
ll = ctypes.cdll.LoadLibrary

# TODO 将 m 脚本整合成一个大函数，只需要加载一个dll
m_sin = ll("./New_sin.dll")
# sin.New_sin.argtype = ctypes.c_double # 设置函数传入参数的类型
m_sin.New_sin.restype = ctypes.c_double   # 设置函数返回参数的类型
m_cos = ll("./New_cos.dll")
m_cos.New_cos.restype = ctypes.c_double
m_tan = ll("./New_tan.dll")
m_tan.New_tan.restype = ctypes.c_double
m_cot = ll("./New_cot.dll")
m_cot.New_cot.restype = ctypes.c_double


#UI界面
window = tk.Tk()
window.title("trigonometric function")
window.geometry("320x400")


flag = 0    #flag为0 使用python脚本 flag为1 使用m脚本

def p_program():
    global flag
    flag = 0
    tk.messagebox.showinfo(title='programming language', message='you have selected python script!')

def m_program():
    global flag
    flag = 1
    tk.messagebox.showinfo(title='programming language', message='you have selected M script!')

#top menu 菜单界面
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)  # tearoff 可以单独出来
menubar.add_cascade(label='Options', menu=filemenu)
filemenu.add_command(label='Python Script', command=p_program)
filemenu.add_command(label='M Script', command=m_program)
filemenu.add_separator()  # 这里就是一条分割线
filemenu.add_command(label='Exit', command=window.quit)
window.config(menu=menubar)

tk.Label(window, text='请输入要计算的数: ').place(x=30, y=40)
tk.Label(window, text='弧度').place(x=165, y=10)
tk.Label(window, text='角度').place(x=245, y=10)


#输入界面
var_radian_input = tk.StringVar()   #弧度界面
entry_radian_input = tk.Entry(window,
                              textvariable=var_radian_input,
                              width=8,bg="tan")
entry_radian_input.place(x=150, y=40)

var_angle_input = tk.StringVar()    #角度界面
entry_angle_input = tk.Entry(window,
                              textvariable=var_angle_input,
                              width=8,bg="tan")
entry_angle_input.place(x=230, y=40)

#弧度和角度之间转换
# TODO 实际上是角度转换成弧度，因为计算时按弧度计算
# TODO 无输入点击有弹窗，输入角度时有bug==解决
# TODO 输入字符弹窗提示==解决
# TODO 输入大量的数字如何计算==解决

def convert():
    if (entry_radian_input.get() == "")&(entry_angle_input.get() == ""):
        tk.messagebox.showwarning(title='FBI Warning', message='PLEASE INPUT A NUMBER！')
        # var_angle_input.set("error")  # TODO 后面改成弹窗info
        radian_value = float(entry_radian_input.get())
        angle_value = float(entry_angle_input.get())
    elif entry_radian_input.get() == "":
        try:
            angle_value = float(entry_angle_input.get())
            radian_value = angle2radian(angle_value)
            var_radian_input.set("%.5f"%radian_value)
        except TypeError:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')
        except ValueError:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')
        except:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')

    elif entry_angle_input.get() == "":
        try:
            radian_value = float(entry_radian_input.get())
            angle_value = radian2angle(radian_value)
            var_angle_input.set("%.5f"%angle_value)
        except TypeError:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')
        except ValueError:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')
        except:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')
    else: #两个输入框都有数据时，以弧度框为准
        try:
            radian_value = float(entry_radian_input.get())
            angle_value = radian2angle(radian_value)
            var_angle_input.set("%.5f"%angle_value)
        except TypeError:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')
        except ValueError:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')
        except:
            tk.messagebox.showerror(title='Error', message='请输入 < 99999999的数')

    return (radian_value % (2*pi)), angle_value


def compute_sin():
    var,_ = convert()
    if flag:
        result = m_sin.New_sin(ctypes.c_double(var))
    else:
        result = sin(var)
    var_sin_result.set("%.8f"%result)

def compute_cos():
    var,_ = convert()
    if flag:
        result = m_cos.New_cos(ctypes.c_double(var))
    else:
        result = cos(var)
    var_cos_result.set("%.8f"%result)

def compute_tan():
    var,var1 = convert()
    if (var1 % 90) == 0:
        var_tan_result.set("error")
    else:
        if flag:
            result = m_tan.New_tan(ctypes.c_double(var))
        else:
            result = tan(var)
        var_tan_result.set("%.8f"%result)

def compute_cot():
    var,_ = convert()
    if (var%90) == 0:
        var_cot_result.set("error")
    else:
        if flag:
            result = m_cot.New_cot(ctypes.c_double(var))
        else:
            result = cot(var)
        var_cot_result.set("%.8f"%result)

#清除所有界面的信息
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
l_sin = tk.Label(window,width=14, height=2,
                 textvariable=var_sin_result,
                 font=(12), #删除了字体
                 bg="gray")
l_sin.place(x=150, y=90)

var_cos_result = tk.StringVar()
l_cos = tk.Label(window,width=14, height=2,
                 textvariable=var_cos_result,
                 font=(12),bg="gray")
l_cos.place(x=150, y=150)

var_tan_result = tk.StringVar()
l_tan = tk.Label(window,width=14, height=2,
                 textvariable=var_tan_result,
                 font=(12),bg="gray")
l_tan.place(x=150, y=210)

var_cot_result = tk.StringVar()
l_cot = tk.Label(window,width=14, height=2,
                 textvariable=var_cot_result,
                 font=(12),bg="gray")
l_cot.place(x=150, y=270)


window.mainloop()


