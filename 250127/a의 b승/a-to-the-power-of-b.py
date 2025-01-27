arr = input().split()
a, b = int(arr[0]), int(arr[1])
result = 1
if b != 0:
    result = a
    for i in range(1, b): 
        result = a * result
print(result)