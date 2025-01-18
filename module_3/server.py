import struct

import os
import select
import socket
from openpyxl import load_workbook
filepath = os.path.abspath(__file__)
dir = os.path.dirname(filepath)
filename = os.path.join(dir,"files","users.xlsx")
wb = load_workbook(filename)
sheet = wb.worksheets[0]
def recv_data(conn, chunk_size=1024):
    bytes_list = []
    has_recv_size = 0
    # 获取头部长度数据
    while has_recv_size < 4:
        chunk = conn.recv(4 - has_recv_size)
        bytes_list.append(chunk)
        has_recv_size = len(chunk)
    header_data = b"".join(bytes_list)
    data_length = struct.unpack("i", header_data)[0]
    data_list = []
    has_recv_data = 0
    while has_recv_data < data_length:
        size = chunk_size if (data_length - has_recv_size) > chunk_size else data_length - has_recv_size
        chunk = conn.recv(size)
        data_list.append(chunk)
        has_recv_data += len(chunk)
    data = b"".join(data_list)
    return data


def recv_file(conn, file_name, chunk_size=1024):
    sava_file_path = os.path.join("files", file_name)
    has_recv_size = 0
    bytes_list = []
    while has_recv_size < 4:
        header = conn.recv(4-has_recv_size)
        bytes_list.append(header)
        has_recv_size += len(header)
    header_data = "b".join(bytes_list)
    data_length = struct.unpack("i",header_data)[0]
    file_object = open(sava_file_path,mode="wb")
    has_recv_data = 0
    while has_recv_data < data_length:
        size = chunk_size if (data_length - has_recv_size) > chunk_size else data_length-has_recv_size
        data = conn.recv(size)
        file_object.write(data)
        file_object.flush()
        has_recv_size += len(data)
    file_object.close()

def send_data(conn,content):
    data = content.encode("utf-8")
    header = struct.pack("i", len(data))
    conn.sendall(header)
    conn.sendall(data)

def login(name,password):
    a_column = sheet['A'][1:]  # 从第二行开始获取 A 列的数据
    b_column = sheet['B'][1:]  # 从第二行开始获取 B 列的数据
    is_success = "999"

    for a_cell, b_cell in zip(a_column, b_column):
        name2 = str(a_cell.value)
        en_password2 = str(b_cell.value)
        if(name == name2.strip() and password == en_password2.strip()):
            print("登录成功")
            is_success = "000"
            break
        else:
            print("用户名或密码错误")
    return is_success

def register():
    pass


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)  # 加上就变为了非阻塞
    server.bind(('127.0.0.1', 8001))
    server.listen(5)

    inputs = [server, ]  # socket对象列表 -> [server, 第一个客户端连接conn ]
    while True:
        # 当 参数1 序列中的socket对象发生可读时（accetp和read），则获取发生变化的对象并添加到 r列表中。
        # r = []
        # r = [server,]
        # r = [第一个客户端连接conn,]
        # r = [server,]
        # r = [第一个客户端连接conn，第二个客户端连接conn]
        # r = [第二个客户端连接conn,]
        r, w, e = select.select(inputs, [], [], 0.05)
        for sock in r:
            # server
            if sock == server:
                conn, addr = sock.accept()  # 接收新连接。
                print("有新连接")
                # conn.sendall()
                # conn.recv("xx")
                inputs.append(conn)
            else:
                data = recv_data(sock).decode("utf-8")
                print(data)
                if not data:
                    print("关闭连接")
                    inputs.remove(sock)
                if data == "LS":
                    pass
                elif data.find("|") > -1:
                    instrucion = data.split("|")[0]
                    if "up" == instrucion:
                        recv_file(sock,data.split("|")[1])
                    elif "down" == instrucion:
                        pass
                    elif "login" == instrucion:
                        result = login(data.split("|")[1],data.split("|")[2])
                        send_data(sock,result)
                    elif "msg" == instrucion:
                        print("这是客户端发来的消息",data.split("|")[1])

                else:
                    recv_data(sock)
        # 干点其他事 20s
    """
    优点：
        1. 干点那其他的事。
        2. 让服务端支持多个客户端同时来连接。
    """

if __name__ == "__main__":
    run()