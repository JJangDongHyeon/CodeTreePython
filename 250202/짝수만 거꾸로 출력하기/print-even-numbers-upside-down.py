n = int(input())
arr_a = []; arr_b = list(map(int, input().split()))
for i in arr_b:
    if i % 2 == 0:
        arr_a.append(i)
print(*arr_a[::-1])
    