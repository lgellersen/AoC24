read="input.txt"
#read="test.txt"
#read="test2.txt"
#read = "test3.txt"
wires = dict()
gates = []
with open(read) as file:
    doneWires = False
    for line in file:
        line = line.strip()
        if line == "":
            doneWires = True
            continue
        if not doneWires:
            line = line.split(": ")
            wires[line[0]] = int(line[1])
        else:
            line = line.split()
            gates.append([line[1],line[0],line[2],line[4]])
#line = open(read).read()

def findGate(op,inp1,inp2):
    for gate in gates:
        if gate[0] == op and ((gate[1] == inp1 and gate[2] == inp2) or (gate[1] == inp2 and gate[2] == inp1)):
            return gate[3]

def findSwaps():
    swaps = []
    addreg = False
    uebertrag = False
    for i in range(45):
        istr = str(i).zfill(2)
        prevuebertrag = uebertrag

        addreg = findGate("XOR","x"+istr,"y"+istr)
        t0 = findGate("AND","x"+istr,"y"+istr)

        if prevuebertrag:
            t1 = findGate("AND",addreg,prevuebertrag)
            if not t1:
                addreg,t0 = t0,addreg
                swaps.extend([t0,addreg])
                t1 = findGate("AND",addreg,prevuebertrag)

            z = findGate("XOR",prevuebertrag,addreg)

            if not z[0] == "z":
                if addreg[0] == "z":
                    addreg,z = z,addreg
                    swaps.extend([addreg,z])
                if t0[0] == "z":
                    t0,z = z,t0
                    swaps.extend([t0,z])
                if t1[0] == "z":
                    t1,z = z,t1
                    swaps.extend([t1,z])

            uebertrag = findGate("OR",t0,t1)
        else:
            uebertrag = t0
        if uebertrag and uebertrag[0] == "z" and uebertrag != "z45":
            uebertrag,z = z,uebertrag
            swaps.extend([z,uebertrag])

    return sorted(swaps)

print("Part 2:",",".join(findSwaps()))

#def run(gates,wires):
#    gatesloc = gates.copy()
#    lennow = len(gatesloc) + 1
#    while len(gatesloc) > 0:
#        if len(gatesloc) == lennow:
#            return False
#        lennow = len(gatesloc)
#        for gate in gatesloc:
#            if gate[1] in wires and gate[2] in wires:
#                if gate[0] == "AND":
#                    wires[gate[3]] = wires[gate[1]] & wires[gate[2]]
#                if gate[0] == "OR":
#                    wires[gate[3]] = wires[gate[1]] | wires[gate[2]]
#                if gate[0] == "XOR":
#                    wires[gate[3]] = wires[gate[1]] ^ wires[gate[2]]
#                gatesloc.remove(gate)
#    return wires
#
##Forge test wires
#def produce0():
#    testwires = {}
#    for i in range(100):
#        testwires["x"+f"{i:02}"] = 0
#        testwires["y"+f"{i:02}"] = 0
#    return testwires
#
#def convertnums(wires):
#    xstr = ""
#    i = 0
#    while True:
#        istr = f"{i:02}"
#        if "x"+istr in wires:
#            xstr = str(wires["x"+istr]) + xstr
#            i += 1
#        else:
#            break
#    ystr = ""
#    i = 0
#    while True:
#        istr = f"{i:02}"
#        if "y"+istr in wires:
#            ystr = str(wires["y"+istr]) + ystr
#            i += 1
#        else:
#            break
#    zstr = ""
#    i = 0
#    while True:
#        istr = f"{i:02}"
#        if "z"+istr in wires:
#            zstr = str(wires["z"+istr]) + zstr
#            i += 1
#        else:
#            break
#    x = int(xstr,2)
#    y = int(ystr,2)
#    z = int(zstr,2)
#    return x,y,z
#
#def findswap(gates,wires):
#    candidates = []
#    for i in range(len(gates)):
#        for j in range(i+1,len(gates)): 
#            g1 = gates[i][3]
#            g2 = gates[j][3]
#            testgates = gates.copy()
#            testgates[i] = (gates[i][0],gates[i][1],gates[i][2],g2)
#            testgates[j] = (gates[j][0],gates[j][1],gates[j][2],g1)
#            wires = run(testgates,wires)
#            x,y,z = convertnums(wires)
#            if x+y==z:
#                candidates.append([g1,g2,testgates])
#    return candidates
#    print("No suitable swap found")
#    exit()
#
#def accswaps(gates,swaps):
#    global candidates
#    i = 0
#    while True:
#        if i == 45 and len(swaps)==8:
#            print("Valid candidate: ",",".join(swaps))
#            candidates.append(",".join(swaps))
#            break
#        testwires = produce0()
#        testwires["x"+f"{i:02}"] = 1
#        testwires["y"+f"{i:02}"] = 1
#        i += 1
#        wires = run(gates,testwires)
#        if wires == False:
#            return
#        x,y,z = convertnums(wires)
#        if x+y==z:
#            continue
#        else:
#            candidates = findswap(gates,testwires)
#            for candidate in candidates:
#                newswaps = sorted(list(dict.fromkeys(swaps+[candidate[0],candidate[1]])))
#                accswaps(candidate[2],newswaps)
#        #wires = run(gates,testwires)
#        #x,y,z = convertnums(wires)
#        #print(x,"+",y,"=",z,x+y==z)
#        #if len(swaps) == 8:
#        #    break
#
#candidates = []
#accswaps(gates,[])
#print(candidates)
