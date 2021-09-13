x = input()
cost = 0
for i in range(len(x) // 2):
    if x[i] != x[len(x) - i - 1]:
        cost += 1
print(cost)
