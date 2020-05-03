# se2020
homework for software engineering

三角函数测试工作
=
编写软件：python、matlab
--
* 点击界面右下角的Test按钮，开始自测，对每个三角函数模块进行1000次求值测试，并将测试的结果逐条地显示在界面下方。要求和系统三角函数的误差小于阈值，若误差大于阈值，则额外弹出错误消息提示框。

![](https://github.com/PufeiLi/se2020/raw/master/界面.png)

### 后台
* 测试函数，以python编写的sin模块为例```

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
        content1.set("sin功能测试完成,误差:"+str(error_max))
        tkinter.messagebox.showwarning(title='出错了！', message='sin功能测试完成,误差大于0.001!')
    else:
        # v.set('sin功能测试完成,误差大于0.001!')
        content1.set("sin功能测试完成,误差:"+str(error_max))
    ```

         
