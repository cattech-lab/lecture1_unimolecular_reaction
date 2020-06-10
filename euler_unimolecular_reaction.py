import matplotlib.pyplot as plt
import csv

# parameter
a = 1.0
b = 0.0
t = 0.0
k = 0.1
dt = 0.1

# graph data array
gt = []
ga = []
gb = []

# csv file
outfile = open('output.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(['i', 't', 'A', 'B'])

# time loop
for i in range(1000):
    fa = -k * a
    fb = k * a
    
    a = a + dt * fa
    b = b + dt * fb
    t = t + dt

    print('i: {0:4d}, t: {1:6.2f}, A: {2:9.6f}, B: {3:9.6f}'.format(i, t, a, b))

    gt.append(t)
    ga.append(a)
    gb.append(b)

    writer.writerow([i, t, a, b])

outfile.close()

# graph plot
plt.plot(gt, ga)
plt.plot(gt, gb)
plt.xlabel('t')
plt.ylabel('A,B')
plt.legend(['A', 'B'])
plt.show()
