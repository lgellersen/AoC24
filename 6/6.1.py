read="input.txt"
#read="test.txt"
gmap = []
with open(read) as file:
    doneWithRules = False
    for line in file:
        line = line.strip()
        gmap.append(line)
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


while True:
    prop = (guardPos[0] + dirct[0],guardPos[1]+dirct[1])
    if prop[0] < 0 or prop[0] > len(gmap) or prop[1] < 0 or prop[1] > len(gmap[0]):
        break
    visited[guardPos] = "_"
    if prop in obst:
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
    print(guardPos)

print(len(visited))
