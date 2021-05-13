import socket
mi_socket = socket.socket()
mi_socket.bind(("localhost",8000))
mi_socket.listen(5)

while True:
    conecxion, direccion = mi_socket.accept()
    print("nueva conecxion establecida")
    print(direccion)

    conecxion.send("Servidor establece datos")
    conecxion.close()