read="input.txt"
#read="test.txt"
#read="test2.txt"
garden = []
with open(read) as file:
    for line in file:
        line = line.strip()
        #line = line.split()
        garden.append(line)
#line = open(read).read()
print(garden)

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
    per = 0
    for ar in area:
        y,x = ar
        if (y-1,x) not in area:
            per += 1
        if (y+1,x) not in area:
            per += 1
        if (y,x-1) not in area:
            per += 1
        if (y,x+1) not in area:
            per += 1
    return per*a

knownAreas = []
done = []
for y in range(len(garden)):
    for x in range(len(garden[0])):
        if (y,x) in done:
            continue
        knownAreas.append(buildGarden((y,x),garden[y][x]))

print(knownAreas)

result = 0
for ka in knownAreas:
    result += score(ka)

print(result)
