import socket
import time
#import smbus
#import RPi.GPIO as GPIO

HOST = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(socket.gethostname())
s.connect((HOST, 1234))

#channel = 6
#GPIO setup
#GPIO.setmode(GPIO>BCM)
#GPIO.setup(23, GPIO.OUT)
#GPIO.setup(24,GPIO.OUT)

x = int(0)

#addr1 = 0x07
#addr2 = 0x08
#bus = smbus.SMBus(1)

#bus.write_byte(addr1, 0xFF)
#bus.write_byte(addr2, 0xFF)

##bus.write_byte(addr1, 0)
#bus.write_byte(addr2, 0)

#GPIO.output(23, False) #exists in code
#GPIO.output(24, False)  #exists in code

direction_raw = s.recv(1024)
direction = int(direction_raw.decode("utf-8"))
print("direction is ", direction)

# Receiving values from the main computer. 

endVal_raw = s.recv(1024)                      #1-100
end_val = int(endVal_raw.decode("utf-8"))
print("end val is", end_val)

stepVal_raw = s.recv(1024)
step_val = int(stepVal_raw.decode("utf-8"))          #1-10
print("step val is", step_val)

interval_raw = s.recv(1024)
interval = int(interval_raw.decode("utf-8"))
print("inteval is", interval)

# Giving command to the motor. 
for i in range(0, int((end_val / step_val))):

    x = (x + step_val)
    time.sleep(interval / 1000)
    
    if direction == 1:
    
        ##value = bus.write_byte(addr1, x)
        #value = bus.write_byte(addr2, x)
        print(x)
        
    elif direction == 2:

        ##value.write_byte(addr1, -1 * x)
        #value.write_byte(addr2, -1 * x)
        
        print(-1 * x)
        
    # IF LAN CONNECTION == BROKEN:
        # Apply Brakes. 
        
        
    # Input sensor values. 
    # Find distance
    # check if distance is 50m if so break
    # put values in a file or send it to the computer again. 
        
    # MEANWHILE
    # Also run sensor code in this for loop, by iterating like a thousand times a second, 
    # and getting sensor values, and at particular times within those iterations, also give instructions
    # to the motor, to accelerate. The sensor values are read and immediately written to a file
    # This way the motor code is run and the sensor data is written to a file. 
    # Also before writing to the file, the sensor code starts calculating the distance covered, 
    # and checks if it exceeds a certain amount, if so then break. 
    
    # After successful execution of the motor code, and successfully saving the sensor values in a csv file, 
    # the PI now becomes the TCP server, and the main computer becomes the host. 
    # the PI then sends the csv file through, and the main computer makes a graph out of it, to then display in the GUI. 
    # this will cause the GUI to wait for the complete run of the pod, and will create a graph only after its done. 
    
    # another method would be to multithread the GUI code in the main computer, such that the PI continueously sends 
    # new sensor values say every 20 ms, and we plot the graph and or show the values in a dashboard real time. 
    # that means the PI immediately after receiving the motor code input values becomes a server, and starts sending values. 
    
        
x = 0
#print (x)
##value = bus.write_byte(addr1, 0)
##value = bus.write_byte(addr2, 0)
time.sleep(0.2)
#GPIO.output(23, True)
#GPIO.output(24, True)
time.sleep(1)
#GPIO.output(23, False)
#GPIO.output(24, False)
print("Total delay : ", (end_val / step_val) * interval / 1000 )
#x = 0
        
print('motor output given. ')       



    

    




    







