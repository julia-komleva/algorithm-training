bench_length, cubes_amount = map(int, input().split())
cubes_coordinates = list(map(int, input().split()))


def cubes():
    bench_center = bench_length // 2
    if bench_length % 2 != 0:
        for i in range(cubes_amount):
            if cubes_coordinates[i] == bench_center:
                return bench_center,

    for i in range(cubes_amount - 1):
        if cubes_coordinates[i] < bench_center <= cubes_coordinates[i + 1]:
            return cubes_coordinates[i], cubes_coordinates[i + 1]


print(' '.join(str(i) for i in cubes()))
