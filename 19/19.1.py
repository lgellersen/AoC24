from functools import *

read="input.txt"
#read="test.txt"
#read="test2.txt"
pos = []
patterns = []
designs = []
with open(read) as file:
    donewithpatterns = False
    for line in file:
        line = line.strip()
        if line == "":
            continue
        if not donewithpatterns:
            patterns = line.split(", ")
            donewithpatterns = True
            continue
        designs.append(line)
#line = open(read).read()

print(patterns, designs)

@lru_cache(maxsize=1024)
def works(design):
    ways = 0
    for pat in patterns:
        if design[0:len(pat)] == pat:
            if len(design) == len(pat):
                ways += 1
            else:
                ways += works(design[len(pat):])
    return ways

possible = 0
ways = 0
for design in designs:
    wd = works(design)
    if wd > 0:
        print(design,"yes")
        possible += 1
        ways += wd
    else:
        print(design,"no")

print("Part 1:",possible)
print("Part 2:",ways)
