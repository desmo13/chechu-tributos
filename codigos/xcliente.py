import socket


mi_socket = socket.socket()
mi_socket.connect(('localhost',8000))
#mensaje = 
#mb = mensaje.enconde()
mi_socket.send(b"hola soy el cliente")
respuesta = mi_socket.recv(1024)
print (respuesta)
mi_socket.close()