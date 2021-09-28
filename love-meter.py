games = ["League", "Barotrauma", "Factorio", "Civ", "Minecraft", "Dbd", "Terraria", "Phasmophobia", "Dread",
         "crusader kings 2"]
names = ["speed", "glebu", "spood", "salt", "slav", "cat", "goga"]
game_scores = []

for i in range(0, len(games)):
    game_scores.append(0)

speed = [10, 8, 10, 1, 8, 1, 6, 5, 7, 1]
glebu = [10, 8, 1, 10, 8, 6, 7, 3, 7, 1]
spood = [2, 9, 1, 7, 8, 1, 5, 4, 7, 1]
salt = [2, 6, 1, 8, 9, 6, 6, 4, 9, 1]
slav = [10, 3, 7, 10, 7, 6, 10, 8, 10, 1]
cat = [9, 8, 9, 6, 4, 6, 8, 10, 10, 1]
goga = [1, 1, 1, 10, 1, 1, 1, 1, 1, 10]

players = [speed, glebu, spood, salt, slav, cat, goga]


def difference(a, b):
    return abs(a - b) ** 2


def calculate(a, b):
    max = 800
    sum = 0
    for i in range(0, len(games) - 1):
        sum += difference(a[i], b[i])
    result = 100 - (sum / max * 100)
    return result


best = 0
best_i = 0
best_j = 0
minimum = 100

for i in range(0, len(players)):
    for j in range(0, len(players)):
        if i == j:
            continue
        value = calculate(players[i], players[j])
        print(names[i], "and", names[j], " = ", value, "%")
        if value > best:
            best_i = i
            best_j = j
            best = value
        if value < minimum:
            minimum = value
            min_i = i
            min_j = j

for i in range(0, len(games)):
    for j in range(0, len(players)):
        game_scores[i] += players[j][i]

print("best lovers:", names[best_i], "and", names[best_j], "with", best, "%")
print("haters:", names[min_i], "and", names[min_j], "with", minimum, "%")
print("most loved game:", games[game_scores.index(max(game_scores))])
print("most hated game:", games[game_scores.index(min(game_scores))])
