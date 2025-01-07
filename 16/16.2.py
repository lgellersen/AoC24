read="input.txt"
#read="test.txt"
#read="test2.txt"

maze = []
with open(read) as file:
    donewm = False
    for line in file:
        line = line.strip()
        #line = line.split()
        maze.append(line)
#line = open(read).read()

start = (-1,-1)
end = (-1,-1)
walls = []
sites = []

for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == "S":
            start = (y,x)
        if maze[y][x] == "E":
            end = (y,x)
        if maze[y][x] == "#":
            walls.append((y,x))
        if maze[y][x] == ".":
            sites.append((y,x))

visited = dict()
last = dict()
best = dict()
final = (1000000,(-1,-1,-1))

#Dijkstras 2023.17.1
from queue import PriorityQueue

dirs = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}

queue = PriorityQueue()
queue.put((0,(start[0],start[1],0)))
visited[(start[0],start[1],0)] = 0
cutscore = 1000000
while queue:
    score,shortest = queue.get()
    newNodes = []
    newScores = []
    #print(str(score)+": "+str(shortest))
    if (shortest[0],shortest[1]) == end:
        if score < final[0]:
            final = [score,[shortest]]
        elif score == final[0]:
            final = [score,final[1].append(shortest)]
        if cutscore == 1000000:
            cutscore = score
    if score > cutscore:
        break
    d = shortest[2]
    if (shortest[0] + dirs[d][0],shortest[1] + dirs[d][1]) not in walls:
        newScores.append(score+1)
        newNodes.append((shortest[0]+dirs[d][0],shortest[1]+dirs[d][1],d))
    newScores.append(score + 1000)
    newNodes.append((shortest[0],shortest[1],(d+1)%4))
    dnew = d-1
    if dnew == -1:
        dnew = 3
    newNodes.append((shortest[0],shortest[1],dnew))
    newScores.append(score + 1000)
    for newNode, newScore in zip(newNodes,newScores):
        if newNode not in visited or newScore < visited[newNode]:
            visited[newNode] = newScore
            last[newNode] = [shortest]
            queue.put((newScore, newNode))
        elif visited[newNode] < newScore:
            continue
        else:
            last[newNode].append(shortest)

def compPrev(current):
    best[(current[0],current[1])] = True
    if (current[0],current[1]) == start:
        return
    for prev in last[current]:
        compPrev(prev)

for fin in final[1]:
    compPrev(fin)

print("Lowest score:", final[0])
print("Number of best tiles:",len(best))
