N, start, finish = map(int, input().split())

dist1 = abs(start - finish) - 1
dist2 = N - 2 - dist1
print(min(dist1, dist2))
"""
if start < finish:
    right = finish - start - 1
    left = N - finish + start - 1
else:
    right = N - start + finish - 1
    left = start - finish - 1

print(min(right, left))
"""