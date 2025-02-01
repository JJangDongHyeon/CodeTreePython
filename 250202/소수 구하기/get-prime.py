n = int(input())

for i in range(1, n + 1):
    cnt = 0
    for j in range(2, i + 1):
        if i % j == 0 and i == j:
            if cnt == 0:
                print(i, end = ' ')
                continue
        if i % j == 0:
            cnt += 1
        
