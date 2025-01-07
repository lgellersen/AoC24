list1 = []
list2 = []
#with open("test.txt") as file:
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))
    
print(list1)
print(list2)
list1s=list1.copy()
list2s=list2.copy()
list1s.sort()
list2s.sort()
print(list1s)
print(list2s)

dist = 0
for one, two in zip(list1s,list2s):
    dist += abs(one - two)
    #dist += abs(list1.index(one) - list2.index(two))
    #print(one,two,list1.index(one),list2.index(two),abs(list1.index(one)-list2.index(two)))
    #list1s[list1s.index(one)] = -1
    #list2s[list2s.index(two)] = -1
print(dist)
