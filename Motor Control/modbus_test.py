# -*- coding: utf_8 -*-


import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


def mod(PORT="com6"):
    red = []
    alarm = ""
    try:
        # 设定串口为从站
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
                                                    baudrate=19200, bytesize=8, parity='N', stopbits=1))
        master.set_timeout(5.0)
        master.set_verbose(True)

        # 读保持寄存器
        # while True:
        #     print("What to do?\n0：Modbus使能，1：驱动器输出使能，2：电机目标速度，3：电机加速度")
        red = master.execute(1, cst.READ_HOLDING_REGISTERS, 3, 1)  # 这里可以修改需要读取的功能码
        print(red)
        master.execute(1,cst.WRITE_SINGLE_REGISTER,0,output_value=1)
        master.execute(1,cst.WRITE_SINGLE_REGISTER,3,output_value = 5000)
        red = master.execute(1, cst.READ_HOLDING_REGISTERS, 3, 1)  # 这里可以修改需要读取的功能码
        print(red)
        alarm = "正常"
        return list(red), alarm

    except Exception as exc:
        print(str(exc))
        alarm = (str(exc))

    return red, alarm  ##如果异常就返回[],故障信息


if __name__ == "__main__":
    mod()