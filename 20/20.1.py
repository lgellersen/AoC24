read="input.txt"
saveatleast = 100
#read="test.txt"
#saveatleast = 1
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

for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == "S":
            start = (y,x)
        if maze[y][x] == "E":
            end = (y,x)
        if maze[y][x] == "#":
            walls.append((y,x))

#Dijkstras 2023.17.1
from queue import PriorityQueue

def walk():
    wallset = set(walls)
    visited = dict()
    queue = PriorityQueue()
    queue.put((0,(start[0],start[1])))
    visited[(start[0],start[1])] = 0
    cutscore = 1000000
    while not queue.empty():
        score,shortest = queue.get()
        #print(str(score)+": "+str(shortest))
        if (shortest[0],shortest[1]) == end:
            if cutscore == 1000000:
                cutscore = score
            return score,visited
            break
        props = [(shortest[0] +1,shortest[1]), (shortest[0]-1,shortest[1]),(shortest[0],shortest[1]+1),(shortest[0],shortest[1]-1)]
        for newNode in props:
            if newNode not in wallset:
                newscore = score+1
                if (newNode not in visited) or visited[newNode] > newscore:
                    visited[newNode] = newscore
                    queue.put((newscore, newNode))
        if queue.empty():
            return False,visited

dist,visited = walk()
print("No cheating:",dist)
cheats1 = {}
cheats2 = {}
for vis1 in visited:
    for vis2 in visited:
        if abs(vis2[0]-vis1[0]) + abs(vis2[1] - vis1[1]) <= 2:
            if visited[vis2] - visited[vis1] >= saveatleast+2:
                cheats1[(vis1,vis2)] = True
        if abs(vis2[0]-vis1[0]) + abs(vis2[1] - vis1[1]) <= 20:
            if visited[vis2] - visited[vis1] >= saveatleast+abs(vis2[0]-vis1[0]) + abs(vis2[1]-vis1[1]):
                cheats2[(vis1,vis2)] = True
numcheats1 = len(cheats1)
numcheats2 = len(cheats2)
print("Part 1:",numcheats1)
print("Part 2:",numcheats2)
#cheats = cheatWalk()
#numcheats = 0
#for cheat in cheats:
#    numcheats += cheats[cheat]
#print(cheats)
