num = 1
x = []
while num != 0:
    num = int(input())
    x.append(num)
x.pop()
m = max(x)
cnt = 0
# print(x)
for i in x:
    if i == m:
        cnt += 1
print(cnt)
