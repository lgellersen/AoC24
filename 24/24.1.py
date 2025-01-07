read="input.txt"
#read="test.txt"
#read="test2.txt"
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
            gates.append((line[1],line[0],line[2],line[4]))
#line = open(read).read()

print(wires)
print(gates)

while len(gates) > 0:
    for gate in gates:
        print(gate[3])
        if gate[1] in wires and gate[2] in wires:
            if gate[0] == "AND":
                wires[gate[3]] = wires[gate[1]] & wires[gate[2]]
            if gate[0] == "OR":
                wires[gate[3]] = wires[gate[1]] | wires[gate[2]]
            if gate[0] == "XOR":
                wires[gate[3]] = wires[gate[1]] ^ wires[gate[2]]
            gates.remove(gate)

print(wires)

zstr = ""
i = 0
while True:
    istr = f"{i:02}"
    if "z"+istr in wires:
        zstr = str(wires["z"+istr]) + zstr
        i += 1
    else:
        break

print(zstr)
print(int(zstr,2))
