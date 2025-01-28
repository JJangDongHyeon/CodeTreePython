cnt = 0; result = 0
while True:
    n = int(input())
    if n % 3 == 0:
        cnt += 1
    else:
        cnt -= 1
    result += 1
    if result >= 5:
        if cnt == 5:
            print(1)
        else:
            print(0)
        break
