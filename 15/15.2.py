read="input.txt"
#read="test.txt"
#read="test2.txt"
#read="test3.txt"
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

newm = []
for y in range(len(m)):
    newm.append([])
    for x in range(len(m[0])):
        if m[y][x] == "#":
            newm[y].extend(["#","#"])
        if m[y][x] == "O":
            newm[y].extend(["[","]"])
        if m[y][x] == ".":
            newm[y].extend([".","."])
        if m[y][x] == "@":
            newm[y].extend(["@","."])



boxes = []
walls = []
pos = (-1,-1)

for y in range(len(newm)):
    for x in range(len(newm[0])):
        if newm[y][x] == "#":
            walls.append((y,x))
        if newm[y][x] == "[":
            boxes.append((y,x))
        if newm[y][x] == "@":
            pos = (y,x)

def vizualise():
    vis = [["."]*len(newm[0])]
    for i in range(len(newm)-1):
        vis.append(vis[0].copy())
    vis[pos[0]][pos[1]] = "@"
    for box in boxes:
        vis[box[0]][box[1]] = "["
        vis[box[0]][box[1]+1] = "]"
    for wall in walls:
        vis[wall[0]][wall[1]] = "#"
    for line in vis:
        print(''.join(line))
    print()

#print("Initial state:")
#vizualise()

def pushUp(box):
    toBePushedL = []
    if (box[0]-1,box[1]) in walls or (box[0]-1,box[1]+1) in walls:
        return False
    if (box[0]-1,box[1]) in boxes:
        toBePushedL = pushUp((box[0]-1,box[1]))
        if toBePushedL == False:
            return False
    if (box[0]-1,box[1]-1) in boxes:
        toBePushedL = pushUp((box[0]-1,box[1]-1))
        if toBePushedL == False:
            return False
    if (box[0]-1,box[1]+1) in boxes:
        toBePushedL2 = pushUp((box[0]-1,box[1]+1))
        if toBePushedL2 == False:
            return False
        toBePushedL.extend(toBePushedL2)
    toBePushedL.append(box)
    ret = toBePushedL
    return ret

def pushDown(box):
    toBePushedL = []
    if (box[0]+1,box[1]) in walls or (box[0]+1,box[1]+1) in walls:
        return False
    if (box[0]+1,box[1]) in boxes:
        toBePushedL = pushDown((box[0]+1,box[1]))
        if toBePushedL == False:
            return False
    if (box[0]+1,box[1]-1) in boxes:
        toBePushedL = pushDown((box[0]+1,box[1]-1))
        if toBePushedL == False:
            return False
    if (box[0]+1,box[1]+1) in boxes:
        toBePushedL2 = pushDown((box[0]+1,box[1]+1))
        if toBePushedL2 == False:
            return False
        toBePushedL.extend(toBePushedL2)
    toBePushedL.append(box)
    return(toBePushedL)

def pushRight(box):
    toBePushedL = []
    if (box[0],box[1]+2) in walls:
        return False
    if (box[0],box[1]+2) in boxes:
        toBePushedL = pushRight((box[0],box[1]+2))
        if toBePushedL == False:
            return False
    toBePushedL.append(box)
    return(toBePushedL)

def pushLeft(box):
    toBePushedL = []
    if (box[0],box[1]-1) in walls:
        return False
    if (box[0],box[1]-2) in boxes:
        toBePushedL = pushLeft((box[0],box[1]-2))
        if toBePushedL == False:
            return False
    toBePushedL.append(box)
    return(toBePushedL)

for mov in moves:
    if mov == "^":
        toBePushed = []
        if (pos[0]-1,pos[1]) in walls:
            continue
        elif (pos[0]-1,pos[1]) in boxes:
            toBePushed = pushUp((pos[0]-1,pos[1]))
            if toBePushed != False:
                toBePushedD = dict()
                for tbp in toBePushed[::-1]:
                    toBePushedD[tbp] = "_"
                for tbp in toBePushedD:
                    boxes.remove(tbp)
                    boxes.append((tbp[0]-1,tbp[1]))
                pos = (pos[0]-1,pos[1])
        elif (pos[0]-1,pos[1]-1) in boxes:
            toBePushed =pushUp((pos[0]-1,pos[1]-1))
            if toBePushed != False:
                toBePushedD = dict()
                for tbp in toBePushed[::-1]:
                    toBePushedD[tbp] = "_"
                for tbp in toBePushedD:
                    boxes.remove(tbp)
                    boxes.append((tbp[0]-1,tbp[1]))
                pos = (pos[0]-1,pos[1])
        else:
            pos = (pos[0]-1,pos[1])
    if mov == "v":
        toBePushed = []
        if (pos[0]+1,pos[1]) in walls:
            continue
        elif (pos[0]+1,pos[1]) in boxes:
            toBePushed = pushDown((pos[0]+1,pos[1]))
            if toBePushed != False:
                toBePushedD = dict()
                for tbp in toBePushed[::-1]:
                    toBePushedD[tbp] = "_"
                for tbp in toBePushedD:
                    boxes.remove(tbp)
                    boxes.append((tbp[0]+1,tbp[1]))
                pos = (pos[0]+1,pos[1])
        elif (pos[0]+1,pos[1]-1) in boxes:
            toBePushed =pushDown((pos[0]+1,pos[1]-1))
            if toBePushed != False:
                toBePushedD = dict()
                for tbp in toBePushed[::-1]:
                    toBePushedD[tbp] = "_"
                for tbp in toBePushedD:
                    boxes.remove(tbp)
                    boxes.append((tbp[0]+1,tbp[1]))
                pos = (pos[0]+1,pos[1])
        else:
            pos = (pos[0]+1,pos[1])
    if mov == ">":
        toBePushed = []
        if (pos[0],pos[1]+1) in walls:
            continue
        elif (pos[0],pos[1]+1) in boxes:
            toBePushed = pushRight((pos[0],pos[1]+1))
            if toBePushed != False:
                for tbp in toBePushed[::-1]:
                    boxes.remove(tbp)
                    boxes.append((tbp[0],tbp[1]+1))
                pos = (pos[0],pos[1]+1)
        else:
            pos = (pos[0],pos[1]+1)
    if mov == "<":
        toBePushed = []
        if (pos[0],pos[1]-1) in walls:
            continue
        elif (pos[0],pos[1]-2) in boxes:
            toBePushed = pushLeft((pos[0],pos[1]-2))
            if toBePushed != False:
                for tbp in toBePushed[::-1]:
                    boxes.remove(tbp)
                    boxes.append((tbp[0],tbp[1]-1))
                pos = (pos[0],pos[1]-1)
        else:
            pos = (pos[0],pos[1]-1)
    #print("Move",mov+":")
    #vizualise()


res = 0
for box in boxes:
    res += 100*box[0] + box[1]

print(res)
