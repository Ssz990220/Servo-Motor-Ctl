# Motor Control
## 硬件信息：
* 电机型号：[YZ-60W40P10C](https://detail.tmall.com/item.htm?id=564338158204&spm=a1z09.2.0.0.25fc2e8dP2Q6cc&_u=c1n98e50407a)
    * 工作电压：48V
    * 最大转速：3000 rpm
    * 编码器线数：2500（10000线/圈）
* 控制器型号：[YZ-ACSD608](https://detail.tmall.com/item.htm?id=564338158204&spm=a1z09.2.0.0.25fc2e8dP2Q6cc&_u=c1n98e50407a)
    * 工作电压：DC24v~48v
* 行星齿轮型号：[YT-200-18](https://detail.tmall.com/item.htm?id=610150059104&spm=a1z09.2.0.0.25fc2e8dP2Q6cc&_u=c1n98e5071ee)
    * 减速比：1/18
* 具体参数及技术细节参考[手册](https://github.com/Ssz990220/Servo-Motor-Ctl/blob/master/Manual/YZ-ACSD608%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_v6.8.pdf)
## 安装方法：
* 安装[CH341-w7.exe](https://github.com/Ssz990220/Servo-Motor-Ctl/blob/master/Driver/CH341-W7.exe)（串口驱动）
* 安装[yz_acsd608_5_2.exe](https://github.com/Ssz990220/Servo-Motor-Ctl/blob/master/Driver/yz_acsd608_5_2.exe)（电机调试）
* 使用设备管理器查看端口号（windows：win+x→设备管理器→串口（例如COM6））
* 运行YZ_ACSD608，输入对应端口进行连接
    * 使能modbus，发送1
    * 其他参数操作...
    * 参数保存标志，发送1，以保存数据
## python环境
* python >= 3.5
    * serial
    * pyserial
* 运行`main.py`前
    * 修改端口：`ser = init("COM6")`
    * 修改指令：`move_abs(ser,DEGREE_TO_MOVE_TO)`
    * 确保YZ_ACSD608程序未在运行（或端口未连接）
## 命令解读
* 读取指令结构：
    * 请求命令：以010300030001为例
        * 01表示控制器编号，默认为01
        * 03是控制指令，03是读取，06是写入
        * 0003表示读取0x03位上的数据，参考说明书
        * 0001表示该数据位上有一位数据
    * 返回命令：
