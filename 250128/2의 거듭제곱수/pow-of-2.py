n = int(input())
val = 1
cnt = 0
while True:
    val *= 2
    cnt += 1
    if val == n:
        print(cnt)
        break