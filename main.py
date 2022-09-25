numberPowerPoints = 13
changeTime = 10
durationTime = 120
time = 0
rpmIndex = 0
torqueIndex = 0
path = "C:/Users/kolja/Documents/Revolute/CSV.txt"
M1Rpm = [0, 0, 0, 0]
M2Rpm = [88, 175, 250, 350]
M3Rpm = [0, 0, 0, 0]
M1Torque = [0, 0, 0, 0]
M2Torque = [0, 0, 0, 0]
M3Torque = [5, 10, 15, 19]

f = open(path, 'w')


## Lastpunkte
for n in range(numberPowerPoints*2):

    #ungerade anfang neuer Wert
    if n%2 != 0:
        time += durationTime
        f.write(str(time))
        f.write(str(","))
        f.write(str(M2Rpm[rpmIndex]))
        f.write(str(","))
        f.write(str(M2Torque[torqueIndex]))
        f.write(str(","))
        f.write(str(M1Rpm[rpmIndex]))
        f.write(str(","))
        f.write(str(M1Torque[torqueIndex]))
        f.write(str(","))
        f.write(str(M3Rpm[rpmIndex]))
        f.write(str(","))
        f.write(str(M3Torque[torqueIndex]))
        f.write(str(","))

        ## JOA usw aber das ist nicht so regelmäßig
        ## hardcode die scheisse

        f.write("0")
        f.write('\n')

    if n > 1 and n % 2 == 0:
        torqueIndex+=1

    if n > 1 and n%8 ==0:
        rpmIndex+=1
        torqueIndex=0

    # gerade ende wert
    if n%2 == 0:
        time +=changeTime
        f.write(str(time))
        f.write(str(","))
        f.write(str(M2Rpm[rpmIndex]))
        f.write(str(","))
        f.write(str(M2Torque[torqueIndex]))
        f.write(str(","))
        f.write(str(M1Rpm[rpmIndex]))
        f.write(str(","))
        f.write(str(M1Torque[torqueIndex]))
        f.write(str(","))
        f.write(str(M3Rpm[rpmIndex]))
        f.write(str(","))
        f.write(str(M3Torque[torqueIndex]))
        f.write(str(","))
        f.write("0")
        f.write('\n')



