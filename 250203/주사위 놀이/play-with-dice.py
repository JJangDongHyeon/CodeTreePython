arr = list(map(int, input().split()))

arr_result = [0 for i in range(6)]

for i in arr:
    arr_result[i - 1] += 1

for i in range(len(arr_result)):
    print(f'{i + 1} - {arr_result[i]}')