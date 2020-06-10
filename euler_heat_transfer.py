import matplotlib.pyplot as plt
import csv
import math

# parameter
temp = 100.0
ta = 20.0

h = 400.0

time = 0.0
dt = 0.1

d = 0.01
den = 7870.0
cp = 442.0
area = math.pi * d**2
vol = math.pi * d**3 / 6.0 
mass = den * vol

# graph data array
gtime = []
gtemp = []

# csv file
outfile = open('output.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(['i', 'time', 'temperature'])

# time loop
for i in range(1000):
    ft = h * area * (ta - temp) / (cp * mass)
    temp = temp + dt * ft
    time = time + dt

    print('i: {0:4d}, time: {1:6.2f}, temp: {2:9.6f}'.format(i, time, temp))

    gtime.append(time)
    gtemp.append(temp)

    writer.writerow([i, time, temp])

outfile.close()

# graph plot
plt.plot(gtime, gtemp)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend(['T'])
plt.show()
