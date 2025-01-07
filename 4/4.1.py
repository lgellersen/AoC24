read="input.txt"
#read="test.txt"
data = []
with open(read) as file:
    for line in file:
        line = line
        line = line.strip()
        #line = line.split()
        data.append(line)
print(data)

found = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        #print("testing x,y =",x,y," ", data[y][x])
        #Horizontal
        if len(data[y])-4 >= x and data[y][x] == "X" and data[y][x+1] == "M" and data[y][x+2] == "A" and data[y][x+3] == "S":
            found += 1
        if x >= 3 and data[y][x] == "X" and data[y][x-1] == "M" and data[y][x-2] == "A" and data[y][x-3] == "S":
            found += 1
        #vertical
        if len(data)-4 >= y and data[y][x] == "X" and data[y+1][x] == "M" and data[y+2][x] == "A" and data[y+3][x] == "S":
            found += 1
        if y >= 3 and data[y][x] == "X" and data[y-1][x] == "M" and data[y-2][x] == "A" and data[y-3][x] == "S":
            found += 1
        #diagonal
        if len(data[y]) - 4 >= x and len(data) -4 >= y and data[y][x] == "X" and data[y+1][x+1] == "M" and data[y+2][x+2] == "A" and data[y+3][x+3] == "S":
            found += 1
        if len(data[y]) - 4 >= x and y >= 3 and data[y][x] == "X" and data[y-1][x+1] == "M" and data[y-2][x+2] == "A" and data[y-3][x+3] == "S":
            found += 1
        if x >= 3 and len(data) -4 >= y and data[y][x] == "X" and data[y+1][x-1] == "M" and data[y+2][x-2] == "A" and data[y+3][x-3] == "S":
            found += 1
        if x >= 3 and y >= 3 and data[y][x] == "X" and data[y-1][x-1] == "M" and data[y-2][x-2] == "A" and data[y-3][x-3] == "S":
            found += 1
#line = open(read).read()

print(found)
