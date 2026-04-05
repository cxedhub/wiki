

import CoDrone
drone = CoDrone.CoDrone()
import time
import csv

def get_data():
    temp = drone.get_drone_temp()
    height= drone.get_height()
    pressure = drone.get_pressure()
    print(temp)
    print(height)
    print(pressure)       
    csvwriter.writerow([height,temp,pressure])
drone = CoDrone.CoDrone()
drone.pair('4083')


f =open("dronedata.csv", "w")
f.write("Height, Temp, Pressure\n")
f.close()
timer = time.process_time()


with open("dronedata.csv", "a", newline = '')as file:
        csvwriter = csv.writer(file)
        drone.takeoff()
        drone.hover(1)
        get_data()
        drone.set_yaw(10)
        drone.hover(2)
        get_data()
        drone.set_pitch(30)
        drone.move(2)
        get_data()
        drone.hover(1)
        get_data()
        drone.set_roll(10)
        get_data()
        
        
drone.close()
