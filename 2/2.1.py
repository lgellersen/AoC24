read="input.txt"
#read="test.txt"
reports = []
with open(read) as file:
    for line in file:
        line = line.strip()
        line = line.split()
        reports.append([int(number) for number in line])

numSave = 0
for report in reports:
    print("working on ",report)
    inc = 0
    for i in range(len(report)):
        if i == 0:
            continue
        if i == 1:
            if report[i] > report[0]:
                inc = 1
                print("increasing")
            elif report[i] < report[0]:
                inc = -1
                print("decreasing")
        if i > 1:
            if report[i] > report[i-1] and inc != 1:
                print("Wasn't decreasing")
                break
            if report[i] < report[i-1] and inc != -1:
                print("Wasn't increasing")
                break
        diffabs = abs(report[i] - report[i-1])
        if diffabs < 1 or diffabs > 3:
            print("Differences was ",diffabs)
            break
        if i == len(report) -1:
            numSave += 1
            print("This was good!")

print(numSave)


