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

def rearr(arr):
    ilog = 1e6
    done = False
    doneFiles = dict()
    while (True):
        if done:
            break
        for i in reversed(range(len(arr))):
            if arr[i] != "." and arr[i] not in doneFiles:
                count = 1
                while arr[i-count] == arr[i]:
                    count += 1
                c = arr[i]
                if c == "0":
                    done = True
                ilog = i-count+1
                doneFiles[arr[i]] = "_"
                break
        for i in range(len(arr)):
            if arr[i] == ".":
                if i > ilog:
                    break
                counts = 1
                while arr[i+counts] == ".":
                    counts += 1
                if counts >= count:
                    for x in range(count):
                        arr[i+x] = c
                        arr[ilog+x] = "."
                    break
    return arr       

arr = rearr(expand)

i = 0
result = 0
for c in arr:
    if c == ".":
        i += 1
        continue
    result += i*int(c)
    i += 1

print(result)
