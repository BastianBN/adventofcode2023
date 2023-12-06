def p1():
    p1 = float('inf')
    step = ""
    ranges = {}
    f = open('data.txt', 'r')
    lines = f.readlines()
    seeds = [int(x) for x in lines[0].split(':')[1].split()]
    for seed in seeds:
        for line in lines[1:]:
            line = line.strip('\n').split()
            if line and not line[0].isdecimal():
                step = line[0]
                ranges[step] = {}
                found = False
            elif line and line[0].isdecimal() and not found:
                line = [int(x) for x in line]
                ranges[step] = {
                    "dest": range(line[0], line[0]+line[-1]),
                    "source": range(line[1], line[1]+line[-1])
                }
                if seed in ranges[step]["source"]:
                    seed = line[0] + seed - line[1]
                    found = True
                else:
                    seed = seed
        p1 = min(p1, seed)
    print("p1 result : ", p1)

def p2():
    with open("data.txt", "r") as file:
        data = file.readlines()

    seeds = [int(i) for i in data[0].strip().split(": ")[1].split(" ")]
    mappings = []
    for line in data[2:]:
        line = line.strip()
        if line.endswith(":"):
            mappings.append([])
        elif len(line) > 0:
            mappings[-1].append([int(i) for i in line.split(" ")])

    res = 2**64
    for s, o in zip(seeds[::2], seeds[1::2]):
        ranges = [(s, s + o - 1)]
        for typemappings in mappings:
            newranges = []
            for l, h in ranges:
                found = False
                for md, ms, mo in typemappings:
                    if l >= ms and h < ms + mo:
                        newranges.append((l - ms + md, h - ms + md))
                        found = True
                    elif l < ms and h >= ms and h < ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + h - ms))
                        found = True
                    elif l < ms + mo and h >= ms + mo and l >= ms:
                        ranges.append((ms + mo, h))
                        newranges.append((md + l - ms, md + mo - 1))
                        found = True
                    elif l < ms and h >= ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + mo - 1))
                        ranges.append((ms + mo, h))
                        found = True
                    if found == True:
                        break
                if found == False:
                    newranges.append((l, h))
            ranges = newranges.copy()
        res = min(res, min(ranges)[0])
    print(res)


p1()
p2()