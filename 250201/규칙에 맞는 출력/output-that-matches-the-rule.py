n = int(input())
cnt = 0
for i in range(n, 0 , -1):
    for j in range(n):
        cnt = i + j
        print(cnt, end = ' ')
        if cnt == n:
            break       
    print()