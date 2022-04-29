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
    
    print('motor control code was run once (not in a loop).')
    
    print(start_val, end_val, step_val, interval)
    
    # #channel = 6

    # #GPIO setup
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(23,GPIO.OUT)
    # GPIO.setup(24,GPIO.OUT)

    # x = int(0)

    # addr1 = 0x07
    # addr2 = 0x08

    # bus = smbus.SMBus(1)

    # #bus.write_byte(addr1, 0xFF)
    # #bus.write_byte(addr2, 0xFF)
    
    # # Stuff below this line was inside a while loop.
    # # This will now only be run once, if you wanna run it more times, 
    # # then take the input and then call this function, coz the GUI will
    # # Anyway run in a while loop, always taking input. 
    
    # #bus.write_byte(addr1, 0)
    # bus.write_byte(addr2, 0)
    # GPIO.output(23, False)
    # GPIO.output(24, False)
    # # start_val = int(input("press 1 FOR - 2 to REV: "))
    
    # if(start_val == 1):
        
    #     # end_val = int(input("Enter End Value : "))       #1-100
    #     # step_val = int(input("Enter Step Size : "))      #1-10
    #     # interval = int(input("Enter Step Delay (MicroSeconds) : "))
        
    #     for i in range(0, int((end_val / step_val))):
            
    #         x = (x + step_val) 
    #         time.sleep(interval / 1000)
    #         #value = bus.write_byte(addr1, x)
    #         value = bus.write_byte(addr2, x)
    #         print(x)

        
    # if(start_val == 2):
        
    #     end_val = int(input("Enter End Value : "))       #1-100
    #     step_val = int(input("Enter Step Size : "))      #1-10
    #     interval = int(input("Enter Step Delay (MicroSeconds) : "))
        
    #     for i in range(0, int((end_val / step_val) )):
            
    #         x = (x + step_val) 
    #         time.sleep(interval / 1000)
    #         #value = bus.write_byte(addr1, -1 * x)
    #         value = bus.write_byte(addr2, -1 * x) 
    #         print(-1 * x) 
        
    # x = 0
    # #print(x)
    # #value = bus.write_byte(addr1, 0)
    # #value = bus.write_byte(addr2, 0)
    # time.sleep(0.2)
    # GPIO.output(23, True)
    # GPIO.output(24, True)
    # time.sleep(1)
    # GPIO.output(23, False)
    # GPIO.output(24, False)
    
    # print("Total delay : ", (end_val / step_val) * interval / 1000 )
    # x = 0
    

