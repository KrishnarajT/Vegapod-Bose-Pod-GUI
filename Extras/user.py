import socket
import time
#import reverse_connect_user as a


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
clientsocket, address = s.accept()
print(f"connection from {address} has been established!")

while True:
     
    clientsocket.send(bytes(Direction, "utf-8"))
    time.sleep(0.5)
    clientsocket.send(bytes(end_val, "utf-8"))
    time.sleep(0.5)
    clientsocket.send(bytes(step_val, "utf-8"))
    time.sleep(0.5)
    Direction = input("Enter Direction :  ")
    clientsocket.send(bytes(interval, "utf-8"))
    time.sleep(0.5)
    
    end_val = input("End value = ")
    
    step_val = input("Step value = ")
    
    interval = input("interval:   ")


    
    #Connecting as client
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.connect(('169.254.201.77', 1234))
    print(f"connection from {address} has been established AGAIN as client !!!")

    # Take values for approx 20/25 seconds
    x = time.time()
    samay = 0
    while (samay < 7):
        b = time.time()
        samay = b - x
        print("inside recv loop")

        mpu_accel_raw = a.recv(1024)
        mpu_accel = mpu_accel_raw.decode("utf-8")


    
    print("Session finished...")
    exit()




    
    
    