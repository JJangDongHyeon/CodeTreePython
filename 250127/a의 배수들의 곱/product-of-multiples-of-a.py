arr = input().split()
a, b = int(arr[0]), int(arr[1])
result = 1
for i in range(1, b + 1):
    if i % a == 0:
        result *= i
print(result)