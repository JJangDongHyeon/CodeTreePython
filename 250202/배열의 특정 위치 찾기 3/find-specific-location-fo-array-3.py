arr = list(map(int, input().split()))
sum_val = 0
for i in range(len(arr)):
    if arr[i] == 0:
        sum_val += sum(arr[i - 3:i:])
        break
print(sum_val)