# se2020
homework for software engineering

三角函数软件工程项目
=
编写软件：python
--
### 界面
* (1)界面有一个棕色输入框和一个灰色输出框，分别用于三角函数变量的输入和值的输出。
* (2)界面有四个按钮，分别为sin，cos，tan，cot，点击四个按钮可以分别计算对应三角函数的值。

![](https://github.com/PufeiLi/se2020/raw/master/界面.jpg)
### 后台
* 界面尺寸、标题```
             window = tk.Tk()
             window.title("trigonometric function")
             window.geometry("300x200")
             ```
* 输入变量 ```
             e.get()   
             ```
三角函数值输出```
         t.insert("end", result)
         ```<br>

* 界面按钮，例如```
         tk.Button(window,
                  text="sin",
                  # width=15,height=2,
                  width=15, height=1,
                  command=compute_sin, )
                  ```
         
