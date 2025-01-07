read="input.txt"
#read="test.txt"
#read="test2.txt"
secnum = []
with open(read) as file:
    for line in file:
        line = line.strip()
        secnum.append(int(line))
#line = open(read).read()

secnums = []
secnums.append(secnum)
prices = [[int(str(sn)[-1]) for sn in secnum]]
changes = [[0 for _ in secnum]]
for _ in range(2000):
    secnumnew = []
    pricenew = []
    changenew = []
    for isec in range(len(secnum)):
        sn = secnums[-1][isec]
        oldprice = prices[-1][isec]
        sn = (sn ^ (64*sn))%16777216
        sn = (int(sn/32)^sn)%16777216
        sn = ((sn*2048)^sn)%16777216
        secnumnew.append(sn)
        price = int(str(sn)[-1])
        pricenew.append(price)
        changenew.append(price-oldprice)
    secnums.append(secnumnew)
    prices.append(pricenew)
    changes.append(changenew)

secnums = tuple(secnums)
prices = tuple(prices)
changes = tuple(changes)

print("Part 1:",sum(secnums[-1]))

pricelog = []
for buyer in range(len(secnum)):
    pricelog.append(dict())
    for i in range(4,len(changes)):
        key = (changes[i-3][buyer],changes[i-2][buyer],changes[i-1][buyer],changes[i][buyer])
        if not key in pricelog[-1]:
            pricelog[-1][key] = prices[i][buyer]

def tryMonkey(monkey):
    mysum = 0
    for buyer in range(len(secnum)):
        if monkey in pricelog[buyer]:
            mysum += pricelog[buyer][monkey]
    return mysum

monkeys = []
for log in pricelog:
    monkeys.extend(list(log.keys()))
monkeys = {monkey:True for monkey in monkeys}
bestMonkey = (0,0,0,0)
score = 0
for monkey in monkeys:
    newscore = tryMonkey(monkey)
    if newscore > score:
        bestMonkey = monkey
        score = newscore
        print(monkey,score)

print("Part 2:",score)
