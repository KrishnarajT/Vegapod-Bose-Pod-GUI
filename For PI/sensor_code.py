import smbus
#from mpu6050 import mpu6050
#import mpu_library_varad as mpu
import time
import json
import socket
#import smbus
import RPi.GPIO as GPIO
#mpu = mpu6050(0x68)
global y 
bus = smbus.SMBus(1)
addr2 = 0x09
pressure_example = 100.00
rpm_example = 5000
mpu_example_accel = [5,10,15]
mpu_example_gyro = [40, 50, 70]
 
y = 0
def sensor_vals(duration):
        print("inside sesnor vals")
        #while (1):
        
        #connecting as server
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.bind(('', 1234))
        a.listen(2)
        clientsocket, address = a.accept()
        print(f"connection from {address} has been established as Server!!")

        x = time.time()
        y = 0
        def collect_values(duration):
            y = 0
            while (y < duration):
                b = time.time()
                y = b - x
                
                ### GATHER DATA HERE ####
                
                #mpu_data = mpu.processed_data()    #calling function to get mpu_data
                #tcp send mpu_data
                mpu1 = mpu_example_accel
                mpu2 = mpu_example_gyro
                pressure = pressure_example
                rpm = 5000
                
                ### CREATE DICTIONARY ###
                
                # Creating a dictionary with the relevant values. 
                data = {
                        'Acceleration': mpu1,
                        'Gyroscope': mpu2,
                        'Pressure': pressure,
                        'RPM': rpm
                }
                data = json.dumps(data) # this is a string in json format
                
                ### SEND DATA ###
                
                clientsocket.send(bytes(data,"utf-8"))
                time.sleep(0.01)

        collect_values(duration)
        exit()
        
#exit()

#sensor_vals(10)

        #collect_values(duration)

        #Braking

        #print("Actuating Brakes!...")
        #GPIO.output(23, False)
        #GPIO.output(24, False)
        #collect_values(1)
        #time.sleep(1)
        #GPIO.output(23, True)
        #GPIO.output(24, True)
        #print("Braking completed!")

        #collect_values(7)
        #exit()
 




        #for i in range(0, 3):
        #    print("Actuating brakes!", i)
        #    #GPIO.output(23, True)
        #    #GPIO.output(24, True)
        #    collect_values(1)
        #    #GPIO.output(23, False)
        #    #GPIO.output(24, False)

















         
