x = list(map(int, input().split()))
shop_pos = -20
left = [0] * len(x)

for i in range(len(x)):
    if x[i] == 2:
        shop_pos = i
    if x[i] == 1:
        left[i] = i - shop_pos
ans = 0
shop_pos = 30
for i in range(len(x) - 1, -1, -1):
    if x[i] == 2:
        shop_pos = i
    if x[i] == 1:
        min_dist = min(shop_pos - i, left[i])
        ans = max(ans, min_dist)

print(ans)
"""
longest = 0
nearest_shop = len(x)

for i in range(len(x)):  # house
    if x[i] == 1:
        nearest_shop = len(x)
        for j in range(len(x)):  # shop
            if x[j] == 2:
                distance = abs(i - j)
                nearest_shop = min(distance, nearest_shop)
        longest = max(longest, nearest_shop)

print(longest)
"""
