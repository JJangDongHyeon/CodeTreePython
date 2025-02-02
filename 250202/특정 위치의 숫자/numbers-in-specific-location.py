arr = list(map(int, input().split()))
sum_val = 0

for i in range(1, 11):
    if i == 3 or i == 5 or i == 10:
        sum_val += arr[i - 1]
print(sum_val)