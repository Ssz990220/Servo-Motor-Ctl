def calc_crc(data):
    # crc calculator
    crc = 0xFFFF
    for pos in data:
        crc ^= pos 
        for i in range(8):
            if ((crc & 1) != 0):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

def cmd_crc(cmd):
    # Calculate the CRC checker and reencode the cmd
    #　cmd written in '01030001...'
    cmd_array = bytearray.fromhex(cmd)
    crc_ori = calc_crc(cmd_array)
    crc_str = "%04x"%(crc_ori)
    cmdcrc = cmd+crc_str[2:4]+crc_str[0:2]
    return cmdcrc