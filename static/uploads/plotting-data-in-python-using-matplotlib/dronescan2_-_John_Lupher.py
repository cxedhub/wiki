import CoDrone
drone = CoDrone.CoDrone()
import time
import csv
def get_data():
    temp = drone.get_drone_temp()
    height = drone.get_height()
    print(temp)
    print(height)
    stemp = str(temp)
    sheight = str(height)
    csvwriter.writerow([sheight,stemp])

drone = CoDrone.CoDrone()
drone.pair('8934')

f = open("dronedata.csv","w")
f.write("Height,Temp\n")
f.close()
timer = time.process_time()

while timer<10:
    drone.move(0,0,0,100)
    with open("dronedata.csv","a",newline='')as file:
        csvwriter = csv.writer(file)
        get_data()
        drone.takeoff()
        get_throttle()
        drone.hover(1)
        get_data()
        drone.set_yaw(100)
        drone.hover(6)
        get_data()
        drone.hover(1)
        drone.set_pitch(10)
        drone.move(6)
        get_data()
        drone.land()
        get_data()

drone.close()
