def count_sort(seq):
    min_val = min(seq)  # O(n)
    max_val = max(seq)  # O(n)
    k = (max_val - min_val + 1)  # количество возможных значений
    count = [0] * k  # O(K)
    for now in seq:
        count[now - min_val] += 1
    now_pos = 0
    for val in range(0, k):  # по всем возможным значениям
        for i in range(count[val]):
            seq[now_pos] = val + min_val
            now_pos += 1


seq = [1, 3, 4, 3, 2, 6, 2, 8, 4, 4, 4, 3, 1]
print(seq)
count_sort(seq)
print(seq)
