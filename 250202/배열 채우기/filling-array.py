
arr = []
arr_one = list(map(int, input().split()))
for i in arr_one:
    if i != 0:
        arr.append(i)
    elif i == 0:
        break
print(*arr[::-1])