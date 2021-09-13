x = list(map(int, input().split()))
answer = []

seen = set()
for i in x:
    if i not in seen:

        seen.add(i)
        answer.append(i)

    else:

        if i in answer:
            answer.remove(i)

print(' '.join(map(str, answer)))