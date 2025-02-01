m = int(input())

for i in range(m):
    cnt = 0
    n = int(input()) 
    for j in range(100):
        if n == 1 or n == 0:
            break
        elif n % 2 == 0:
            n = n / 2
            cnt += 1
        else:
            n = n * 3 + 1
            cnt += 1
    print(cnt)