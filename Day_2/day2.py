from functools import reduce

def solve():
    p1 = 0
    p2 = 0
    f = open('data.txt', 'r')
    for line in f.readlines():
        g, sets = line.strip('\n').split(': ')
        game = sets.split('; ')
        game_score = 0
        maxs = {
            "blue":0,
            "green":0,
            "red":0,
            }
        for s in game:
            game_p1 = {
                "blue":0,
                "green":0,
                "red":0,
                }
            cubes = [cubes for cubes in s.split(', ')]
            for cube in cubes:
                number, color = cube.split(' ')
                game_p1[color] += int(number)
                maxs[color] = max(maxs[color], int(number))
            if (game_p1["red"] <= 12) and (game_p1["green"] <= 13) and (game_p1["blue"] <= 14):
                game_score += 1
            if game_score == len(game):
                p1 += int(g.split(' ')[1])
        p2 += reduce(lambda x, y: x*y, maxs.values())        
    print("p1 :", p1)
    print("p2 :", p2)

solve()