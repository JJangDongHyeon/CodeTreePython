arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
result = 0

if a <= b and a <= c:
    result = a

if b <= a and b <= c:
    result = b
if c <= a and c <= b:
    result = c

print(result)