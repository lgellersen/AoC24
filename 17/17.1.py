read="input.txt"
#read="test.txt"
#read="test2.txt"
A = -1
B = -1
C = -1
with open(read) as file:
    donewm = False
    for line in file:
        line = line.strip()
        if line == "":
            continue
        line = line.split()
        if line[1] == "A:":
            A = int(line[2])
        if line[1] == "B:":
            B = int(line[2])
        if line[1] == "C:":
            C = int(line[2])
        if line[0] == "Program:":
            insts = [int(i) for i in line[1].split(",")]
#line = open(read).read()

print(A,B,C,insts)

def combop(i):
    if i >= 0 and i <= 3:
        return i
    if i == 4:
        return A
    if i == 5:
        return B
    if i == 6:
        return C
    if i == 7:
        print("7 encountered")
        exit()

output = []
iid = 0
while True:
    if iid > len(insts)-2:
        break
    if insts[iid] == 0:
        A = A//(2**combop(insts[iid+1]))
    elif insts[iid] == 1:
        B = B ^ insts[iid+1]
    elif insts[iid] == 2:
        B = combop(insts[iid+1])%8
    elif insts[iid] == 3:
        if A != 0:
            iid = insts[iid+1]
            continue
    elif insts[iid] == 4:
        B = B ^ C
    elif insts[iid] == 5:
        output.append(combop(insts[iid+1])%8)
    elif insts[iid] == 6:
        B = A//(2**combop(insts[iid+1]))
    elif insts[iid] == 7:
        C = A//(2**combop(insts[iid+1]))
    iid += 2

print(output)
outstr = ""
for o in output:
    outstr = outstr + str(o)+","
outstr = outstr[0:-1]
print(outstr)
