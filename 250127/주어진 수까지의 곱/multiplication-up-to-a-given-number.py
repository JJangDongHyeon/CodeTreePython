arr = input().split()
a, b = int(arr[0]), int(arr[1])
result = 1
for i in range(a, b + 1):
    result *= i

print(result)