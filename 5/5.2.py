read="input.txt"
#read="test.txt"
data = []
rules = []
updates = []
with open(read) as file:
    doneWithRules = False
    for line in file:
        line = line.strip()
        if line == "":
            doneWithRules = True
            continue
        if not doneWithRules:
            line = line.split("|")
            rules.append([int(a) for a in line])
        else:
            updates.append([int(a) for a in line.split(",")])
print(rules)
print(updates)
#line = open(read).read()

def order(iup):
    while True:
        ordered = True
        for rule in rules:
            if rule[0] in updates[iup] and rule[1] in updates[iup]:
                if updates[iup].index(rule[0]) > updates[iup].index(rule[1]):
                    print("before: ",updates[iup])
                    updates[iup].insert(updates[iup].index(rule[0])+1,rule[1])
                    del updates[iup][updates[iup].index(rule[1])]
                    print("after: ",updates[iup])
                    ordered = False
                    break
        if ordered == True:
            break


result = 0
for iup in range(len(updates)):
    legal = True
    for rule in rules:
        if rule[0] in updates[iup] and rule[1] in updates[iup]:
            if updates[iup].index(rule[0]) > updates[iup].index(rule[1]):
                legal = False
                order(iup)
    if not legal:
        print(updates[iup])
        print(updates[iup][len(updates[iup])//2])
        result += updates[iup][len(updates[iup])//2]

print(result)
