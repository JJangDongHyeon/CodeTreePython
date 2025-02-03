arr = list(map(int, input().split()))
cnt = 2
while len(arr) < 10:
    arr.append(arr[cnt - 1] + (2 * arr[cnt - 2]))
    cnt += 1
print(*arr)