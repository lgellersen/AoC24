import numpy as np
import scipy

read="input.txt"
#read="test.txt"
#read="test2.txt"
prizes = []
As = []
Bs = []
with open(read) as file:
    for line in file:
        line = line.strip()
        line = line.split()
        print(line)
        if len(line) < 1:
            continue
        if line[1] == "A:":
            As.append((int(line[2][2:-1]),int(line[3][2:])))
        if line[1] == "B:":
            Bs.append((int(line[2][2:-1]),int(line[3][2:])))
        if line[0] == "Prize:":
            prizes.append((int(line[1][2:-1]),int(line[2][2:])))
#line = open(read).read()

result = 0
for A,B,prize in zip(As,Bs,prizes):
    print(A,B,prize)
    if True:
        add = 10000000000000
        prize = (prize[0] + add,prize[1] + add)
    a = np.array([A,B],dtype=np.int64)
    a = a.transpose()
    b = np.array(prize,dtype=np.int64)
    x = scipy.linalg.solve(a,b)
    tol = 0.01
    if abs(x[0] - round(x[0])) > tol or abs(x[1] - round(x[1])) > tol:
        continue
    x = np.array([round(x[0]),round(x[1])])
    if(np.allclose(np.dot(a,x),b) and x[0] > 0 and x[1] > 0):
        result += 3*x[0] + x[1]
    print(x)

print(result)

