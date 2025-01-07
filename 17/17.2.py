read="input.txt"
#read="test.txt"
#read="test2.txt"
A = -1
B = -1
C = -1
with open(read) as file:
    donewm = False
    for line in file:
        line = line.strip()
        if line == "":
            continue
        line = line.split()
        if line[1] == "A:":
            A = int(line[2])
        if line[1] == "B:":
            B = int(line[2])
        if line[1] == "C:":
            C = int(line[2])
        if line[0] == "Program:":
            insts = [int(i) for i in line[1].split(",")]
#line = open(read).read()

print("Input:",A,B,C,insts)

def combop(i,A,B,C):
    if i >= 0 and i <= 3:
        return i
    if i == 4:
        return A
    if i == 5:
        return B
    if i == 6:
        return C
    if i == 7:
        print("7 encountered")
        exit()

def solve(A,B,C,insts):
    output = []
    iid = 0
    while True:
        if iid > len(insts)-2:
            break
        if insts[iid] == 0:
            A = A//(2**combop(insts[iid+1],A,B,C))
        elif insts[iid] == 1:
             B = B ^ insts[iid+1]
        elif insts[iid] == 2:
            B = combop(insts[iid+1],A,B,C)%8
        elif insts[iid] == 3:
            if A != 0:
                iid = insts[iid+1]
                continue
        elif insts[iid] == 4:
            B = B ^ C
        elif insts[iid] == 5:
            output.append(combop(insts[iid+1],A,B,C)%8)
        elif insts[iid] == 6:
            B = A//(2**combop(insts[iid+1],A,B,C))
        elif insts[iid] == 7:
            C = A//(2**combop(insts[iid+1],A,B,C))
        iid += 2
    outstr = ""
    for o in output:
        outstr = outstr + str(o)+","
    outstr = outstr[0:-1]
    return outstr

print("Part 1:",solve(A,B,C,insts))

#Build lookup
def buildLookup(prev,p):
    lookup = dict()
    for i in range(8):
        n = solve(prev+(8**p)*i,0,0,insts).split(",")
        if len(n)-1 < p:
            prop = 0
        else:
            prop = int(n[p])
        if prop in lookup:
            lookup[prop].append(i)
        else:
            lookup[prop] = [i]
    return lookup

p = len(insts)-1
test = [2,5]
test = insts
p = len(test)-1
res = [0]
#for i in insts:
for i in insts[::-1]:
    resnew = []
    for r in res:
        lookup = buildLookup(r,p)
        if i in lookup:
            for l in lookup[i]:
                resnew.append(r + (8**p)*l)
    p -= 1
    res = sorted(resnew)

# If last int is 0, last instruction will be missing. Filter out:
for r in res.copy():
    if solve(r,0,0,insts) != ",".join([str(s) for s in insts]):
        res.remove(r)

print("Part 2:",res[0])
#2,4: B = A % 8
#1,2: B = B ^ 2
#7,5: C = A // (2**B)
#4,3: B = B ^ C
#0,3: A = A // (2**3)
#1,7: B = B ^ 7
#5,5: output B % 8
#3,0: return to start
