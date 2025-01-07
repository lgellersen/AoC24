read="input.txt"
#read="test.txt"
#read="test2.txt"
stones = []
with open(read) as file:
    for line in file:
        line = line.strip()
        line = line.split()
        stones = [int(s) for s in line]
#line = open(read).read()
print(stones)

from functools import *
@lru_cache(maxsize=1024)
def iter(s,num):
    if num == 0:
        return 1
    if s == 0:
        return iter(1,num-1)
    elif len(str(s)) % 2 == 0:
        return iter((int(str(s)[:int(len(str(s))/2)])),num-1) + iter(int(str(s)[int(len(str(s))/2):]),num-1)
    else:
        return iter(s*2024,num-1)
    
result = 0
for s in stones:
    result += iter(s,25)

print(result)
