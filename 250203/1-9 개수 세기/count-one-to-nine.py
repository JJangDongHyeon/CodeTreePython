n = int(input())

arr = list(map(int, input().split()))
arr_new = [0 for i in range(9)]

for i in arr:
    arr_new[i - 1] += 1

for i in range(len(arr_new)):
    print(arr_new[i])
