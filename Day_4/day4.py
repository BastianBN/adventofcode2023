def solve():
    p1 = 0
    p2 = 0
    lines = []
    f = open('data.txt', 'r')
    lines = f.readlines()
    total_cards = {i: 1 for i in range(1, len(lines)+1)}
    for line_nb, line in enumerate(lines):
        line = line.strip("\n").split(": ")[1].split(' | ')
        winning_numbers = 0
        card_score = 0
        first = True
        for number in line[1].split(" "):
            if number.isdecimal() and number in line[0].split(" "):
                winning_numbers += 1
                if first:
                    card_score += 1
                    first = False
                else:
                    card_score *= 2
        for i in range(line_nb+2, line_nb + 2 + winning_numbers):
            total_cards[i] += 1 * total_cards[line_nb+1]
        p1 += card_score
    p2 =sum(total_cards.values())
    print(p1)
    print(p2)

solve()