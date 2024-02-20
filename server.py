import socket


target_host=socket.gethostname()
target_port=50002

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket,address=s.accept()
    print(f"connection from{address} has been established")
    clientsocket.send(bytes("welcome to the server","utf-8"))
    s.close()