# se2020
homework for software engineering

三角函数软件工程项目
=
编写软件：python、matlab
--
### 界面
* (1)点击界面的options按钮可下拉隐藏的工具，包含Python Language、M Language和Exit选项，可选择后台执行三角函数计算采用的编辑语言或系统退出操作。
* (2)界面有两个输入框，分别为弧度和角度，对应于三角函数输入变量的角度制和弧度制两种形式，可对其中一个输入框输入，则另一个输入框变为输出框，计算对应弧度角度转换的值。
   ![](https://gitub.com/PufeiLi/se2020/raw/master/界面.png)
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

         
