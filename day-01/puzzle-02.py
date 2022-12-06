with open('input.txt') as file:
    data = file.read().split("\n")

all = []
score = 0
for line in data:
    if line == '':
        all.append(score)
        score = 0
    else:
        score += int(line)

all = sorted(all, reverse=True)
print(f"PART 2 SOLUTION: {all[0] + all[1] + all[2]}")
