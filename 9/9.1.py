# Run me using pypy3

read="input.txt"
#read="test.txt"
line = open(read).read()
line = line.strip()

expand = []
i = 0
fm = True
for l in line:
    if fm:
        expand.extend(int(l)*[str(i)])
    else:
        expand.extend(int(l)*".")
    if fm:
        fm = False
        i += 1
    else:
        fm = True
print(expand)

def rearr(arr):
    ilog = 1e6
    done = False
    while (True):
        if done:
            break
        for i in reversed(range(len(arr))):
            if arr[i] != ".":
                c = arr[i]
                ilog = i
                break
        for i in range(len(arr)):
            if arr[i] == ".":
                if i > ilog:
                    done = True
                    break
                arr[i] = c
                arr[ilog] = "."
                break
    return arr       

arr = rearr(expand)

i = 0
result = 0
for c in arr:
    if c == ".":
        break
    result += i*int(c)
    i += 1

print(result)
