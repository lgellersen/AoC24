import re

read="input.txt"
#read="test.txt"
with open(read) as file:
    for line in file:
        line = line
        #line = line.strip()
        #line = line.split()
line = open(read).read()

#result = 0
#for int1,int2 in re.findall(r"mul\((\d+),(\d+)\)", line):
#    result += int(int1)*int(int2)
#
#print(result)
#exit()


do=True
result = 0
resultDO = 0
while(True):
    ind=line.find("mul(")
    doind = line.find("do")
    dontind = line.find("don't")
    if dontind < ind:
        do = False
        line = line[5:]
        continue
    elif doind < ind:
        do = True
        line = line[2:]
        continue
    if ind == -1:
        break
    line = line[ind+4:]
    print(line, result,"\n")
    oneDone = False
    int1= 0
    int2= 0
    while(True):
        if line[0].isnumeric() and not oneDone:
            int1 = 10*int1 + int(line[0])
            line= line[1:]
            continue
        if not oneDone and not line[0].isnumeric() and line[0] == ",":
            line= line[1:]
            oneDone = True
            continue
        if oneDone and line[0].isnumeric():
            int2 = 10*int2 + int(line[0])
            line= line[1:]
            continue
        if oneDone and line[0] == ")":
            if int1 >= 1000 or int2 >= 1000:
                break
            result += int1 * int2
            if do:
                resultDO += int1 * int2
        break

print(result,resultDO)
