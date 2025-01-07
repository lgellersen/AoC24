read="input.txt"
#read="test.txt"
gmap = []
with open(read) as file:
    doneWithRules = False
    for line in file:
        line = line.strip()
        gmap.append([c for c in line])
print(gmap)

guardPos = (0,0)
dirct = (0,0)
obst = dict()
visited = dict()
for y in range(len(gmap)):
    for x in range(len(gmap[0])):
        if gmap[y][x] == "^":
            guardPos = (y,x)
            dirct = (-1,0)
        if gmap[y][x] == ">":
            guardPos = (y,x)
            dirct = (0,1)
        if gmap[y][x] == "v":
            guardPos = (y,x)
            dirct = (1,0)
        if gmap[y][x] == "<":
            guardPos = (y,x)
            dirct = (0,-1)
        if gmap[y][x] == "#":
            obst[(y,x)] = "_"
print(guardPos)
print(obst)
print(dirct)
guardPosStart = guardPos
dirctStart = dirct

def walknloop(newObst,guardPos,dirct):
    loopLog = dict()
    loop = False
    while True:
        if (guardPos[0],guardPos[1],dirct[0],dirct[1]) in loopLog:
            loop = True
            break
        #print(loopLog)
        loopLog[(guardPos[0],guardPos[1],dirct[0],dirct[1])] = "_"
        prop = (guardPos[0] + dirct[0],guardPos[1]+dirct[1])
        if prop[0] < 0 or prop[0] > len(gmap) or prop[1] < 0 or prop[1] > len(gmap[0]):
            break
        visited[guardPos] = "_"
        if prop in newObst:
            if dirct == (0,1):
                dirct = (1,0)
            elif dirct == (1,0):
                dirct = (0,-1)
            elif dirct == (0,-1):
                dirct = (-1,0)
            elif dirct == (-1,0):
                dirct = (0,1)
            continue
        guardPos = prop
        #print(guardPos)
    return loop

loopcount = 0
for y in range(len(gmap)):
    for x in range(len(gmap[0])):
        if (y,x) == guardPosStart:
            continue
        newObst = obst.copy()
        newObst[(y,x)] = "_"
        if walknloop(newObst,guardPosStart,dirctStart):
            loopcount += 1
            print(loopcount)

print(loopcount)
