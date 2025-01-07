read="input.txt"
#read="test.txt"
ant = []
with open(read) as file:
    for line in file:
        line = line.strip()
        #line = line.split()
        ant.append(line)
#line = open(read).read()
print(ant)

pairs = dict()
for y in range(len(ant)):
    for x in range(len(ant[0])):
        al = ant[y][x]
        if al != ".":
            if al in pairs:
                pairs[al].append((y,x))
            else:
                pairs[al] = [(y,x)]

an = dict()
for pair in pairs:
    for a1 in pairs[pair]:
        for a2 in pairs[pair]:
            print("Checking",a1,a2)
            if a1 != a2:
                diff = (a2[0]-a1[0],a2[1]-a1[1])
                prop1 = (a1[0] - diff[0], a1[1] - diff[1])
                prop2 = (a2[0] + diff[0], a2[1] + diff[1])
                if prop1[0] < len(ant) and prop1[0] >= 0 and prop1[1] >= 0 and prop1[1] < len(ant[0]):
                    an[prop1] = "_"
                if prop2[0] < len(ant) and prop2[0] >= 0 and prop2[1] >= 0 and prop2[1] < len(ant[0]):
                    an[prop2] = "_"

print(len(an))
