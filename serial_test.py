from utils import *
import serial
import time
import math

def init(port):
    ser = serial.Serial(     
        port=port,        
        baudrate = 19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
    write_data(ser, 0x00,1,"使能modbus")           #使能modbus
    write_data(ser, 0x0a,1,"电子齿轮比分子")        #电子齿轮比分子为1
    write_data(ser,0x0b,0x12,"电子齿轮比分母")      # 电子齿轮比分母为18 0x12
    write_data(ser,0x03,0x03e8,"电机加速度")        # 电机加速度1000 0x3e8
    write_data(ser,0x04,0x05,"电机起始速度")
    write_data(ser, 0x05,0x0fa0,"速度比例环系数kp") # 速度比例环系数kp：2000
    write_data(ser,0x07,0x03e8,"位置比例环系数kp")  #  位置比例环系数kp：1000
    write_data(ser,0x02,0x0014,"位置模式目标转动速度")   #  位置模式目标转动速度：10
    write_data(ser,0x14,0x01,"保存设置")
    
    return ser

def read_data(ser, cmd,cmd_type='',disp=1):
    # send a command and read the inquired data
    cmd = "%02d"%(cmd)
    if cmd=="16" or cmd=="17":
        cmd = "010300"+cmd+"0002" 
        send_cmd(ser, cmd)
        rev = ser.read(9)
    else:    
        cmd = "010300"+cmd+"0001" 
        send_cmd(ser, cmd)
        rev = ser.read(8)
    if disp:
        print("Raw data:", rev)
        print(cmd_type,decode_rrev(rev))
    return decode_rrev(rev)
        
def write_data(ser, cmd, data, cmd_type=''):
    # ser is the Serial instance for modbus connection
    # cmd is the command to send, written in hex, e.g. 0x03
    # data is the value to send
    # cmd_type is void as default for now.
    if isinstance(cmd, str):
        pass
    else:
        cmd_hex = "%02x"%(cmd)
    data = "%04x"%(data)
    if cmd== 0x16 or cmd==0x17:
        raise ValueError("Data 0x16 and 0x17 should be sent in pulse mode.")
    if cmd>=0x0C and cmd <= 0x13:
        raise ValueError("Data to be changed is readonly.")
    cmd = '010600' + cmd_hex + data
    send_cmd(ser, cmd)
    rev = ser.read(8)
    print(cmd_type,": ",decode_wrev(rev))
    
def decode_wrev(rev):
    # decode the received message after sending the write cmd
    rev_str = rev.hex()[8:12]
    return int(rev_str,16)

def decode_rrev(rev):
    # decode the received message after sending the read cmd
    rev_str = rev.hex()
    data_len = int(rev_str[4:6])
    data = int(rev_str[6:6+data_len],16)
    return data

def send_cmd(ser, cmd, disp=0):
    # encode and send a command
    cmd = cmd_crc(cmd)
    cmd_b = bytes.fromhex(cmd)
    ser.write(cmd_b)
    if disp:
        print(cmd)

def move(ser,degree):
    r = degree/360
    p = int(r*2500*4*18)
    if p>=0:
        cmd = "%08x"%(p)
    else:
        cmd = "%08x"%(0xffffffff+p+1)
    cmd = "01100016000204"+cmd[4:6]+cmd[6:8]+cmd[0:2]+cmd[2:4]
    send_cmd(ser,cmd)
    rev = ser.read(32)
    
    
if __name__=='__main__':
    # 指令结构：以010300030001为例
    # 01表示控制器编号，默认为01
    # 03是控制指令，03是读取，06是写入
    # 0003表示读取0x03位上的数据，参考说明书
    # 0001表示该数据位上有一位数据
    # Read income msg to clear cache every time you send a cmd !!!
    ser = init("COM6")
    move(ser, 150)
    read_data(ser,16)
    read_data(ser,17)
    send_cmd(ser, "010600000000")    #下使能modbus