import networkx as nx

read="input.txt"
#read="test.txt"
#read="test2.txt"
connections = []
with open(read) as file:
    for line in file:
        line = line.strip()
        line = line.split("-")
        connections.append((line[0],line[1]))
#line = open(read).read()

graph = nx.Graph(connections)
cliques = nx.find_cliques(graph)
sets = []
maxlen = 0
maxset = []
for c in nx.find_cliques(graph):
    if len(c) > maxlen:
        maxlen = len(c)
        maxset = sorted(c)
    ct = []
    if len(c) >= 3:
        for c1 in c:
            if c1[0] == "t":
                ct.append(c1)
    for c1 in ct:
        for c2 in c:
            for c3 in c:
                if c1 != c2 and c1 != c3 and c2 != c3:
                    new = tuple(sorted([c1,c2,c3]))
                    if new not in sets:
                        sets.append(new)
print("Part 1:",len(sets))
print("Part 2:",",".join(maxset))



