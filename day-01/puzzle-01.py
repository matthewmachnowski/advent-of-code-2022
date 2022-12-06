
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


print(f"PART 1 SOLUTION: {max(all)}")
