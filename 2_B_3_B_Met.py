x = list(map(int, input().split()))
met = {}
for i in x:
    if i in met:
        print('YES')
    else:
        met[i] = 1
        print('NO')
