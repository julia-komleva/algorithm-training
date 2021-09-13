m = int(input())
patterns = []
for i in range(m):
    patterns.append(input())
n = int(input())
plates = []
matched = [0] * n
for i in range(n):
    plate = input()
    plates.append(plate)
    for j in patterns:
        if set(j).issubset(plate):
            matched[i] += 1
maximum = max(matched)
answer = []
for i in range(n):
    if matched[i] == maximum:
        print(plates[i])

