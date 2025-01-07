from functools import lru_cache
read="input.txt"
power = 2
#read="test.txt"
#read="test2.txt"
sequences = []
with open(read) as file:
    for line in file:
        line = line.strip()
        sequences.append(line)
#line = open(read).read()
numpadmap = [["7","8","9"],["4","5","6"],["1","2","3"],["x","0","A"]]
keypadmap = [["x","^","A"],["<","v",">"]]

@lru_cache(maxsize=1024)
def padDist(n,cur):
    if n in numpadmap[0]:
        ny = 0
    elif n in numpadmap[1]:
        ny = 1
    elif n in numpadmap[2]:
        ny = 2
    else:
        ny = 3
    nx = numpadmap[ny].index(n)
    if cur in numpadmap[0]:
        cury = 0
    elif cur in numpadmap[1]:
        cury = 1
    elif cur in numpadmap[2]:
        cury = 2
    else:
        cury = 3
    curx = numpadmap[cury].index(cur)
    ret = (ny - cury, nx - curx)
    return ret

@lru_cache(maxsize=1024)
def keypaddist(n,cur):
    if n in keypadmap[0]:
        ny = 0
    else:
        ny = 1
    nx = keypadmap[ny].index(n)
    if cur in keypadmap[0]:
        cury = 0
    else:
        cury = 1
    curx = keypadmap[cury].index(cur)
    ret = (ny - cury, nx - curx)
    return ret

@lru_cache(maxsize=1024)
def nextPadStep(current,new):
    ways = [""]
    y,x = keypaddist(new,current)
    # y first
    if y < 0:
        ways[-1] += abs(y)*"^"
    if x > 0:
        ways[-1] += x*">"
    if x < 0:
        ways[-1] += abs(x)*"<"
    if y > 0:
        ways[-1] += y*"v"
    ways[-1] += "A"
    if not ((current in ["^","A"] and new in ["<"]) or (current in ["<"] and new in ["^","A"])):
        ways.append("")
        if x < 0:
            ways[-1] += abs(x)*"<"
        if y > 0:
            ways[-1] += y*"v"
        if y < 0:
            ways[-1] += abs(y)*"^"
        if x > 0:
            ways[-1] += x*">"
        ways[-1] += "A"
    if len(ways) == 1:
        return ways[0]
    else:
        return ways[0] if len(ways[0]) < len(ways[1]) else ways[1]

@lru_cache(maxsize=1024)
def padseqnew(padseq,pown):
    shortest = ""
    for i in range(len(padseq)):
        if i == 0:
            current = "A"
        else:
            current = padseq[i-1]
        shortest += nextPadStep(current,padseq[i])
    while pown > 1:
        pown -= 1
        shortest = padseqnew(shortest,pown)
    return shortest

@lru_cache(maxsize=1024)
def nextStep(current,new):
    global power
    ways = [""]
    y,x = padDist(new,current)
    # y first
    if y < 0:
        ways[-1] += abs(y)*"^"
    if x > 0:
        ways[-1] += x*">"
    if x < 0:
        ways[-1] += abs(x)*"<"
    if y > 0:
        ways[-1] += y*"v"
    ways[-1] += "A"
    if not ((current in ("1","4","7") and new in ("0","A")) or (new in ("1","4","7") and current in ("0","A"))):
        ways.append("")
        if x < 0:
            ways[-1] += abs(x)*"<"
        if y > 0:
            ways[-1] += y*"v"
        if y < 0:
            ways[-1] += abs(y)*"^"
        if x > 0:
            ways[-1] += x*">"
        ways[-1] += "A"
    shortestsequence1 = padseqnew(ways[0],power)
    if len(ways) == 1:
        return len(shortestsequence1)
    else:
        shortestsequence2 = padseqnew(ways[1],power)
        if len(shortestsequence1) < len(shortestsequence2):
            return len(shortestsequence1)
        else:
            return len(shortestsequence2)

def calc():
    res = 0
    for sequence in sequences:
        shortest = 0
        for i in range(len(sequence)):
            if i == 0:
                current = "A"
            else:
                current = sequence[i-1]
            shortest += nextStep(current,sequence[i])
        print(sequence,shortest,shortest)
        res += int(sequence[0:3])*shortest
    return res

print(calc())
