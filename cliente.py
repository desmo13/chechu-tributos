import socket


mi_socket = socket.socket()
mi_socket.connect(("localhost",8000))

mi_socket.send("cliente enva datos a servidor ")
respuesta = mi_socket.recv(1024)
print (respuesta)
mi_socket.close()