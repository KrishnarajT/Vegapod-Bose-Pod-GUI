import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
clientsocket, address = s.accept()
print(f"connection from {address} has been established!")

while True:
     
    start_val = input("Start_value = ")
    clientsocket.send(bytes(start_val, "utf-8"))
    #time.sleep(0.5)
    
    end_val = input("End value = ")
    clientsocket.send(bytes(end_val, "utf-8"))
    time.sleep(0.5)
    
    step_val = input("Step value = ")
    clientsocket.send(bytes(step_val, "utf-8"))
    time.sleep(0.5)
    
    delay = input("delay = ")
    clientsocket.send(bytes(delay, "utf-8"))
    time.sleep(3)
    
    