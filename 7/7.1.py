read="input.txt"
#read="test.txt"
cal = dict()
with open(read) as file:
    for line in file:
        line = line.strip()
        line = line.split(":")
        cal[int(line[0])] = [int(c) for c in line[1].split()]
#line = open(read).read()
print(cal)

def possibleResults(numbers):
    if len(numbers) > 2:
        res1 = []
        res2 = []
        res1.append(numbers[0] + numbers[1])
        res1.extend(numbers[2:])
        res2.append(numbers[0] * numbers[1])
        res2.extend(numbers[2:])
        done1 = possibleResults(res1)
        done2 = possibleResults(res2)
        done1.extend(done2)
        return done1
    else:
        return [numbers[0]+numbers[1],numbers[0]*numbers[1]]

res = 0
for key in cal:
    pres = possibleResults(cal[key])
    if key in pres:
        res += key

print(res)
