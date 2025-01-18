import struct

# ########### 数值转换为固定4个字节，四个字节的范围 -2147483648 <= number <= 2147483647  ###########
v1 = struct.pack('i', 199)
print(v1)  # b'\xc7\x00\x00\x00'

for item in v1:
    print(item, bin(item))

# ########### 4个字节转换为数字 ###########
v2 = struct.unpack('i', v1)[0]  # v1= b'\xc7\x00\x00\x00'
print(v2)  # (199,)

a =["123".encode("utf-8"),"222".encode("utf-8")]
b = b"".join(a)
print(b)
