arr = input().split()
a, b = int(arr[0]), int(arr[1])
result = a
for i in range(1, b):
    result = a * result

print(result)