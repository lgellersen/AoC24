read="input.txt"
#read="test.txt"
#read="test2.txt"
mymap = []
with open(read) as file:
    for line in file:
        line = line.strip()
        #line = line.split()
        mymap.append(line)
#line = open(read).read()
print(mymap)

def getScore(y,x,val,res):
    if y < 0 or y >= len(mymap):
        return 0
    if x < 0 or x >= len(mymap[0]):
        return 0
    if val == 9 and mymap[y][x] == "9":
        print("found",y,x)
        res[(y,x)] = "_"
    if mymap[y][x] == str(val):
        print("trying",y,x,val)
        getScore(y-1,x,val+1,res)
        getScore(y+1,x,val+1,res)
        getScore(y,x-1,val+1,res)
        getScore(y,x+1,val+1,res)
    else:
        return 0

result = 0
for y in range(len(mymap)):
    for x in range(len(mymap)):
        res = dict()
        if mymap[y][x] == "0":
            getScore(y,x,0,res)
            result += len(res)
print(result)
