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

result = 0
for update in updates:
    legal = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                legal = False
                break
    if legal:
        print(update)
        print(update[len(update)//2])
        result += update[len(update)//2]

print(result)
