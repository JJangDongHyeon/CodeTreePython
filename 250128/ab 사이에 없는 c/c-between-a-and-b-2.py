arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
d = False
for i in range(a, b + 1):
    if i % c == 0:
        d = True
if d == True:
    print('NO')
else:
    print('YES')