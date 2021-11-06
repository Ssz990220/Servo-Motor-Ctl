# Motor Control
## 硬件信息：
* 电机型号：[YZ-60W40P10C](https://detail.tmall.com/item.htm?id=564338158204&spm=a1z09.2.0.0.25fc2e8dP2Q6cc&_u=c1n98e50407a)
    * 工作电压：48V
    * 最大转速：300rpm
    * 编码器线数：2500（10000线/圈）
* 控制器型号：[YZ-ACSD608](https://detail.tmall.com/item.htm?id=564338158204&spm=a1z09.2.0.0.25fc2e8dP2Q6cc&_u=c1n98e50407a)
    * 工作电压：DC24v~48v
* 行星齿轮型号：[YT-200-18](https://detail.tmall.com/item.htm?id=610150059104&spm=a1z09.2.0.0.25fc2e8dP2Q6cc&_u=c1n98e5071ee)
    * 减速比：1/18
* 具体参数及技术细节参考手册：
## 安装方法：
* 安装CH341-w7.exe（串口驱动）
* 安装yz_acsd608_5_2.exe（电机调试）
* 使用设备管理器查看端口号（windows：win+x→设备管理器→串口（例如COM6））
* 运行YZ_ACSD608，输入对应端口进行连接
    * 使能modbus，发送1
    * 其他参数操作...
    * 参数保存标志，发送1，以保存数据
## python环境
* python 3.8.5
    * serial
    * pyserial
* 运行`main.py`前
    * 修改端口：`ser = init("COM6")`