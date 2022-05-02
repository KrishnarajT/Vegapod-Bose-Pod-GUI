# from mpu6050 import mpu6050
import time
import random



def get_accel_output():
    # mpu = mpu6050(0x68)

    # print('Sensor output has been called')

    # print("Temp: "+str(mpu.get_temp()))
    # print()

    # accel_data = mpu.get_accel_data()
    # print("Acc X: " +str(accel_data['x']))
    # print("Acc Y: " +str(accel_data['y']))
    # print("Acc Z: " +str(accel_data['z']))
    # print()

    # gyro_data = mpu.get_gyro_data()
    # print("Gyro X: " +str(gyro_data['x']))
    # print("Gyro Y: " +str(gyro_data['y']))
    # print("Gyro Z: " +str(gyro_data['z']))
    # print()
    # print('=========================')
    # accel_data = [1, 1, 1]
    # ax.setText(str(accel_data[0]))
    # gyro_data = [2, 2, 2]
    accel_data = []
    for i in range(3):
        accel_data.append(random.choice(range(100)))
    print(accel_data)
    return accel_data


def get_gyro_output():
    gyro_data = []
    for i in range(3):
        gyro_data.append(random.choice(range(100)))
    print(gyro_data)
    # gyro_data = [21, 212, 23]
    return gyro_data