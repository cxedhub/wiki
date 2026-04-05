#Student1
import CoDrone
drone = CoDrone.CoDrone()
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
drone.pair('4083')
f = open('dronedata.csv','w')
f.write('Height,Temp,Pressure,State,Battery,Throttle,Timer\n')
f.close()
timer = time.process_time()
def get_data():
    temp = drone.get_drone_temp()
    height = drone.get_height()
    pressure = drone.get_pressure()
    state = drone.get_state()
    battery = drone.get_battery_voltage()
    throttle = drone.get_throttle()
    timer = time.process_time()
    print(temp)
    print(height)
    print(pressure)
    print(state)
    print(battery)
    print(throttle)
    print(timer)
    stemp = str(temp)
    sheight = str(height)
    spr = str(pressure)
    sstate = state
    sthrottle = str(throttle)
    sbattery = str(battery)
    stimer = str(timer)
    csvwriter.writerow([sheight,stemp,spr,sstate,sbattery,sthrottle,stimer])
    
with open('dronedata.csv','a',newline='')as file:
    csvwriter = csv.writer(file)
    drone.takeoff()
    drone.hover(1)
    drone.set_throttle(80)
    get_data()
    drone.set_pitch(50)
    drone.move(4)
    get_data()
    drone.set_pitch(-20)
    drone.move(3)
    get_data()
    drone.land()
    get_data()
drone.close()



