#Student 2

import CoDrone
drone = CoDrone.CoDrone()
import time
import csv
drone.pair('2159')


def get_data():
    temp = drone.get_drone_temp()
    height = drone.get_height()
    state = drone.get_state()
    pressure = drone.get_pressure()
    battery = drone.get_battery_voltage()
    throttle = drone.get_throttle()
    timer = time.process_time()
    
    
    print(temp)
    print(height)
    print(state)
    print(pressure)
    stemp = str(temp)
    sheight = str(height)
    csvwriter.writerow([sheight,stemp,state,pressure,battery,throttle,timer])

f = open("dronedata2.csv","w")
f.write("Height,Temp,State,Pressure,Battery,Throttle,Time\n")
f.close()
timer = time.process_time()

with open("dronedata2.csv","a",newline = '')as file:
    csvwriter = csv.writer(file)
    get_data()
    drone.takeoff()
    get_data()
    drone.hover(1)
    get_data()
    drone.set_throttle(50)
    drone.set_pitch(50)
    drone.move(2)
    get_data()
    drone.set_pitch(-35)
    drone.move(2)
    get_data()
    drone.hover(1)
    get_data()
    drone.land()
    get_data()

drone.close()

'''df = pd.read_csv("dronedata2")
print(df)
print(df.srd())
print(df.mean())

plt.plot['Time'],df['Height']'''
