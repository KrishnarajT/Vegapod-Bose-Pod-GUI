import socket
import smbus
import RPi.GPIO as GPIO
import time
import sensor_code as mpu
import sys

HOST =  '169.254.164.35'           #IP of the base station

while(True):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #print(socket.gethostname())
            s.connect((HOST, 1234))
            print("connected")

            #channel = 6
            #GPIO setup
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(23, GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            x = int(0)
            addr1 = 0x09
            #addr2 = 0x08
            bus = smbus.SMBus(1)

            #bus.write_byte(addr1, 0xFF)
            #bus.write_byte(addr2, 0xFF)

            ##bus.write_byte(addr1, 0)
            #bus.write_byte(addr2, 0)

            #GPIO.output(23, False) #exists in code
            #GPIO.output(24, False)  #exists in code

            
            #Receiving values from User

            direction_raw = s.recv(1024)                       #Received Direction
            direction = int(direction_raw.decode("utf-8"))
            bus.write_byte(addr1, direction)
            #bus.write_byte(addr2, direction)
            #bus.write_byte(addr3, direction)
            #bus.write_byte(addr4, direction)
            print("direction is ", direction)

            endVal_raw = s.recv(1024)                          #REceived end_val 
            end_val = int(endVal_raw.decode("utf-8"))
            bus.write_byte(addr1, end_val)
            #bus.write_byte(addr2, end_val)
            #bus.write_byte(addr3, end_val)
            #bus.write_byte(addr4, end_val)                    #1-100
            print("end val is", end_val)

            stepVal_raw = s.recv(1024)                         #Received step_Val
            step_val = int(stepVal_raw.decode("utf-8"))
            bus.write_byte(addr1, step_val)                   #1-10
            #bus.write_byte(addr3, step_val)
            #bus.write_byte(addr3, step_val)
            #bus.write_byte(addr4, step_val)
            print("step val is", step_val)

            interval_raw = s.recv(1024)                        #Received interval
            interval = int(interval_raw.decode("utf-8")) 
            bus.write_byte(addr1, interval)                   #1-10
            #bus.write_byte(addr3, interval)
            #bus.write_byte(addr3, interval)
            #bus.write_byte(addr4, interval)     
            print("inteval (centiseconds) is", interval)       #divide by 10
            print(" ")
            print("Sending Values to the controller...")
            s.close()                                #Socket close

            print(" ")
            time.sleep(0.1)
            #Calculates total delay
            delay = (end_val / step_val) * (interval / 100) + 0.25
            print("Total Delay is: ", delay)
            print(" ")

            #trying to implement mpu code

            mpu.sensor_vals(delay)
            #time.sleep(delay)

            # Phancy Braking
            #for i in range (0, 3):
            #     print("Actuating Brakes!...", i)
            #     #GPIO.output(23, True)
            #     #GPIO.output(24, True)
            #     time.sleep(1)
            #     #GPIO.output(23, False)
            #     #GPIO.output(24, False)


            # shistit Braking
            #print("Actuating Brakes!..")
            #GPIO.output(23, False)
            #GPIO.output(24, False)

            #time.sleep(1)
            #GPIO.output(23, True)
            #GPIO.output(24, True)

            
            print(" ")
            #print("Braking completed!")
            time.sleep(0.15)
            print(" ")
            print("Run Executed!")
            print("---------------------------------------")
            exit()


    except ConnectionRefusedError as e:
        # print(e)
        continue
    except ConnectionResetError as e2:
        # print(e2)
        continue        















