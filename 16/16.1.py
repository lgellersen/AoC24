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
print(maze)

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
print(walls)

visited = dict()
#Dijkstras 2023.17.1
from queue import PriorityQueue

dirs = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}

queue = PriorityQueue()
queue.put((0,(start[0],start[1],0)))
visited[(start[0],start[1],0)] = 0
cutscore = 1000000
while queue:
    score,shortest = queue.get()
    #print(str(score)+": "+str(shortest))
    if (shortest[0],shortest[1]) == end:
        if cutscore == 1000000:
            cutscore = score
        print(score)
    if score > cutscore + 1000:
        break
    d = shortest[2]
    if (shortest[0] + dirs[d][0],shortest[1] + dirs[d][1]) not in walls:
        newscore = score+1
        newNode = (shortest[0]+dirs[d][0],shortest[1]+dirs[d][1],d)
        if (newNode not in visited) or visited[newNode] > newscore:
            visited[newNode] = newscore
            queue.put((newscore, newNode))
    newscore = score + 1000
    newNode = (shortest[0],shortest[1],(d+1)%4)
    if (newNode not in visited) or visited[newNode] > newscore:
        visited[newNode] = newscore
        queue.put((newscore, newNode))
    dnew = d-1
    if dnew == -1:
        dnew = 3
    newNode = (shortest[0],shortest[1],dnew)
    if (newNode not in visited) or visited[newNode] > newscore:
        visited[newNode] = newscore
        queue.put((newscore, newNode))
    
