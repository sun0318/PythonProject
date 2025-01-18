# ################### socket客户端 ###################
import os
import socket
import struct
import select

client = socket.socket()

try :
    client.connect(('127.0.0.1', 8001))
except Exception:
    pass
def send_data(conn, content):
    data = content.encode("utf-8")
    header = struct.pack("i", len(data))
    conn.sendall(header)
    conn.sendall(data)


def send_file(conn, file_name):
    file_size = os.stat(file_name).st_size
    header = struct.pack("i", file_size)
    conn.sendall(header)
    file_object = open(file_name, mode="rb")
    has_read_size = 0
    while has_read_size < file_size:
        chunk = file_object.read(2048)
        conn.sendall(chunk)
        has_read_size += len(chunk)
    file_object.close()

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
        size = chunk_size if (data_length - has_recv_data) > chunk_size else data_length - has_recv_data
        chunk = conn.recv(size)
        data_list.append(chunk)
        has_recv_data += len(chunk)
    data = b"".join(data_list)
    return data

def register():
    pass

def run():
    client_list = []
    recv_list = []
    is_succ = False
    while True:
        if not is_succ:
            name = input("欢迎登录系统，请输入用户名：")
            pwd = input("请输入密码：")
            client_list.append(client)
        # w = [第一个socket对象,]
        # r = [socket对象,]
        # r, w, e = select.select(recv_list, client_list, [], 0.1)
        # for sock in w:
        msg = "login|{}|{}".format(name, pwd)
        send_data(client, msg)
            # recv_list.append(sock)
            # client_list.remove(sock)

        # r, w, e = select.select(recv_list, client_list, [], 0.1)
        # for sock in r:
        #     # 数据发送成功后，判断数据
        result = recv_data(client).decode("utf-8")
        # recv_list.remove(sock)
        if "000" == result:
            is_succ = True
            print("登录成功")
            break
        else:
            print("账号或密码错误，请重新输入")
            continue
        if is_succ:
            break
    client_list.append(client)
    # recv_list = []
    while True:
        # r, w, e = select.select(recv_list, client_list, [], 0.1)
        # for sock in w:
        content = input("请输入你需要的操作：")
        send_data(client, content)
            # recv_list.append(sock)
            # client_list.remove(sock)

        # for sock in r:
            # 数据发送成功后，判断数据
        recv_data(client)
        # if not recv_list and not client_list:
        #     break
        if content.upper() == 'Q':
            break
        if content.upper() == 'LS':
            continue
        if len(content.split("|")) == 2:
            instruction = content.split("|")[0]
            if "up" == instruction:
                send_data(client,content)
                send_file(client,content.split("|")[1])
            elif "down" == instruction:
                pass
            elif "msg" == instruction:
                send_file(client,content.split("|")[1])

        else:
            send_data(client,content)


if __name__ == "__main__":
    run()
