import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
s.bind((HOST, 1234))
s.listen(5)
clientsocket, address = s.accept()
print(f"connection from {address} has been established!")

# Sending to PI

clientsocket.send(bytes(start_val, "utf-8"))

clientsocket.send(bytes(end_val, "utf-8"))

clientsocket.send(bytes(step_val, "utf-8"))

clientsocket.send(bytes(delay, "utf-8"))


    