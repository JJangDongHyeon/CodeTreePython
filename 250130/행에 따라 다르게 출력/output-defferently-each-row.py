n = int(input())

for i in range(n):
    if i % 2 == 0:
        if i == 0:
            for j in range(n):
                print((n * i) + 1 + j, end = ' ')
        else:
            for j in range(n):
                print((i + 1) * n + j + 1, end = ' ')
    elif i % 2 != 0:
        if i == 1:
            for j in range(n):
                print(n * i + (2 * (j + 1)), end = ' ')
        else:
            for j in range(n):
                print((n * (i + 1)) + 2 + (j * 2), end = ' ' )
    print()