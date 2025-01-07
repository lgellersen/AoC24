read="input.txt"
#read="test.txt"
#read="test2.txt"
keys = []
locks = []
with open(read) as file:
    this = []
    for line in file:
        line = line.strip()
        if line == "":
            if this[0] == "#####":
                locks.append(this)
            elif this[0] == ".....":
                keys.append(this)
            else:
                print(wtf)
                exit()
            this = []
            continue
        else:
            this.append(line)
    if this[0] == "#####":
        locks.append(this)
    elif this[0] == ".....":
        keys.append(this)

keysconv = []
locksconv = []

for key in keys:
    keynums = [None for _ in range(5)]
    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j] == "#":
                if keynums[j] == None:
                    keynums[j] = 6-i
    keysconv.append(tuple(keynums))

for lock in locks:
    locknums = [None for _ in range(5)]
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == ".":
                if locknums[j] == None:
                    locknums[j] = i-1
    locksconv.append(tuple(locknums))

fits = 0
for key in keysconv:
    for lock in locksconv:
        fit = True
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                fit = False
                break
        if fit:
            fits += 1
print("Part 1:",fits)
