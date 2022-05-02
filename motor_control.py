#DUTY LINEAR - PI

import smbus
import time
# import RPi.GPIO as GPIO 

def input_and_control(start_val = 1, end_val = 20, step_val = 5, interval = 500):
    """
    Inputs: Takes 4 integers, start val can be either 1 or 2
    That denotes either forward or reverse. 
        Default = 1 (Forward)

    end_val = Last value of motor power thing
        Default = 20
    
    step_val = step value of motor power thing
        Default = 5
    
    interval = time between control commands in microseconds. 
        Default = 500
    """
    
    print('motor code was invoked. ')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    s.bind((HOST, 1234))
    s.listen(5)
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")

    # Sending to PI
    print('sending values to pi')

    clientsocket.send(bytes(start_val, "utf-8"))

    clientsocket.send(bytes(end_val, "utf-8"))

    clientsocket.send(bytes(step_val, "utf-8"))

    clientsocket.send(bytes(delay, "utf-8"))
