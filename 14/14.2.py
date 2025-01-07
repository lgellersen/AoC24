import numpy as np
from matplotlib import pyplot as plt
read="input.txt"
ydim = 103
xdim = 101

#read="test.txt"
#ydim = 7
#xdim = 11
#read="test2.txt"
poss = []
vels = []
with open(read) as file:
    for line in file:
        line = line.strip()
        line = line.split()
        p = line[0].split("=")[1]
        v = line[1].split("=")[1]
        poss.append([int(i) for i in p.split(",")])
        vels.append([int(i) for i in v.split(",")])
#line = open(read).read()

print(poss,vels)

seconds = 1000000
for s in range(seconds):
    for r in range(len(poss)):
        poss[r][0] += vels[r][0]
        poss[r][1] += vels[r][1]
    
    for r in range(len(poss)):
        if poss[r][0] < 0:
            poss[r][0] += (-poss[r][0]//xdim+1)*xdim
        if poss[r][1] < 0:
            poss[r][1] += (-poss[r][1]//ydim+1)*ydim
        if poss[r][0] >= xdim:
            poss[r][0] -= (poss[r][0]//xdim) * xdim 
        if poss[r][1] >= ydim:
            poss[r][1] -= (poss[r][1]//ydim) * ydim 
    
    q1 = q2 = q3 = q4 = 0
    for r in range(len(poss)):
        if poss[r][0] < xdim/2 - 1 and poss[r][1] < ydim/2 - 1:
            q1 += 1
        if poss[r][0] > xdim/2 and poss[r][1] < ydim/2 - 1:
            q2 += 1
        if poss[r][0] > xdim/2 and poss[r][1] > ydim/2:
            q3 += 1
        if poss[r][0] < xdim/2 - 1 and poss[r][1] > ydim/2:
            q4 += 1
    # 1st try: symmetric around y axis. Not the case
    # 2nd try: All take part, i.e., no overlap?
    md = dict()
    for p in poss:
        md[(p[0],p[1])] = "_"
    if len(poss) == len(md):
        print(s+1)
        img = np.zeros((xdim,ydim))
        for p in poss:
            img[p[0],p[1]] = 1
        plt.imshow(img.transpose())
        plt.show()
        break
#print(q1,q2,q3,q4,q1*q2*q3*q4)

