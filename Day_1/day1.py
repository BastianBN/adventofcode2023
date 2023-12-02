import re

def part1():
    results = []
    f = open('data.txt', 'r')
    for line in f.readlines():
        numbers = []
        for c in line:
            if c.isdigit() :
                numbers.append(c)
        if numbers:
            results.append(int(f"{numbers[0]}{numbers[-1]}"))
        else:
            results.append(0)
    print(sum(results))

def part2():
    results = []
    cal_values = []
    nbs = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    f = open('data.txt', 'r')
    for line in f.readlines():
        current = []
        for n in nbs.keys():
            if n in line:
                for match in re.finditer(n, line):
                    current.append((match.start(), nbs[match.group()]))
        for i,c in enumerate(line):
            if c.isdigit():
                current.append((i, c))
        sorted_current = sorted(current)
        result = int(f"{int(sorted_current[0][1])}{int(sorted_current[-1][1])}")
        cal_values.append(result)
    print(sum(cal_values))

if __name__ == "__main__":
    part1()
    part2()