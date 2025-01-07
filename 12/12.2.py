read="input.txt"
#read="test.txt"
#read="test2.txt"
#read="E.txt"
garden = []
with open(read) as file:
    for line in file:
        line = line.strip()
        #line = line.split()
        garden.append(line)
#line = open(read).read()

def buildGarden(pos,c):
    y,x = pos
    if y < 0 or x < 0 or y >= len(garden) or x >= len(garden[0]):
        return []
    if (y,x) in done:
        return []
    if garden[y][x] == c:
        done.append((y,x))
        return [(y,x)]+buildGarden((y-1,x),c)+buildGarden((y+1,x),c) + buildGarden((y,x-1),c) + buildGarden((y,x+1),c)
    else:
        return []

def score(area):
    a = len(area)
    sides = dict()
    for ar in area:
        y,x = ar
        if (y-1,x) not in area:
            if ('yd',y-1) in sides:
                sides[('yd',y-1)].append(x)
            else:
                sides[('yd',y-1)] = [x]
        if (y+1,x) not in area:
            if ('yu',y+1) in sides:
                sides[('yu',y+1)].append(x)
            else:
                sides[('yu',y+1)] = [x]
        if (y,x-1) not in area:
            if ('xd',x-1) in sides:
                sides[('xd',x-1)].append(y)
            else:
                sides[('xd',x-1)] = [y]
        if (y,x+1) not in area:
            if ('xu',x+1) in sides:
                sides[('xu',x+1)].append(y)
            else:
                sides[('xu',x+1)] = [y]
    sc = 0
    for side in sides:
        sides[side].sort()
        sc += 1
        for i in range(len(sides[side])):
            if i == 0:
                continue
            if sides[side][i] - sides[side][i-1] > 1:
                sc += 1
    return sc*a

knownAreas = []
done = []
for y in range(len(garden)):
    for x in range(len(garden[0])):
        if (y,x) in done:
            continue
        knownAreas.append(buildGarden((y,x),garden[y][x]))

result = 0
for ka in knownAreas:
    result += score(ka)

print(result)
