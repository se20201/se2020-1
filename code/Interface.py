from tkinter import *
import tkinter.messagebox
import matlab
import matlab.engine
import string
import math
import func
root = Tk()
eng = matlab.engine.start_matlab()
v1 = IntVar()
v1.set(1)
flag = 1
# eng.se_sin(90)

# 窗口大小  （宽x高）
# root.geometry("250x225")
root.geometry("250x250")

# 设置title
root.title("三角函数计算")

# Frame就是在屏幕上的一块矩形区域  多用来作为容器使用
# frame_show = Frame(width=250, height=150, bg='#ddd')
frame_show = Frame(width=280, height=250, bg='#ddd')
# 添加到主窗体
frame_show.pack()

# 主窗体

# 实例化一个产生变量的类
v = StringVar()
# 初始化赋值'0'
v.set('0')
# Lable(用于存放父组件，属性参数   )
# anchor  文本相对于标签中心的位置   默认是center N S W E
show_label = Label(frame_show, textvariable=v, bg='white', width='30', height='1', anchor='e', font=("黑体", 20, "bold"))

# 添加到主窗体
show_label.pack(padx=10, pady=10)

# frame_bord = Frame(width=250, height=350)
frame_bord = Frame(width=280, height=350)
frame_bord.pack(padx=10, pady=10)

calc = []
isoperate = False

#
def change(num):
    global isoperate
    if isoperate == False:
        if v.get() == "0" and num == '.':
            v.set(length(v.get() + num))
        elif v.get() == "0":
            v.set(length(num))
        else:
            if num == ".":
                if v.get().count(".") < 1:
                    v.set(v.get() + num)
            else:
                v.set(v.get() + num)
    else:
        v.set(length(num))
        isoperate = False
#
#
# # 检验字符串的长度的函数
def length(str):
    if len(str) > 12:
        return str[0:12]
    else:
        return str

#
# # 清空函数
def clear():
    global calc
    calc = []
    # 屏幕窗口恢复到0
    v.set("0")


#
# # 操作 +  -  *  /
# def operate(sign):
#     global calc
#     global isoperate
#     isoperate = True
#     calc.append(v.get())
#     if sign == "+":
#         calc.append(sign)
#     elif sign == "-":
#         calc.append(sign)
#     elif sign == "*":
#         calc.append(sign)
#     elif sign == "/":
#         calc.append(sign)
#
#
# # 运算
# global calcstr
#
#
# def equal():
#     global calc
#     # 获取当前界面的值
#     calc.append(v.get())
#     print(calc)
#     # 列表变字符串 join 把列表用什么拼接成字符串
#     calcstr = "".join(calc)
#     print(calcstr)
#     print(type(calcstr))
#
#     # 运算操作 eval（）把str当成有效的表达式进行计算
#     result = eval(calcstr)
#     if len(str(result)) > 12:
#         result = str(result)
#         result = result[0:12]
#         v.set(result)
#     else:
#         v.set(result)
#
#     print(result)
#
#
# 定义退格函数
def delete():
    # 获取v.get（）长度
    num = len(v.get())
    # 如果长度>1 怎么办
    if num > 1:
        strnum = v.get()
        strnum = strnum[0:num - 1]
        v.set(strnum)
    # 小于等于1的时候
    else:
        v.set("0")

def sel():
    print(v1.get())
    # flag =

def sign(display):
    angle = float(v.get())
    flag = v1.get()
    print(flag)
    rad = 3.14 * (angle / 180)  # 化角度为弧度
    if(flag == 1):
        result = eng.New_sin(rad)
        # return result
    else:
        result = func.sin(rad)
    result = round(result, 3)
        # print(result)
        # v.set(result)
    if(display==1):
        v.set(result)
    return result

def cos(display):
    angle = float(v.get())
    flag = v1.get()
    print(flag)
    rad = 3.14 * (angle / 180)  # 化角度为弧度
    if (flag == 1):
        result = eng.New_cos(rad)
        # return result
    else:
        result = func.cos(rad)
    result = round(result, 3)
        # print(result)
        # v.set(result)
    if (display == 1):
        v.set(result)
    return result

def tan():
    sin_res = sign(0)
    cos_res = cos(0)
    result = sin_res / cos_res
    result = round(result, 3)
    # print(result)
    v.set(result)

def cot():
    sin_res = sign(0)
    cos_res = cos(0)
    result = cos_res / sin_res
    result = round(result, 3)
    # print(result)
    v.set(result)

def matlab_test_cot(): #调用九组func.py进行测试
    error_max = 0
    deg = 0
    for i in range(1, 999):  # 测试1000组数据 #专门为tan
        deg =  + i * 0.18  # 0.18步长测试1000组角度 从-90到90 为tan的定义域
        # deg =  i * 0.36  # 0.36步长测试1000组角度
        rad = func.angle2radian(deg)  # 角度转弧度
        # error = math.fabs(func.sin(rad)-math.sin(rad)) #调用九组sin 与系统math.sin做误差分析
        # error = math.fabs(func.tan(rad)-math.tan(rad)) #调用九组sin 与系统math.sin做误差分析

        error = math.fabs(eng.New_cot(rad) - 1/math.tan(rad))  # 调用九组sin 与系统math.sin做误差分析
        error_max = error if (error > error_max) else error_max  # 得出最大误差
        # print("error_max:", error_max, "deg:", deg)
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        tkinter.messagebox.showwarning(title='出错了！', message='cot功能测试完成,误差大于0.001!')
        content.set("cot功能测试完成,误差:" + str(error_max))
    else:
        tkinter.messagebox.showinfo(title='信息提示！', message='cot功能测试完成,误差不大于0.001!')
        content.set("cot功能测试完成,误差:" + str(error_max))
    # return error_max
def matlab_test_tan(): #调用九组func.py进行测试
    error_max = 0
    deg = 0

    for i in range(1, 999):  # 测试1000组数据 #专门为tan
        deg = -90 + i * 0.18  # 0.18步长测试1000组角度 从-90到90 为tan的定义域
        rad = func.angle2radian(deg) #角度转弧度
        error = math.fabs(eng.New_tan(rad)-math.tan(rad)) #调用九组sin 与系统math.sin做误差分析
        error_max = error if(error>error_max)else error_max #得出最大误差
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("matlab_tan功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showwarning(title='出错了！', message='tan功能测试完成,误差大于0.001!')
    else:
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("matlab_tan功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showinfo(title='信息提示！', message='tan功能测试完成,误差不大于0.001!')
    # return error_max
def matlab_test_cos(): #调用九组func.py进行测试
    error_max = 0
    deg = 0

    for i in range(0,1000): #测试1000组数据
        deg =  i * 0.36  # 0.36步长测试1000组角度
        rad = func.angle2radian(deg) #角度转弧度
        error = math.fabs(eng.New_cos(rad)-math.cos(rad)) #调用九组sin 与系统math.sin做误差分析
        error_max = error if(error>error_max)else error_max #得出最大误差
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("matlab_cos功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showwarning(title='出错了！', message='cos功能测试完成,误差大于0.001!')
    else:
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("matlab_cos功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showinfo(title='信息提示！', message='cos功能测试完成,误差不大于0.001!')
    # return error_max

def matlab_test_sin(): #调用九组func.py进行测试
    error_max = 0
    deg = 0

    for i in range(0,1000): #测试1000组数据
        deg =  i * 0.36  # 0.36步长测试1000组角度
        rad = func.angle2radian(deg) #角度转弧度
        error = math.fabs(eng.New_sin(rad)-math.sin(rad)) #调用九组sin 与系统math.sin做误差分析
        error_max = error if(error>error_max)else error_max #得出最大误差
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("matlab_sin功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showwarning(title='出错了！', message='sin功能测试完成,误差大于0.001!')
    else:
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("matlab_sin功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showinfo(title='信息提示！', message='sin功能测试完成,误差不大于0.001!')
    # return error_max

def test_sin(): #调用九组func.py进行测试
    error_max = 0
    deg = 0

    for i in range(0,1000): #测试1000组数据
        deg =  i * 0.36  # 0.36步长测试1000组角度
        rad = func.angle2radian(deg) #角度转弧度
        error = math.fabs(func.sin(rad)-math.sin(rad)) #调用九组sin 与系统math.sin做误差分析
        error_max = error if(error>error_max)else error_max #得出最大误差
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("sin功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showwarning(title='出错了！', message='sin功能测试完成,误差大于0.001!')
    else:
        # v.set('sin功能测试完成,误差大于0.001!')
        content.set("sin功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showinfo(title='信息提示！', message='sin功能测试完成,误差不大于0.001!')
    # return error_max

def test_cos(): #调用九组func.py进行测试
    error_max = 0
    deg = 0
    for i in range(0,1000): #测试1000组数据
        deg =  i * 0.36  # 0.36步长测试1000组角度
        rad = func.angle2radian(deg) #角度转弧度
        error = math.fabs(func.cos(rad)-math.cos(rad)) #调用九组sin 与系统math.sin做误差分析
        error_max = error if(error>error_max)else error_max #得出最大误差
        # print("error_max:",error_max,"deg:",deg)
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        tkinter.messagebox.showwarning(title='出错了！', message='cos功能测试完成,误差大于0.001!')
        content.set("cos功能测试完成,误差:" + str(error_max))
    else:
        content.set("cos功能测试完成,误差:" + str(error_max))
        tkinter.messagebox.showinfo(title='信息提示！', message='cos功能测试完成,误差不大于0.001!')
    # return error_max

def test_tan(): #调用九组func.py进行测试
    error_max = 0
    deg = 0
    for i in range(1, 999):  # 测试1000组数据 #专门为tan
        deg = -90 + i * 0.18  # 0.18步长测试1000组角度 从-90到90 为tan的定义域
        # deg =  i * 0.36  # 0.36步长测试1000组角度
        rad = func.angle2radian(deg)  # 角度转弧度
        # error = math.fabs(func.sin(rad)-math.sin(rad)) #调用九组sin 与系统math.sin做误差分析
        # error = math.fabs(func.tan(rad)-math.tan(rad)) #调用九组sin 与系统math.sin做误差分析

        error = math.fabs(func.tan(rad) - math.tan(rad))  # 调用九组sin 与系统math.sin做误差分析
        error_max = error if (error > error_max) else error_max  # 得出最大误差
        # print("error_max:", error_max, "deg:", deg)
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        tkinter.messagebox.showwarning(title='出错了！', message='tan功能测试完成,误差大于0.001!')
        content.set("tan功能测试完成,误差:" + str(error_max))
    else:
        tkinter.messagebox.showinfo(title='信息提示！', message='tan功能测试完成,误差不大于0.001!')
        content.set("tan功能测试完成,误差:" + str(error_max))
    # return error_max

def test_cot(): #调用九组func.py进行测试
    error_max = 0
    deg = 0
    for i in range(1, 999):  # 测试1000组数据 #专门为tan
        deg =  + i * 0.18  # 0.18步长测试1000组角度 从-90到90 为tan的定义域
        # deg =  i * 0.36  # 0.36步长测试1000组角度
        rad = func.angle2radian(deg)  # 角度转弧度
        # error = math.fabs(func.sin(rad)-math.sin(rad)) #调用九组sin 与系统math.sin做误差分析
        # error = math.fabs(func.tan(rad)-math.tan(rad)) #调用九组sin 与系统math.sin做误差分析

        error = math.fabs(func.cot(rad) - 1/math.tan(rad))  # 调用九组sin 与系统math.sin做误差分析
        error_max = error if (error > error_max) else error_max  # 得出最大误差
        # print("error_max:", error_max, "deg:", deg)
    error_max = '{:.5g}'.format(error_max)
    error_max = float(error_max)
    if (error_max > 1e-3):
        # print("error_max:", error_max, "deg:", deg)
        tkinter.messagebox.showwarning(title='出错了！', message='cot功能测试完成,误差大于0.001!')
        content.set("cot功能测试完成,误差:" + str(error_max))
    else:
        tkinter.messagebox.showinfo(title='信息提示！', message='cot功能测试完成,误差不大于0.001!')
        content.set("cot功能测试完成,误差:" + str(error_max))
    # return error_max
def test(): #调用九组func.py进行测试
    error_max = 0
    deg = 0
    print("test begin!")
    test_sin()
    test_cos()
    test_tan()
    test_cot()
    # matlab_test_sin()
    # matlab_test_cos()
    # matlab_test_tan()
    matlab_test_cot()
    print("test end!")
    # for i in range(0,1000): #测试1000组数据
    # for i in range(1,999): #测试1000组数据 #专门为tan
    #     deg =  -90+i*0.18 #0.18步长测试1000组角度 从-90到90 为tan的定义域
    #     # deg =  i * 0.36  # 0.36步长测试1000组角度
    #     rad = func.angle2radian(deg) #角度转弧度
    #     # error = math.fabs(func.sin(rad)-math.sin(rad)) #调用九组sin 与系统math.sin做误差分析
    #     # error = math.fabs(func.tan(rad)-math.tan(rad)) #调用九组sin 与系统math.sin做误差分析
    #
    #     error = math.fabs(func.tan(rad) - math.tan(rad))  # 调用九组sin 与系统math.sin做误差分析
    #     error_max = error if(error>error_max)else error_max #得出最大误差
    #     print("error_max:",error_max,"deg:",deg)
    #
    # if (error_max > 1e-3):
    #     print("error_max:", error_max, "deg:", deg)
    #     tkinter.messagebox.showwarning(title='出错了！', message='in功能测试完成,误差大于0.001!')
    #
    # else:
    #     tkinter.messagebox.showinfo(title='信息提示！', message='sin功能测试完成,误差不大于0.001!')
    # return error_max

# Button(父组件，属性参数)
button_del = Button(frame_bord, text='←', width='5', height='1', command=lambda: delete()).grid(row='1', column='0')
button_del = Button(frame_bord, text='CE', width='5', height='1', command=lambda: clear()).grid(row='1', column='1')
button_del = Button(frame_bord, text='0', width='5', height='1', command=lambda: change("0")).grid(row='1', column='2')
button_del = Button(frame_bord, text='Sin', width='5', height='1', command=lambda: sign(1)).grid(row='1', column='3')

button_del = Button(frame_bord, text='7', width='5', height='1', command=lambda: change("7")).grid(row='2', column='0')
button_del = Button(frame_bord, text='8', width='5', height='1', command=lambda: change("8")).grid(row='2', column='1')
button_del = Button(frame_bord, text='9', width='5', height='1', command=lambda: change("9")).grid(row='2', column='2')
button_del = Button(frame_bord, text='Cos', width='5', height='1', command=lambda: cos(1)).grid(row='2', column='3')

button_del = Button(frame_bord, text='4', width='5', height='1', command=lambda: change("4")).grid(row='3', column='0')
button_del = Button(frame_bord, text='5', width='5', height='1', command=lambda: change("5")).grid(row='3', column='1')
button_del = Button(frame_bord, text='6', width='5', height='1', command=lambda: change("6")).grid(row='3', column='2')
button_del = Button(frame_bord, text='Tan', width='5', height='1', command=lambda: tan()).grid(row='3', column='3')

button_del = Button(frame_bord, text='1', width='5', height='1', command=lambda: change("1")).grid(row='4', column='0')
button_del = Button(frame_bord, text='2', width='5', height='1', command=lambda: change("2")).grid(row='4', column='1')
button_del = Button(frame_bord, text='3', width='5', height='1', command=lambda: change("3")).grid(row='4', column='2')
button_del = Button(frame_bord, text='Cot', width='5', height='1', command=lambda: cot()).grid(row='4', column='3')
button_del = Button(frame_bord, text='Test', width='5', height='1', command=lambda: test()).grid(row='5', column='3')
content=StringVar()
content.set('可以选中')
# e1 = Entry(root,  textvariable=content,state='readonly',width=34).place(x=10,y=220)

r1 = Radiobutton(frame_bord, text="matlab", value=1, variable=v1,command=sel)
r1.grid(row=5, column=1)

r2 = Radiobutton(frame_bord, text="python", value=2, variable=v1,command=sel)
r2.grid(row=5, column=2)






root.mainloop()
