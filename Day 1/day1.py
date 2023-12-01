def part1():
    digits = []
    results = []
    f = open('data.txt', 'r')
    for line in f.readlines():
        numbers = []
        for c in line:
            if c.isnumeric() :
                numbers.append(c)
        digits.append(numbers)
    for line in digits:
        results.append(int(f"{line[0]}{line[-1]}"))

    print(sum(results))

def part2():
    pass

if __name__ == "main":
    part1()

# or ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]