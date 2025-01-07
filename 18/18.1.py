read="input.txt"
end = (70,70)
nCor = 1024
#read="test.txt"
#end = (6,6)
#nCor = 12
#read="test2.txt"
pos = []
with open(read) as file:
    for line in file:
        line = line.strip()
        line = line.split(",")
        pos.append(tuple([int(i) for i in line]))
#line = open(read).read()

start = (0,0)

walls = []

for i in range(nCor):
    walls.append(pos[i])

for i in range(-1,end[0]+2):
    walls.append((-1,i))
    walls.append((end[0]+1,i))
    walls.append((i,-1))
    walls.append((i,end[0]+1))

#Dijkstras 2023.17.1
from queue import PriorityQueue

def walk():
    wallset = set(walls)
    visited = dict()
    queue = PriorityQueue()
    queue.put((0,(start[0],start[1])))
    visited[(start[0],start[1])] = 0
    cutscore = 1000000
    while queue:
        score,shortest = queue.get()
        #print(str(score)+": "+str(shortest))
        if (shortest[0],shortest[1]) == end:
            if cutscore == 1000000:
                cutscore = score
            return score
            break
        props = [(shortest[0] +1,shortest[1]), (shortest[0]-1,shortest[1]),(shortest[0],shortest[1]+1),(shortest[0],shortest[1]-1)]
        for newNode in props:
            if newNode not in wallset:
                newscore = score+1
                if (newNode not in visited) or visited[newNode] > newscore:
                    visited[newNode] = newscore
                    queue.put((newscore, newNode))
        if queue.empty():
            return False

print("Part 1:",walk())

i = nCor
while True:
    walls.append(pos[i])
    if not walk():
        print("Part 2:",str(pos[i][0])+","+str(pos[i][1]))
        break
    i += 1
