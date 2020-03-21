# se2020
homework for software engineering

三角函数软件工程项目
=
编写软件：python
--
### 界面
* (1)界面有一个棕色输入框和一个灰色输出框，分别用于三角函数变量的输入和值的输出。
* (2)界面有四个按钮，分别为sin，cos，tan，cot，点击四个按钮可以分别计算对应三角函数的值。

![](https://github.com/PufeiLi/se2020/raw/master/界面图片.jpg)
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
* 三角函数计算<br>
sin计算```
        g = 0
        t = x
        n = 1
        while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
        return g
        ```
  cos计算```
         x = 1.57079 - x
         return sin(x)
         ```
   ；tan计算```
          return sin(x)/cos(x)
          ```
    ；cot计算```
           return cos(x)/sin(x)
           ```

         
