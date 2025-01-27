arr = input().split()
a, b = int(arr[0]), int(arr[1])
result = a
for i in range(a, b + 1):
    result = a * result

print(result)