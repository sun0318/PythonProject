import socket
import threading
server_socket = socket.socket()
server_socket.bind(("localhost", 8888))
server_socket.listen(1)
conn,ip = server_socket.accept()
def recv_msg():
    while True:
        recv_msg = conn.recv(1024).decode("utf-8")
        if recv_msg == "exit":
            break
        print(recv_msg)

def send_msg():
    while True:
        send_msg = input().encode("utf-8")
        conn.send(send_msg)

recv_thread = threading.Thread(target=recv_msg)
send_thread = threading.Thread(target=send_msg)
recv_thread.start()
send_thread.start()