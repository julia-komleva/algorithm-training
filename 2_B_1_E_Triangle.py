d = int(input())
x, y = map(int, input().split())
if x >= 0 and y >= 0 and x + y <= d:
    print(0)
else:
    dist = [(x ** 2 + y ** 2, 1),
            ((x - d) ** 2 + y ** 2, 2),
            (x ** 2 + (y - d) ** 2, 3)]
    print(min(dist)[1])

"""
A = ((0 - x) ** 2 + (0 - y) ** 2) ** 0.5  
B = ((d - x) ** 2 + (0 - y) ** 2) ** 0.5
C = ((0 - x) ** 2 + (d - y) ** 2) ** 0.5


def triangle():
    
    if x + y <= d and x >= 0 and y >= 0:  # внутри или на стороне
        return 0
    if A == min(A, B, C):  # A is the nearest
        return 1
    if B == min(A, B, C):
        return 2
    return 3
    
    
print(triangle())
"""
