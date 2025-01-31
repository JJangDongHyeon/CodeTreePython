n = int(input())

cnt = 1

for i in range(n):
    for j in range(n):
        if cnt > 9:
                cnt = 1
        if i == 0:
            print(cnt, end = ' ')
            cnt += 1
        elif i > j:
            print(' ', end = ' ')
        else:
            print(cnt, end = ' ')
            cnt += 1
    print()