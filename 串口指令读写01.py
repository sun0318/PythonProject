 # 导入模块
import serial
  
 # 需要发送的串口指令
cmd ='02 03 00 63 00 03 F5 E6' 

  
# 将字符串转换成字节
cmd=bytes.fromhex(cmd)
print(cmd)
# 生成串口
serial_com = serial.Serial("com1", 19200, timeout=0.03)

 # 发送串口指令
serial_com.write(cmd)

 # 读取串口返回结果
s=serial_com.read(24).hex()
print(s)
# 关闭串口
serial_com.close()
