n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print((i * n) + 1 + j, end = ' ')
    else:
        for j in range(n):
            print(((i + 1) * n) - j , end = ' ')
    print()
