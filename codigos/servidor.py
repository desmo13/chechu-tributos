import socket


mi_socket = socket.socket()
mi_socket.bind(('localhost',8000))
mi_socket.listen(5)

while True:
    conection, addr = mi_socket.accept()
    print("nueva conecxion")
    print(addr)
    mens = "hola desde el servidor"
    conection.send(mens.encode())
    conection.close()