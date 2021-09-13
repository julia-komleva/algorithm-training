n = int(input())
numbers = set(range(1, n+1))
while True:
    line = input()
    if line == 'HELP':
        break
    answer = input()
    line = set(map(int, line.split()))
    if answer == 'YES':
        numbers &= line
    else:
        numbers -= line
    # print(numbers)
print(' '.join(map(str, numbers)))
