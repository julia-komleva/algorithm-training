first, second, year = map(int, input().split())

if first == second:
    print(1)
elif first < 13 and second < 13:
    print(0)
else:
    print(1)