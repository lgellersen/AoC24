read="input.txt"
#read="test.txt"
#read="test2.txt"
m = []
moves = []
with open(read) as file:
    donewm = False
    for line in file:
        line = line.strip()
        #line = line.split()
        if line == "":
            donewm = True
            continue
        if not donewm:
            m.append(line)
        else:
            moves += line
#line = open(read).read()


boxes = []
walls = []
pos = (-1,-1)

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == "#":
            walls.append((y,x))
        if m[y][x] == "O":
            boxes.append((y,x))
        if m[y][x] == "@":
            pos = (y,x)

for mov in moves:
    if mov == "^":
        s = 1
        toBePushed = []
        while True:
            if (pos[0]-s,pos[1]) in walls:
                break
            elif (pos[0]-s,pos[1]) in boxes:
                toBePushed.append((pos[0]-s,pos[1]))
                s += 1
                continue
            else:
                pos = (pos[0]-1,pos[1])
                for tbp in toBePushed[::-1]:
                    boxes.remove(tbp)
                    boxes.append((tbp[0]-1,tbp[1]))
                break
    if mov == "v":
        s = 1
        toBePushed = []
        while True:
            if (pos[0]+s,pos[1]) in walls:
                break
            elif (pos[0]+s,pos[1]) in boxes:
                toBePushed.append((pos[0]+s,pos[1]))
                s += 1
                continue
            else:
                pos = (pos[0]+1,pos[1])
                for tbp in toBePushed[::-1]:
                    boxes.remove(tbp)
                    boxes.append((tbp[0]+1,tbp[1]))
                break
    if mov == ">":
        s = 1
        toBePushed = []
        while True:
            if (pos[0],pos[1]+s) in walls:
                break
            elif (pos[0],pos[1]+s) in boxes:
                toBePushed.append((pos[0],pos[1]+s))
                s += 1
                continue
            else:
                pos = (pos[0],pos[1]+1)
                for tbp in toBePushed[::-1]:
                    boxes.remove(tbp)
                    boxes.append((tbp[0],tbp[1]+1))
                break
    if mov == "<":
        s = 1
        toBePushed = []
        while True:
            if (pos[0],pos[1]-s) in walls:
                break
            elif (pos[0],pos[1]-s) in boxes:
                toBePushed.append((pos[0],pos[1]-s))
                s += 1
                continue
            else:
                pos = (pos[0],pos[1]-1)
                for tbp in toBePushed[::-1]:
                    boxes.remove(tbp)
                    boxes.append((tbp[0],tbp[1]-1))
                break

res = 0
for box in boxes:
    res += 100*box[0] + box[1]

print(res)
